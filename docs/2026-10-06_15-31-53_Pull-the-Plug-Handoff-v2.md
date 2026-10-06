# Handoff v2: "Pull the Plug" Observing Systems Simulator

**Project:** Keeling Curve Foundation, Data Continuity Initiative
**Owner:** Stephen C. Diggs (SC), Chief Data Officer, KCF
**Handoff date:** October 6, 2026
**Supersedes:** October 4, 2026 handoff (kept in `docs/` for history)
**Status:** Schema v0.1 frozen; data seeded and validating clean; `index.html` v1 built and rendering all six systems
**Repository:** `keelingcurve` GitHub organization. Published at `https://keelingcurve.github.io/pull-the-plug/` (project repo `pull-the-plug`; if SC prefers the root site, the repo is `keelingcurve.github.io` and the path drops).

---

## 1. What changed since October 4

The October 4 handoff described six linear chains. Five research tracks arrived between October 5 and 6 and turned the model into a dependency graph. The three largest shifts:

1. **Shared nodes.** NWLON, NDBC, IOOS, satellite ocean color, and the NCEI archives appear in two or three systems each. They are now defined once in `nodes.json` and referenced by id from `systems.json`. Editing NDBC propagates everywhere.
2. **Clocks belong to paths, not nodes.** One tide gauge feeds three decisions on three timescales; one radiosonde launch feeds today's watch and a 1905 record. Degradation timelines sit on scenarios and name the node they affect at each step.
3. **Decision confidence, not product disappearance.** The failure state is usually not that a decision changes; it's that we lose the evidence to know which decision is right. Every decision node carries its own state vocabulary (open, increased sampling, precautionary closure, status uncertain, safe status cannot be determined), mapped to the 0 to 4 engine.

## 2. Decisions

| Date | Decision |
|---|---|
| Oct 6 | Repository under the `keelingcurve` GitHub organization; site at `https://keelingcurve.github.io/pull-the-plug/`. Not `sdiggs.github.io`. |
| Oct 6 | Schema frozen at v0.1 with five of six research tracks in hand; plankton adds rows, not fields. |
| Oct 6 (default, SC may override) | Opens on the selected system's chain or radial view; the Restore moment is the payoff. |
| Oct 6 (default) | R* and risk vector stored in JSON, hidden from the public; `display.show_rstar` flips it. |
| Oct 6 (default) | Tagline: "The archive lives; the living forecast dies." The certainty sentence carries UI copy. |
| Oct 6 (default) | OHC seeded with funding unresolved; plankton seeded as a stub. |
| Oct 2 | Six systems: coastal erosion, coastal flooding and sea level, HABs, weather balloons with IGRA, plankton and fisheries, ocean heat content. |
| Sep 29 | Three linked views; single HTML, no build step; 0 to 4 scale; "already happened" as a first-class state; ranges with sources, never a bare number. |

## 3. Files delivered in this handoff

```
data/schema.json       JSON Schema draft 2020-12, v0.1, 20 definitions
data/nodes.json        75 nodes, 150 KB
data/systems.json      6 systems, 19 scenarios, 85 KB
tools/validate.py      schema validation plus 12 cross-reference rules
CONTRIBUTING.md        five rules for adding a system
README.md
docs/                  this handoff, the Oct 4 handoff, the weather balloon research track
```

Validator result at handoff: 0 errors, 5 warnings (PORTS and VOS exist as nodes but sit in no branch yet; three plankton stubs unreferenced).

## 4. The data model

### 4.1 Node (nodes.json)

