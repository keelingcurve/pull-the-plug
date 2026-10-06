#!/usr/bin/env python3
"""Validate data/nodes.json and data/systems.json against data/schema.json,
then check everything the schema cannot: node ids that systems reference,
dependency targets, substitute targets, source ids, funding-cliff indices,
and the rules that keep the public display honest.

Usage:  python3 tools/validate.py          (from the repo root)
Exit code 0 = clean. Anything else lists the problems.
"""
import json, sys, pathlib

try:
    import jsonschema
except ImportError:
    sys.exit("pip install jsonschema")

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)

schema = load("schema.json")
nodes_doc = load("nodes.json")
systems_doc = load("systems.json")

problems = []
warnings = []

# 1. Schema validation
validator = jsonschema.Draft202012Validator(schema)
for label, doc in (("nodes.json", nodes_doc), ("systems.json", systems_doc)):
    for err in sorted(validator.iter_errors(doc), key=lambda e: list(e.path)):
        path = "/".join(str(p) for p in err.path)
        problems.append(f"{label}: {path}: {err.message[:200]}")

# 2. Cross-file references
nodes = {n["id"]: n for n in nodes_doc["nodes"]}
if len(nodes) != len(nodes_doc["nodes"]):
    problems.append("nodes.json: duplicate node ids")

for n in nodes_doc["nodes"]:
    src_ids = {s["id"] for s in n.get("sources", [])}
    for d in n.get("depends_on", []):
        if d["node"] not in nodes:
            problems.append(f"node {n['id']}: depends_on unknown node '{d['node']}'")
        if d["node"] == n["id"]:
            problems.append(f"node {n['id']}: depends on itself")
    for s in n.get("substitutes", []):
        if s["node"] not in nodes:
            problems.append(f"node {n['id']}: substitute unknown node '{s['node']}'")
    def check_src(obj, where):
        for sid in obj.get("source_ids", []) or []:
            if sid not in src_ids:
                warnings.append(f"node {n['id']}: {where} cites source '{sid}' not in this node's sources")
    for e in n.get("dated_events", []): check_src(e, "dated_event")
    for p in n.get("people", []): check_src(p, "person")
    fi = n.get("funding", {}).get("funding_instruments", [])
    for i, inst in enumerate(fi):
        check_src(inst, f"funding_instrument[{i}]")
        if inst.get("amount_usd"): check_src(inst["amount_usd"], f"funding_instrument[{i}].amount")
    cost = n.get("funding", {}).get("cost_annual_usd")
    if cost and cost.get("confidence") == "authorized":
        problems.append(f"node {n['id']}: cost_annual_usd cannot be an authorization")

# Cycle check (feeds edges only)
def has_cycle():
    color = {}
    def visit(u, stack):
        color[u] = 1
        for d in nodes[u].get("depends_on", []):
            v = d["node"]
            if v not in nodes: continue
            if color.get(v) == 1:
                problems.append(f"dependency cycle: {' -> '.join(stack + [u, v])}")
                return
            if v not in color: visit(v, stack + [u])
        color[u] = 2
    for u in nodes:
        if u not in color: visit(u, [])
has_cycle()

referenced = set()
for s in systems_doc["systems"]:
    sid = s["id"]
    src_ids = {x["id"] for x in s.get("sources", [])}
    for b in s["branches"]:
        for nid in b["path"]:
            if nid not in nodes: problems.append(f"system {sid}: branch '{b['id']}' references unknown node '{nid}'")
            referenced.add(nid)
    if not any(b.get("headline") for b in s["branches"]):
        warnings.append(f"system {sid}: no branch marked headline")
    for sc in s["scenarios"]:
        if sc["cut_node"] not in nodes: problems.append(f"system {sid}/{sc['id']}: cut_node '{sc['cut_node']}' unknown")
        for i, t in enumerate(sc["timeline"]):
            if t["affects"] not in nodes: problems.append(f"system {sid}/{sc['id']}: timeline[{i}] affects unknown node '{t['affects']}'")
            if t.get("level_high") is not None and t["level_high"] < t["level"]:
                problems.append(f"system {sid}/{sc['id']}: timeline[{i}] level_high < level")
            trig = t["trigger"]
            if trig["type"] == "funding_cliff":
                idx = trig.get("instrument_index")
                fi = nodes[sc["cut_node"]].get("funding", {}).get("funding_instruments", []) if sc["cut_node"] in nodes else []
                if idx is None or idx >= len(fi):
                    problems.append(f"system {sid}/{sc['id']}: funding_cliff instrument_index {idx} not in cut node's funding_instruments")
                elif not fi[idx].get("award_end"):
                    warnings.append(f"system {sid}/{sc['id']}: funding_cliff points at an instrument with no award_end")
    lev = s["leverage"]
    if lev["mode"] == "ratio" and not lev.get("ratio_note"):
        problems.append(f"system {sid}: leverage.mode ratio requires ratio_note")
    for e in s.get("exposure", []):
        for x in e.get("source_ids", []):
            if x not in src_ids: warnings.append(f"system {sid}: exposure '{e['label'][:40]}' cites source '{x}' not in system sources")
        if e.get("value_usd") and e["value_usd"].get("confidence") == "authorized":
            problems.append(f"system {sid}: exposure cannot be an authorization")
    for e in s.get("dated_events", []):
        if e.get("node") and e["node"] not in nodes: problems.append(f"system {sid}: dated_event references unknown node '{e['node']}'")
    if s["status"] == "stub" and s.get("exposure"):
        problems.append(f"system {sid}: stub systems must not carry exposure figures")
    if s["status"] == "complete" and not s.get("bridge"):
        warnings.append(f"system {sid}: complete system without a bridge")

orphans = [nid for nid in nodes if nid not in referenced and not any(nid in [d["node"] for d in m.get("depends_on", [])] for m in nodes.values())]
for o in orphans: warnings.append(f"node '{o}' is referenced by no system branch and no dependency")

# 3. Report
for w in warnings: print("WARN ", w)
for p in problems: print("ERROR", p)
print(f"\n{len(nodes)} nodes, {len(systems_doc['systems'])} systems, {sum(len(s['scenarios']) for s in systems_doc['systems'])} scenarios")
print(f"{len(problems)} errors, {len(warnings)} warnings")
sys.exit(1 if problems else 0)
