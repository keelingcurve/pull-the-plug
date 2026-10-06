# Handoff: "Pull the Plug" Observing Systems Simulator

**Project:** Keeling Curve Foundation, Data Continuity Initiative
**Owner:** Stephen C. Diggs (SC), Chief Data Officer, KCF
**Handoff date:** October 4, 2026
**Status:** Design approved in principle; mockup delivered September 29, 2026; build not started
**Working title:** Pull the plug on one observation. Watch what stops working.

---

## 1. Purpose

A public-facing interactive HTML tool that lets a visitor defund one link in an environmental observing chain and watch, on a clock, what stops working downstream: the forecast, the decision, and the people who depend on it. The goal is persuasion, not reference. The visitor should leave convinced that these systems must be protected and that the cost of protecting them is small next to what they protect.

The tool will be embedded in an iframe on the KCF website and shared as standalone scenario links.

Design constraint set by SC: adding a new system or data stream must require editing one JSON file and nothing else. Maintenance has to be simple enough for a non-developer at KCF.

## 2. Decisions made so far

| Date | Decision |
|---|---|
| Sep 29 | Three linked views sharing one data model: chain view, timeline scrubber, leverage counter. Chain view is the primary surface. |
| Sep 29 | One `index.html` with inline CSS and JS, no build step, plus one `systems.json`. Same pattern as the R* Calculator and the Master Climate Dataset Inventory widget. |
| Sep 29 | Host on `sdiggs.github.io` so `systems.json` can be edited in GitHub's web editor and the tool updates on save. |
| Sep 29 | Use the five-level degradation scale (0 to 4) from the September 29 philanthropy brief. Map the other documents' scales onto it. |
| Sep 29 | "Already happened" is a first-class state, not a footnote. The timeline starts January 2024 and shows realized losses before the visitor's cut. |
| Sep 29 | Each system carries a `risk_vector` field, not a single risk score, because the live threat is administrative (attrition, hiring freezes, contract lapses), not just appropriations. |
| Sep 29 | All dollar figures shown as ranges with sources and a confidence flag. Never a single unsourced number. |
| Sep 29 | DSCOVR is not a headline. NOAA stopped ingesting its solar wind data June 30, 2026; SOLAR-1 is primary. Space weather subsequently dropped from v1 scope. |
| Oct 2 | v1 scope fixed at six systems (see section 4). Drought and space weather dropped. Plankton and ocean heat content added. |
| Oct 2 | IGRA is the archive link at the end of the radiosonde chain, not the chain itself. The radiosonde chain gets six links instead of five. |

### Open decisions (SC to call)

1. Which view opens first for the public: chain view (recommended), timeline, or leverage counter.
2. Whether the R* priority score and risk vector show on screen for the public, or stay in the JSON for internal use only.
3. Whether chains 5 and 6 (plankton, ocean heat content) are drafted now from existing knowledge for SC's review, or wait for commissioned research tracks like the five in the September brief.
4. Tagline confirmation: "The archive lives; the living forecast dies." (from the Sep 29 brief).
5. Repository name and whether the tool lives under `sdiggs.github.io` or a KCF GitHub organization.

## 3. The design

### 3.1 Chain view (primary)

Each system is drawn left to right as a chain of five or six links:

1. Observe (the sensor, survey, launch, or sample)
2. Check and process (QA, lab work, assimilation, the people)
3. Forecast or product (the model output or bulletin)
4. Decide (the closure, warning, quota, or map)
5. Who feels it (named communities, businesses, and health outcomes)
6. Archive (only where the long record is a distinct asset, as with IGRA)

Every link carries: operator, annual cost (range, with confidence flag), what breaks first if it is cut, and how long a missed observation stays missing. Clicking a link cuts its funding. Downstream links degrade in stages through the 0 to 4 scale rather than vanishing, because that is how these systems actually fail.

Under the chain: a legend for the five levels and a one-sentence "what broke first" callout. In the mockup scenario the callout reads: the bulletin went dark in week 2, before anyone outside the lab noticed; the lab's technicians were the single point of failure, not the buoys.

### 3.2 Timeline scrubber

A horizontal rail from January 2024 to roughly 2031. Two segments:

- Dotted rail, left of "Today": losses that have already happened, drawn from each system's `dated_events` array (SEDAC April 2025, NASS county estimates April 2024, NMFS staff losses 2025, MODIS Aqua August 2026, Illinois and Missouri streamgages October and November 2026, Terra MODIS January 2027, and so on).
- Solid rail, right of the cut: what happens after the visitor's cut, keyed to the system's `degradation_timeline`.

A draggable knob shows "N months after the cut." A "Recoverable?" indicator in the side panel flips from yes to partial to no at the irreversibility point. That flip is the persuasive payload.

### 3.3 Leverage counter (side panel)

