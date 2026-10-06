# Pull the Plug

Published at https://keelingcurve.github.io/pull-the-plug/

An interactive public tool from the Keeling Curve Foundation's Data Continuity Initiative. A visitor cuts funding to one link in a U.S. environmental observing chain and watches, on a clock, what stops working downstream: the forecast, the decision, and the people who depend on it. Then they restore the funding and see what never comes back.

## Layout

```
data/schema.json     JSON Schema v0.1 for both data files
data/nodes.json      the federal observing dependency graph (shared nodes)
data/systems.json    the six public-facing systems: branches, scenarios, exposure, bridges
tools/validate.py    schema plus cross-reference checks
docs/                research tracks and handoffs
index.html           single-file app, no build step; loads the two data files at runtime
```

## Systems

| id | status | layout |
|---|---|---|
| coastal-erosion | complete | chain |
| coastal-flooding-sea-level | complete | radial |
| habs | complete | radial |
| weather-balloons | complete | chain |
| ocean-heat-content | partial (funding layer unresolved) | radial |
| plankton-fisheries | stub | chain |

## Model in one paragraph

Eight node types (observe, process, transform, model, product, decide, archive, impact). Two edge kinds (feeds, calibrates) with three strengths (direct, supporting, research). Five timing mechanisms (elapsed, calendar, event, attrition, funding cliff). Three state vocabularies (node, decision, constraint), all mapped to a 0 to 4 degradation scale. Dated events carry proposed, enacted, realized, or operational status. Operators are separate from funders. The UI computes a ratio only when a system's `leverage.mode` is `ratio`.

Sources are cited inline in the data files. Figures tagged `estimate` display with a confidence flag.

Last updated: 2026-10-06