| Field | Purpose |
|---|---|
| `type` | observe, process, transform, model, product, decide, archive, impact |
| `operator[]`, `funders[]` | Kept separate. GLERL runs the Lake Erie ESPs; EPA GLRI paid for them. |
| `funding.cost_annual_usd` | A `money` object (range plus confidence) or null. `embedded_unresolved` is a valid confidence and the UI shows "funding not resolved." |
| `funding.funding_parent` | The larger budget activity, shown labeled as the parent, never as the node's cost. |
| `funding.funding_instruments[]` | Dated awards and appropriations with `award_end`; these drive funding-cliff marks on the rail. |
| `depends_on[]` | `{node, kind: feeds or calibrates, strength: direct, supporting, research}` |
| `substitutes[]` | `{node, degree, cannot_replace[], stated_by}`; mandatory when an agency named the substitute itself. |
| `sampling_role` | Horizontal, vertical, repeat, variables, unique capability. Explains why a substitute is partial. |
| `asset_population` | Count, failure rate, replacements, lifetime. Drives attrition curves. |
| `states` | `{kind: node, decision, or constraint; labels[5]}` |
| `pattern` | Named failure shape: portal_survives_feeders_die, human_transformation_layer, slow_burn_irreversible, immediate_cliff, delayed_seasonal, grant_lapse_cascade, asset_attrition |
| `convergence_point` | True where many inputs become one answer with no redundancy. |
| `people[]`, `users[]` | Named leads with sources; documented recipients of the product. |
| `dated_events[]` | `{date, label, status: realized, enacted, proposed, operational; kind}` |
| `sources[]` | Every node is self-contained; source ids resolve within the node. |

### 4.2 System (systems.json)

| Field | Purpose |
|---|---|
| `layout` | `chain` (five or six boxes) or `radial` (branches around a center). Flooding, HABs, and OHC use radial. |
| `status` | complete, partial, stub. Stubs render with a badge and no numbers (validator enforces). |
| `branches[]` | Ordered node id paths; one marked `headline`. |
| `scenarios[]` | `cut_node`, `lesson`, `what_broke_first`, `already_happened`, `timeline[]`, `record_bar`, `hypothetical_counts[]` |
| `timeline[].trigger` | `elapsed {months}`, `calendar {month_from, month_to}`, `event {event, expected_per_year}`, `attrition {fraction_lost}`, `funding_cliff {instrument_index}` |
| `timeline[].basis` | documented, analog (ECMWF 2015 Russia), inferred_from_operational_cadence, inferred |
| `record_bar` | `{start_year, recoverable: yes, partial, no; gap_label}`; the strip that stays brown after Restore. |
| `exposure[]` | Figure or text, `basis`, and `causal_link: direct, shared_chain, context`. |
| `leverage.mode` | scale, ratio, avoided_loss. The UI computes a ratio only for `ratio`, which requires a `ratio_note`. |
| `bridge` | Written as a commitment: amount, duration, vehicle, keeps, step-down trigger, what philanthropy cannot do. |
| `rstar` | D, P, RRS, DIRS inputs; provisional values, SC to calibrate. |

### 4.3 Rules the validator enforces beyond the schema

Unknown node ids in branches, scenarios, dependencies, substitutes; dependency cycles; funding-cliff indices that don't exist or lack an `award_end`; ratio without a note; authorizations shown as cost or exposure; stubs carrying exposure; source ids that don't resolve (warning).

## 5. Content state by system

| System | Status | Scenarios | Headline scenario | Strongest sourced fact |
|---|---|---|---|---|
| Coastal erosion | complete | 3 | Pull the plug on the airplane (NCMP) | CMHRP $38.511M to $25.245M, 27 FTE, one of three coastlines (FY27 Greenbook) |
| Flooding and sea level | complete | 4 | One tide gauge, three clocks | NWLON 210 to 185, maintenance at 110; IOOS $47.5M to $0 (FY27 CJ) |
| HABs | complete | 4 | PNW toxin sampling | NHABON $3.5M FY24; NCCOS $13.4M Sep 2026 cohort to 2029; 2015 event $97.5M |
| Weather balloons | complete | 3 | The 7 a.m. launch (already happened) | 25 of 30 Kansas mornings missed; April 13 watch 30 min before touchdown; ECMWF 2015 analog |
| Ocean heat content | partial | 4 | Three plugs | XBT: 15% of profiles, 80% of boundary-current profiles |
| Plankton | stub | 1 | none | none |

## 6. Corrections to the September 29 mockup