Two numbers side by side: annual cost to keep the link running versus the economic, property, and life-safety exposure that depends on it. Below: the ratio in plain words ("50 to 1, low estimate"), the recoverability verdict, the basis for the exposure figure with its source, and the philanthropic bridge package phrased as a commitment ("$1.4M/yr keeps sampling, three lab staff, and the bulletin running for 24 months, through NANOOS; step-down trigger when federal funding returns"). R* and risk vector in small type at the bottom, hideable.

### 3.4 Extras for v1.1 or later

- Compare mode: two systems side by side.
- Shareable state: the URL encodes system, cut link, and time (`?system=pnw-hab&cut=observe&t=14m`).
- Scenario presets a KCF staffer can author in JSON without touching code.

### 3.5 Visual direction (from the September 29 mockup)

Mockup file: `2026-09-29_23-14-02_Observing-Systems-Simulator-Mockup.png`.

- Serif display face (Charter or equivalent) for headline and panel titles; a plain sans for UI text.
- Cool light gray base, ink text, four signal colors for the degradation levels: teal (operating), amber (forecasts lose skill), rust (status unknown), dark brown (collapse or lost). Selection highlight in blue.
- No decorative motion. Motion only in response to the visitor's action (cutting a link, dragging the clock).
- Footer "last updated" line stamped with the actual build date.

## 4. The six systems in v1 scope

Set by SC on October 2, 2026. Chains below are sketches for review, not final content.

### 4.1 Coastal and beach erosion

Observe: lidar flights (USGS 3DEP coastal, USACE JALBTCX) and shoreline surveys → Process: USGS Coastal and Marine Hazards and Resources Program (CMHRP) → Product: coastal change forecasts, Coastal Change Hazards Portal → Decide: setback lines, rebuild permits, beach nourishment → Who feels it: homeowners, insurers, county road departments.

Documented numbers: CMHRP FY26 enacted $38.5M to $41.0M (sources conflict; carry both), FY27 request $25.2M. JALBTCX about $10M/yr. The FY27 request states coastal disaster response will be maintained on only one of three coastlines and mapping will concentrate where partner support exists.

Sources: Sep 29 brief rows 14, 15, 18; document 3 (CMHRP budget detail).

### 4.2 Coastal flooding and sea level

Observe: NWLON tide gauges (210 stations), IOOS buoys and HF radar, PORTS → Process: CO-OPS quality control → Product: SLOSH, P-Surge, NWM total water level, STOFS → Decide: evacuation orders, coastal flood warnings, FEMA flood maps → Who feels it: residents, ports and shipping, mortgage and NFIP holders (about $1.4T in coverage keyed to FEMA maps).

Documented numbers: IOOS $42.5M to $47.5M FY26 enacted (sources conflict), $0 requested FY27. NWLON about $25M to $35M/yr (estimate). P-Surge credited with zero U.S. surge deaths in the 2017 hurricane season. Century-long sea level records are the irreversible asset.

Sources: Sep 29 brief rows 8 to 13, 16, 17; document 4 (IOOS funding history).

### 4.3 Harmful algal blooms

Observe: toxin sampling, cell counts, ocean color → Process: regional lab QA (GLERL, FWRI, Mote, University of Washington ORHAB) → Product: HAB bulletins (Gulf of Mexico, Lake Erie, Pacific Northwest, Alaska AHAB) → Decide: shellfish and beach closures, drinking water advisories → Who feels it: harvesters, coastal towns, hospitals.

Documented numbers: NCCOS competitive HAB line $14M/yr, $0 requested FY27; $13.4M awarded September 2026 (runs to about 2029). HABON $2.8M/yr. PNW Bulletin about $1M to $2M/yr (estimate). Exposure anchors: 2015 West Coast Pseudo-nitzschia event, $97.5M lost Dungeness crab landings; 2018 Florida red tide, $2.7B tourism losses; Toledo 2014, 500,000 people without tap water, then $500M in treatment upgrades.

The mockup scenario uses the PNW Bulletin with the sampling link cut and the clock at 14 months.

Sources: Sep 29 brief rows 1 to 7; documents 1, 3, 4, 5.

### 4.4 Weather balloons (NWS upper air network and IGRA)

Observe: NWS radiosonde launches, 92 stations, twice daily at 00Z and 12Z → Process: NCEP data assimilation → Product: numerical model initialization, Storm Prediction Center tornado watches → Decide: shelter orders, school and hospital protocols, aviation routing → Who feels it: families in tornado-prone states, airlines → Archive: IGRA at NCEI, the homogenized record back to the 1940s.

Documented numbers: annual cost ranges from about $20M to $70M across the five documents; flag as a wide estimate until a line item is found. 2025 reporting: at least 11 sites stopped, reduced, or made launches sporadic; one account of 25 of 30 Kansas morning launches missed in a peak season. This track was blocked in the September research run and has the thinnest sourcing of the six.

