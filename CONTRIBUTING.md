# Adding or changing a system

1. Nodes live in `data/nodes.json`, one object per observing component, shared by every system. Views live in `data/systems.json`. Add a system by adding one object to `systems.json` and only the nodes that don't already exist to `nodes.json`.
2. Every dollar figure is a range with a `confidence` class. If there is no line item, use `embedded_unresolved` and a `funding_parent`; never invent a number. Authorizations are never shown as spending.
3. Every timeline entry carries a `basis` (`documented`, `analog`, `inferred_from_operational_cadence`, `inferred`) and a `trigger` type (`elapsed`, `calendar`, `event`, `attrition`, `funding_cliff`).
4. Run `python3 tools/validate.py` before committing. Zero errors is the bar; warnings are advisory.
5. Commit to `main`; GitHub Pages serves the site. The footer date is stamped at build time.