- PNW HAB Bulletin cadence is event-driven, about six bulletins a year, not twice weekly. The "went dark in week 2" line is replaced by the certainty line.
- NWLON cost line ($25M to $35M) withdrawn; shows parent activity ($186.3M base, $140M FY27 request) labeled as parent.
- PNW sampling cost ($1M to $2M) had no source; shows unresolved with the $1.2M UW ESP award as the only hard number.
- Add a Restore button and the record bar. Add "proposed" styling for FY27 events, distinct from realized ones.
- Add the radial layout.

## 7. Build order

| Step | Deliverable | Owner | Status |
|---|---|---|---|
| 1 | Schema v0.1, nodes.json, systems.json, validator, contributor note | Claude | Done Oct 6 |
| 2 | `keelingcurve/pull-the-plug` repo created, Pages enabled on `main`; files pushed | SC | Pending |
| 3 | `index.html` v1: chain and hub-and-lanes layouts, degradation engine with five trigger types and downstream propagation, Restore and record bar, leverage panel honoring `leverage.mode`, stub badge, proposed/realized/cliff event styling, iframe `postMessage` height, URL state, dark mode, mobile | Claude | Done Oct 6 |
| 4 | Three scripting tasks that replace illustrative data with real data: NWLON station ranking for the headline gauge; GTS launch-time scrape since 2025; WOD profile counts by year and depth | Claude | After step 3 or in parallel |
| 5 | Plankton research track; fold in; OHC funding layer | SC commissions; Claude folds in | Pending |
| 6 | SC content review; verification list (section 8) | SC | Before publishing |
| 7 | Publish to GitHub Pages; embed on KCF staging | SC | After step 6 |

## 8. Verification list before anything goes public

Unverified figures still in the data, all tagged `estimate` and most tagged `context`:

- $1.4T NFIP coverage (KCF brief)
- Zero U.S. surge deaths in 2017 attributed to P-Surge (KCF brief)
- PORTS 33% and 59% reductions (NOAA CJ cites a study; audit the study before `avoided_loss`)
- Per-release radiosonde cost ($200 to $325, secondary)
- $360M scallop closure, snow crab figures, 2,200:1 fisheries ROI (not yet in the data; keep off until the plankton track verifies)

Cleared by primary sources: everything in the FY27 NOAA CJ and USGS Greenbook; USACE NCMP figures; NCCOS and NHABON awards; NOAA Fisheries HAB economic figures; Triple-I and Gallagher Re storm losses; the ECMWF 2015 radiosonde case.

## 8a. How the engine works (for whoever edits scenarios)

At clock `t` months after the cut, each timeline entry fires when its trigger is reached: `elapsed` at `months`; `event` at `12 / expected_per_year`; `calendar` at the first month in the window after the cut; `attrition` at `fraction_lost × typical_lifetime_years × 12` (default lifetime 5 years); `funding_cliff` at the instrument's `award_end`. The affected node takes the entry's level. Levels then propagate downstream along `feeds` edges: `direct` edges pass the level unchanged, `supporting` edges pass it minus one, `research` and `calibrates` edges pass nothing; archive nodes cap inherited degradation at 2 because files persist. Restore sets every node back to 0 and freezes the record-bar gap at the restore month. "Today" is fixed at 2026-10-06 in the script for reproducible share links; move it forward at each publish.

## 9. Conventions

- US spelling. No em dashes. No "foster," "ledger," or "load-bearing."
- Output files carry a UTC timestamp prefix `YYYY-MM-DD_HH-MM-SS_`. Repository source files do not; the repo is versioned by git.
- Footer "last updated" stamped with the actual build date.
- All asset and data paths in `index.html` are relative (`data/systems.json`, not `/data/...`) so the page works at `https://keelingcurve.github.io/pull-the-plug/` and inside the KCF iframe without edits.
- Embed snippet for the KCF site: `<iframe src="https://keelingcurve.github.io/pull-the-plug/" ...>`; the page posts its height to the parent via `postMessage`.
- README has no "Editing" or "Verify before publishing" sections.

---

*Prepared by Claude for SC, October 6, 2026.*