Teaching point: cutting the launches breaks both today's tornado forecast and the long climate record. Two irreversibilities in one chain.

Sources: documents 1, 3, 4, 5. Not in the Sep 29 brief.

### 4.5 Plankton observations as they relate to fisheries

Observe: Continuous Plankton Recorder lines, Imaging FlowCytobots, survey net tows (NEFSC and other science center cruises, CalCOFI) → Process: taxonomy, counts, imaging classification → Product: ecosystem indicators and prey fields feeding stock assessments → Decide: annual catch limits, season openings → Who feels it: fishing fleets, processors, port towns (New Bedford, Kodiak, Unalaska).

Documented numbers: none yet specific to plankton. Adjacent anchors: NOAA surveys and assessments PPA $205.7M, FY27 proposes a $19M cut; about 400 NMFS staff lost in 2025; five assessments skipped; U.S. seafood economy about $319B to $321B in sales impacts. Bering Sea snow crab collapse (11.7B to 1.9B animals, about $1B in losses) is the cautionary case for an ecosystem shift that plankton indicators are meant to catch early.

Existing KCF material: the IOOS Plankton Community Knowledge Graph work covers operators, instruments, and dependencies and should seed this entry.

Sources: Sep 29 brief rows 33, 34; documents 3, 5; IOOS Plankton KG.

### 4.6 Ocean heat content

Observe: Argo floats, XBT lines, GO-SHIP repeat hydrography → Process: World Ocean Database ingestion and QC at NCEI → Product: NCEI ocean heat content time series, Earth energy imbalance estimates → Decide: hurricane rapid-intensification forecasts, sea level projections, marine heatwave advisories → Who feels it: coastal planners, reinsurers, fisheries managers, the IPCC assessment record.

Documented numbers: none in the current source set. Needs a research track covering U.S. Argo funding (NOAA GOMO), NCEI staffing, and WOD curation. The WOD-WOA Knowledge Rescue project and WOD FLOW work are the internal starting points.

Sources: none yet. Internal: WOD-WOA Knowledge Rescue project; WOD FLOW.

## 5. Source documents and their disagreements

Six documents were ingested between September 29 and October 2, 2026.

| Doc | Description | How to use it |
|---|---|---|
| 1 | Comprehensive seven-category analysis with tables, failure timelines, and a $75M to $120M/yr philanthropic estimate | Supporting; numbers mostly unsourced |
| 2 | Short seven-system strategic table, $5M to $20M/yr per system | Supporting; weakest sourcing |
| 3 | Inventory with a 1 to 5 risk scale, explicit budget citations (CMHRP, USDM, geomagnetic), and the "$1M sensor protects a $1B economy" framing | Best for sourced figures and the leverage-ratio concept |
| 4 | Observation-model-delivery chain framing, Level 0 to 5 degradation scale, three funding instruments, $92M to $225M year-one portfolio | Best for the chain concept and funder requirements |
| 5 | Six-system summary with ROI figures for fisheries (about 2,200:1) | Supporting |
| 6 | Philanthropy brief dated Sep 29, 2026: 38 systems, enacted versus requested versus estimated funding, realized losses with dates, $230M to $400M/yr envelope | Primary seed for `systems.json` |

Known conflicts to carry as ranges in the JSON:

- Radiosonde network annual cost: $20M to $70M.
- IOOS annual: $40M, $42.5M, $47.5M, $56M depending on source and year.
- USGS CMHRP FY26 enacted: $38.5M (doc 3) versus $41.0M (doc 6).
- Fisheries surveys and assessments: $141M (doc 5), $200M+ (doc 2), $205.7M PPA (doc 6).
- Total philanthropic envelope: $75M to $120M (doc 1), $92M to $225M (doc 4), $230M to $400M (doc 6).

Figures to verify against primary sources before anything goes public on the KCF site: Lloyd's $2.4T five-year geomagnetic scenario; Carrington-class $1.5B to $2B/day GDP loss; $360M scallop fishery closure; snow crab population figures; the 2,200:1 fisheries ROI; the $97.5M Dungeness crab figure (NOAA, likely solid).

## 6. Data model

### 6.1 Files

```
/index.html          single page, inline CSS and JS, loads systems.json at runtime
/systems.json        all content; one object per system
/schema.json         JSON Schema for validation
/CONTRIBUTING.md     five lines: how to add a system, how to validate, how to publish
/scenarios.json      optional: named presets (system, cut, time) for sharing
```

### 6.2 System object (draft)

```json
{
  "id": "pnw-hab",
  "name": "Pacific Northwest HAB Bulletin",
  "category": "habs",
  "status": "operating | degraded | lost",
  "headline": "The chain behind a shellfish closure on the Washington coast",
  "tagline_what_broke_first": "The bulletin went dark in week 2 ...",
  "risk_vector": ["attrition", "grant_lapse"],
  "rstar": { "D": 0.8, "P": 0.7, "RRS": 0.3, "DIRS": 0.6 },
  "links": [
    {
      "id": "observe",
      "stage": "Observe",
      "name": "Beach and offshore toxin sampling",
      "operator": "University of Washington ORHAB; NANOOS",
      "cost_annual_usd": { "low": 1000000, "high": 2000000, "confidence": "estimate", "source_ids": ["doc6-r5"] },
      "missed_observation_recoverable": false,
      "what_breaks_first": "...",
      "degradation_timeline": [
        { "months": 0.5, "level": 2, "note": "Twice-weekly bulletin stops" },
        { "months": 3, "level": 3, "note": "Field contracts lapse" },
        { "months": 9, "level": 3, "note": "3 of 4 technicians leave" },
        { "months": 14, "level": 4, "note": "Record has a permanent hole" }
      ]
    }
  ],
  "exposure": {
    "economic_usd": { "low": 98000000, "high": null, "basis": "2015 Pseudo-nitzschia event, $97.5M lost Dungeness crab landings", "source_ids": ["doc3-29"] },
    "property": "...",
    "life_safety": "Domoic acid: seizures, permanent memory loss, death"
  },
  "bridge": {
    "amount_annual_usd": 1400000,
    "duration_months": 24,
    "vehicle": "NANOOS",
    "keeps": "sampling, three lab staff, the bulletin",
    "step_down_trigger": "federal funding restored"
  },
  "dated_events": [
    { "date": "2026-09", "label": "$13.4M NCCOS cohort awarded (runs to ~2029)", "kind": "funding" }
  ],
  "sources": [
    { "id": "doc6-r5", "cite": "KCF philanthropy brief, Sep 29 2026, row 5", "url": "https://www.orhab.uw.edu/project-strategy/" }
  ]
}
```

Rules:

- Every dollar figure has `low`, `high`, `confidence` (enacted | requested | estimate), and `source_ids`.
- Every `degradation_timeline` entry uses the 0 to 4 scale.
- `dated_events` before today render on the dotted rail; the system's own timeline renders on the solid rail after the cut.
- `rstar` inputs are optional; if present the page computes R* = 0.40·D + 0.30·P + 0.20·(1−RRS) + 0.10·DIRS and shows it only if the display flag is on.
- A system is "lost" if its primary observe link has `status: lost`; it still renders, grayed, as a precedent (SEDAC pattern).

### 6.3 Embedding

- `<meta name="viewport" ...>` and responsive layout down to phone width.
- Page posts its rendered height to the parent via `postMessage` so the KCF iframe resizes.
- Reads `?system=`, `?cut=`, `?t=` from the URL to open a specific scenario.
- No external calls at runtime except Google Fonts (with local fallback). All data inline or in `systems.json` on the same origin.

## 7. Build order and timing

| Step | Deliverable | Owner | Target |
|---|---|---|---|
| 1 | SC answers the five open decisions in section 2 | SC | Oct 7, 2026 |
| 2 | `schema.json` and `CONTRIBUTING.md` | Claude | 1 session after step 1 |
| 3 | `systems.json` seeded with systems 1 to 4 from the Sep 29 brief plus the radiosonde entry | Claude | same session |
| 4 | Draft entries for systems 5 and 6, flagged unsourced, for SC review (or hold for research tracks, per decision 3) | Claude | same session |
| 5 | `index.html` v1 with chain view, timeline, leverage counter | Claude | next session |
| 6 | SC content review of all six chains; verify flagged figures | SC | before publishing |
| 7 | Push to GitHub Pages; test iframe embed on KCF staging | SC | after step 6 |
| 8 | v1.1: compare mode, shareable scenarios, scenario presets | Claude | after public v1 |

Every output file carries a UTC timestamp prefix in the form `YYYY-MM-DD_HH-MM-SS_Name.ext`.

## 8. Conventions carried over from earlier KCF tools

- Single-file HTML, no build step, data in a sidecar JSON (R* Calculator, Master Climate Dataset Inventory widget, Data Repository Explorer).
- Hosted on `sdiggs.github.io/<repo>/`.
- US spelling. No em dashes. Footer "last updated" stamped with the actual build date.
- README files do not include "Editing" or "Verify before publishing" sections unless SC asks.

## 9. Files delivered to date

| Date | File |
|---|---|
| 2026-09-29 | `2026-09-29_23-14-02_Observing-Systems-Simulator-Mockup.png` (1440 by 1000 layout at 2x, PNW HAB scenario, clock at 14 months) |
| 2026-10-04 | this handoff |

---

*Prepared by Claude for SC, October 4, 2026. Figures in this document are quoted from the ingested source documents and have not been independently verified; see section 5 for the verification list.*
