# Research Track: NWS Upper-Air Network (Weather Balloons) with IGRA as the Archive Link

**For:** Pull the Plug simulator, Keeling Curve Foundation Data Continuity Initiative
**Prepared:** October 6, 2026
**Status:** Ready to seed `systems.json`. Gaps are marked where a figure is unresolved rather than estimated.
**System boundary:** federal components that create, transmit, assimilate, forecast from, deliver, or preserve U.S. radiosonde observations. Radar, satellites, and surface mesonets are treated as sibling inputs to the models, not as part of this system.

---

## The one-paragraph version

The National Weather Service launches balloons carrying radiosondes from 92 stations in North America and the Pacific, twice a day at 00Z and 12Z, with special releases at 06Z and 18Z or as needed for critical weather. The program is run by the NWS Office of Observations and also supports 10 Caribbean stations. The data initialize numerical weather models and anchor the Storm Prediction Center's severe weather outlooks. Since February 2025, staffing losses have caused suspensions and reductions at more than a dozen sites, concentrated in the Plains and Upper Midwest; by spring 2026, members of Congress documented 25 of 30 morning launches missed at Kansas sites during peak tornado season and a 30-minute tornado watch lead time in the April 13, 2026 Kansas City outbreak. The same soundings feed the Integrated Global Radiosonde Archive at NCEI, a record that begins in 1905. A missed launch degrades today's forecast and leaves a permanent hole in that record. This is one system with two irreversibilities.

---

## Component inventory

| Component | Federal home | Function | Funding we can defend | Cadence | 2026 status |
|---|---|---|---|---|---|
| NWS Upper-Air Observations Program | NWS Office of Observations, Silver Spring MD | Operates 92 radiosonde stations (69 CONUS, 13 Alaska, 9 Pacific, 1 Puerto Rico); supports 10 Caribbean CHUAS stations | **Embedded, unresolved.** Inside the NWS Observations PPA (about $255M in the FY25 request, ORF). No upper-air line item located. | 00Z and 12Z daily; 06Z/18Z specials | Operating with reductions; NWS says "almost all" 92 sites functioning normally |
| Weather Forecast Office launch staff | NWS WFOs (co-located at most sites) | Prepare, inflate, release, and track the flight; about 1 hour prep | Embedded in WFO staffing | Per launch | Single point of failure in 2025–26; pre-dawn launches dropped where staffing fell |
| Radiosonde Replacement System (RRS) ground stations | NWS | GPS tracking antenna, signal processing, workstation; replaced Micro-ART | Capital, embedded in NWS Systems Acquisition | Continuous | Operating |
| Autolaunchers | NWS | Automated launch units; 24 balloons per load, 12 days unattended; Alaska pilot, planned for about 25% of network | Alaska units funded by spectrum sale proceeds, not appropriations | Per launch | Partially deployed; extent of CONUS rollout unresolved |
| Consumables: radiosondes, balloons, hydrogen or helium | NWS procurement (Vaisala named as radiosonde vendor in press) | About 75,000 sondes released per year; about 20% recovered | Per-release cost reported at $200 to $325 across sources; treat as estimate | Per launch | 2022 helium shortage reduced launches at about 9% of sites; most sites since converted to hydrogen |
| GTS and NOAAPort transmission | NWS NCO / RTH Washington | Distributes soundings to all WFOs, NCEP, and the world | Embedded | Real time | Operating; suspension notices issued through this channel |
| NCEP data assimilation (GFS, RAP, HRRR) | NWS NCEP / EMC | Ingests soundings to initialize models | Embedded | Model cycles | Operating |
| Storm Prediction Center outlooks and watches | NWS SPC, Norman OK | Convective outlooks, tornado and severe thunderstorm watches | Embedded in NWS | Daily, event driven | Operating; April 2026 KC watch issued ~30 minutes before first touchdown |
| WFO warnings and dissemination | NWS WFOs, NOAA Weather Radio, WEA | Tornado warnings to the public | Embedded | Event driven | Operating; some offices no longer 24/7 |
| Commercial GNSS radio occultation | NESDIS Commercial Data Program | Partial substitute for upper-air profiles; 10,000 profiles/day | $67.054M over two years, announced Sept 2026 (from doc 3) | Continuous | Operating; does not replace in-situ humidity/wind detail near the surface |
| IGRA v2.2 | NOAA NCEI | Quality-assured archive of radiosonde and pilot balloon data, 2,800+ stations, 1905 to present, updated daily from about 800 to 900 reporting stations | Embedded in NCEI (NCEI FY25 request $73.29M, not line-itemed) | Daily updates | Operating; v2.2 began 2023 to ingest BUFR-format reports |

---

## 1. The network

NWS Office of Observations staff oversee 92 radiosonde stations in North America and the Pacific Islands plus the 10-station Cooperative Hurricane Upper Air Stations program in the Caribbean. Launches are at 00Z and 12Z, with SPECI releases at 06Z and 18Z or as needed for critical weather. The office also develops and tests the ground systems and the balloon flight train.
Source: https://www.weather.gov/upperair/

Station breakdown: 69 in the conterminous U.S., 13 in Alaska, 9 in the Pacific, 1 in Puerto Rico. The NWS fact sheet itself notes that because of funding and resource limits, not all stations provide twice-daily soundings every day.
Source: https://www.weather.gov/upperair/factsheet

Scale: roughly 75,000 radiosondes released per year nationally; about 20% are recovered and reconditioned.
Source: https://www.weather.gov/rev/upperair

Alaska launches are flagged by NOAA as especially important for downstream Lower 48 forecasts.
Source: https://www.noaa.gov/stories/up-up-and-away-6-benefits-of-automated-weather-balloon-launches

## 2. Funding: what we can and cannot say

- No upper-air line item exists in the NOAA Congressional Justification. The program sits inside the NWS Observations PPA, which was about $255M in the FY25 request (ORF). Represent as `embedded_unresolved`.
  Source: https://www.noaa.gov/sites/default/files/2024-03/NOAA_FY25_Congressional_Justification.pdf
- FY27 request for NWS overall: $1.504B, a 2.7% increase over FY26. The House Appropriations Committee's FY27 CJS bill recommends $1.6B for NWS, including $40M to expand the National Mesonet. Neither document breaks out radiosondes.
  Sources: https://republicans-science.house.gov/_cache/files/6/2/62ab6dcc-da12-4a11-add5-dc8cec492630/CA20681883AEB28A5CF5F9B4AD3D027EEE3EF877E96FC71932EC163D246C1A4F.04.28.26-fy27-noaa-budget-hearing-charter.pdf ; https://thebridge.agu.org/2026/05/26/fy2027-appropriations-update-nasa-noaa-and-nsf/
- Per-release cost: $200 (one secondary source) to $300–325 (doc 5). At 75,000 releases, consumables alone are on the order of $15M to $24M per year. This is arithmetic from estimates, not a budget figure; tag `confidence: estimate`.
- Alaska autolaunchers were paid for by spectrum sale proceeds, described by NOAA as cost-neutral to taxpayers.
  Source: https://www.noaa.gov/stories/up-up-and-away-6-benefits-of-automated-weather-balloon-launches
- Comparator: NOAA's September 2026 commercial GNSS-RO purchase of $67.054M over two years for 10,000 profiles/day (doc 3). That is the price the government pays for a partial substitute.

The key point for the leverage counter: the cost of restoring twice-daily launches at the affected sites is a staffing cost at a dozen or so WFOs, not a program-scale number. The 2025 reductions were caused by vacancies, not by the balloon budget.

## 3. What happened, in order

| Date | Event | Source |
|---|---|---|
| 2021 | Chatham, MA launches paused after coastal erosion made the site unsafe (a coastal erosion dependency inside the radiosonde system) | https://ipmnewsroom.org/unprecedented-cuts-to-midwest-weather-balloon-launches-could-make-it-harder-to-forecast-storms/ |
| Mar 29, 2022 | Helium shortage and a hydrogen contract issue reduce launches at about 9% of 101 upper-air sites | https://weather.gov/bou/HeliumShortageandBalloonLaunches |
| Feb 2025 | About 1,000 NOAA positions cut; Kotzebue, AK launches suspended indefinitely | https://www.businesswire.com/news/home/20250228603358/en |
| Mar 11, 2025 | NWS data management notice: launches suspended at Albany NY, Gray ME, Kotzebue AK "due to a lack of Weather Forecast Office staffing" | https://weather.gov/source/datamgmt/DM032506.txt |
| Mar 20, 2025 | Omaha NE and Rapid City SD suspended; Aberdeen SD, Grand Junction CO, Green Bay WI, Gaylord MI, North Platte NE, Riverton WY reduced to once daily | https://www.axios.com/2025/03/21/nws-layoffs-cuts-weather-balloons-forecasts ; https://nebraskapublicmedia.org/en/news/news-articles/nebraska-south-dakota-hit-with-unprecedented-cuts-to-weather-balloon-launches-across-the-midwest/ |
| Mar 2025 | About 17% of U.S. balloon sites doing partial or no launches (AP via Euronews) | https://euronews.com/green/2025/03/24/embarrassing-bad-and-frankly-dangerous-experts-react-to-drop-in-us-weather-balloon-launche |
| Spring 2025 | Half of NWS offices at an estimated 20% vacancy; reductions reported in OR, SD, NE, TX, FL, AZ, LA; suspensions in WA, FL, CO, MA | https://www.yahoo.com/news/noaa-restores-key-roles-heels-133956915.html |
| Jun 2025 | Rep. Davids letter to Commerce on NWS staffing after an EF-3 near Kansas City | https://davids.house.gov/media/press-releases/davids-escalates-calls-weather-safety-demands-federal-action-restore-vital |
| Apr 13, 2026 | Kansas City outbreak, EF-2 tornadoes; morning launches reportedly skipped across the Midwest; SPC tornado watch issued about 30 minutes before first touchdown | https://www.bostonglobe.com/2026/04/28/metro/tornadoes-severe-weather-balloons-storms/ ; https://www.nbcnews.com/weather/tornadoes/tornadoes-kansas-concerns-changes-national-weather-service-rcna331826 |
| Apr 22, 2026 | Davids letter to Lutnick asking whether launches were missed and whether changes are permanent; Sens. Peters and Slotkin letter to NWS Director Ken Graham on a Michigan event | https://www.kctv5.com/2026/05/23/you-dont-get-quietly-scale-back-congresswoman-demands-answers-nws/ ; NBC above |
| May 2026 | Public upper-air records show 25 of 30 standard morning launches missed at Kansas sites | https://davids.house.gov/media/press-releases/davids-escalates-calls-weather-safety-demands-federal-action-restore-vital |
| May 6, 2026 | NPR: launches shifted from pre-dawn to office hours at some sites; NWS says almost all 92 sites functioning normally with only a few missed launches; NWS reports more than 200 positions filled | https://www.npr.org/2026/05/06/nx-s1-5805228/tornado-outbreaks-catch-forecasters-by-surprise-after-national-weather-service-cuts ; https://lawrencekstimes.com/2026/06/22/kns-ks-mo-surprised-tornados/ |
| Aug 19, 2026 | 33 members of Congress demand restoration of twice-daily schedule; letter cites about 15% NWS workforce reduction | https://davids.house.gov/media/press-releases/davids-escalates-calls-weather-safety-demands-federal-action-restore-vital |
| Sep 2026 | NOAA buys $67M of commercial GNSS-RO profiles over two years | doc 3 |

NOAA's position throughout: "Weather model performance has not been impacted by any changes to the schedule of our twice-daily radiosonde launches." The simulator should show this statement alongside the missed-launch record and let the visitor weigh it. The honest framing is that forecast skill is noisy day to day and a single missed sounding is hard to attribute, which is exactly why data-denial experiments exist (section 5).
Source: https://www.bostonglobe.com/2026/04/28/metro/tornadoes-severe-weather-balloons-storms/

## 4. The mechanism: why one missing morning sounding matters

A sounding gives the vertical profile of temperature, humidity, and wind. Forecasters use it to evaluate instability and shear, the two ingredients of severe convection; NWS Green Bay describes the vertical distribution as critical for forecasting severe thunderstorms and tornadoes.
Source: https://www.weather.gov/grb/ua

The 12Z (7 a.m. Central) sounding is the one that matters most for a same-day outbreak: it samples the morning atmosphere before storms initiate. A launch delayed to midday, as reported in spring 2026, arrives after convection is already underway. That is the specific failure mode behind the April 13 case, and it is a staffing-hours problem, not a budget-line problem.
Source: https://lawrencekstimes.com/2026/06/22/kns-ks-mo-surprised-tornados/

## 5. Documented degradation: the evidence base

The strongest evidence does not come from U.S. press reports. It comes from a real-world case and from controlled experiments.

**Russia, 2015.** When Roshydromet cut radiosonde reports in early 2015, ECMWF's automated monitoring caught the change within weeks. ECMWF ran paired forecasts (full data versus the reduced set) and found a significant degradation: errors grew first over Russia, then moved downstream over the Pacific, and at longer lead times affected forecast scores for the whole Northern Hemisphere. Impact was greatest in winter, when satellite data over land are used less. ECMWF took the results to Roshydromet.
Source: https://www.ecmwf.int/en/newsletter/149/meteorology/global-radiosonde-network-under-pressure

This is the closest documented analog to a U.S. network reduction, and it supplies a `basis: documented` entry for the degradation timeline: the hit is immediate at short range and propagates downstream within days.

**Data-denial experiments.** In NCEP GFS experiments, denying radiosondes increased wind and temperature forecast errors more than denying AMSU satellite radiances in the 3DVar system, with the largest improvements from radiosondes in upper-tropospheric wind and in the extratropics.
Source: https://doi.org/10.1155/2015/280546

ECMWF's global observing system experiments show the present system is resilient to losing any single observing type, with conventional observations (radiosondes among them) giving clear benefits and the largest degradation occurring when several types are lost together.
Source: https://www.ecmwf.int/sites/default/files/elibrary/2019/18859-global-observing-system-experiments-ecmwf-assimilation-system.pdf

Taken together: the global network is redundant enough that NOAA's "no measurable model impact" statement can be true for hemispheric skill scores while a regional morning gap still removes the one profile a forecaster needed for a same-day watch. Both things hold. The simulator should say so.

## 6. IGRA: the archive link

The Integrated Global Radiosonde Archive, maintained by NCEI since 2004, holds quality-assured radiosonde and pilot balloon data from more than 2,800 stations, period of record 1905 to present, updated daily from about 800 to 900 currently reporting stations. Version 2.2 (began 2023) added BUFR-format streams so that stations switching formats could continue to be updated. Derived products include RATPAC, the radiosonde temperature record used for climate trend assessment.
Sources: https://www.ncei.noaa.gov/products/weather-balloon/integrated-global-radiosonde-archive ; https://www.ncei.noaa.gov/pub/data/igra/igra2-product-description.pdf ; https://climatedataguide.ucar.edu/climate-data/integrated-global-radiosonde-archive-igra

IGRA team contact: ncei.igra@noaa.gov. Named maintainers in NCEI presentations: Imke Durre and Xungang Yin.
Source: https://cpaess.ucar.edu/sites/default/files/2023-08/Durre-Imke.pdf

Two distinct failure modes, which the simulator should separate:

1. **Upstream gap.** The archive keeps running but has nothing to ingest for a station on the days launches were missed. The 25 of 30 missed Kansas mornings in spring 2026 are already permanent holes in Topeka's and Dodge City's IGRA records. No funding restores them. This is Level 4 for those observations from the moment they are missed, even while the station itself is "operating."
2. **Archive service loss.** If NCEI curation stopped (the SEDAC pattern), the files would persist somewhere but daily updates, QA, station metadata maintenance, and derived products would not. That is a Level 3 service failure that becomes Level 4 if preservation itself lapses.

External dependency worth recording: ECMWF's reanalysis and homogenized radiosonde products (RHARM) build on IGRA. A U.S. archive failure propagates into European climate records.
Source: https://www.ecmwf.int/node/37592

## 7. Exposure

- Severe convective storms caused $51B in U.S. insured losses in 2025, the third straight year above $50B; total economic damage exceeded $68B. March 2025 alone had a record 300+ tornadoes and $8.4B insured.
  Source: https://www.carriermanagement.com/news/2026/04/16/286826.htm
- Aon puts 2025 global SCS insured losses at $61B, now the costliest insured peril of the century, driven by U.S. outbreaks.
  Source: https://www.captive.com/news/severe-convective-storms-now-costliest-insured-peril-globally
- The March 13–16, 2025 outbreak: at least 118 tornadoes across 15 states, 43 fatalities, insured losses approaching $7.7B. The May 16, 2025 outbreak: at least 27 tornado deaths in a single day; an EF-4 in Kentucky killed 19.
  Sources: https://www.nbcdfw.com/news/business/money-report/insurers-just-marked-the-costliest-first-half-of-the-year-since-2011/3888811/?amp=1 ; https://www.itiger.com/hans/news/2537133687
- NOAA's own estimate cited in a Senate report: extreme weather since 2022 has caused 1,534 fatalities and $461.6B in damage.
  Source: https://www.govinfo.gov/content/pkg/CRPT-119srpt88/pdf/CRPT-119srpt88.pdf

Attribution caution for the leverage counter: these are the exposures that depend on severe weather forecasting as a whole, not on radiosondes alone. The honest ratio compares the staffing cost of restoring morning launches at the affected Plains sites (low single-digit millions, estimate) against the share of warning lead time that soundings provide. Present the exposure as "what the warning system protects" and the cost as "what the missing link costs," and label the ratio as an upper bound.

## 8. Named people and documented users

People (sourced, current as of their citation):
- Ken Graham, NWS Director (recipient of the Peters/Slotkin letter)
- Imke Durre, Xungang Yin, NCEI IGRA team
- John Dean, CEO, WindBorne Systems (offered free Alaska balloon data after Kotzebue suspension)
- Rep. Sharice Davids (KS); Sens. Gary Peters and Elissa Slotkin (MI); the 33 signatories of the August 2026 letter
- Dr. Kevin Schrab, Portfolio Manager, NWS Office of Observations (confirmed current via NOAA VLab listing, Oct 2026). Oversees the Surface and Upper Air Division, NDBC, and radar. Signed the 2009 Radiosonde Replacement System implementation notices as Chief of the Observing Services Division; represents the U.S. on WMO WIGOS. kevin.schrab@noaa.gov, (301) 427-9320. Sources: https://vlab.noaa.gov/web/obs/office-of-observations-obs ; https://www.weather.gov/media/notification/tins/tin09-22rrs_schedule.pdf ; https://www.icams-portal.gov/resources/ofcm/odwr37/r37_odw.pdf

Documented users of the soundings:
- NCEP models (GFS, RAP, HRRR) and every WFO
- Storm Prediction Center
- National Hurricane Center (model initialization)
- Commercial and broadcast meteorologists (e.g., station in-house models cited in press)
- Aviation (turbulence, winds aloft)
- ECMWF and the global NWP community via GTS
- Climate researchers via IGRA and RATPAC

## 9. Dependency graph

```text
WFO launch staff ──┐
Consumables ───────┤
Autolaunchers ─────┤  (partial substitute for staff)
                   ↓
          Radiosonde launch (92 sites, 00Z/12Z)
                   │
      ┌────────────┼────────────────┐
      ↓            ↓                ↓
   GTS / NOAAPort  Local WFO     NCEI ingest
      ↓            analysis         ↓
   NCEP DA         (sounding       IGRA v2.2
   (GFS/RAP/HRRR)   plots)           ↓
      ↓            ↓             RATPAC, reanalyses,
   SPC outlooks ───┘             ECMWF RHARM
   and watches
      ↓
   WFO tornado warnings
      ↓
   Public, schools, hospitals, aviation, insurers

Commercial GNSS-RO ──→ NCEP DA   (sibling input; partial redundancy)
Satellite sounders ──→ NCEP DA   (sibling input; weaker over land in winter)
Radar, mesonets ─────→ WFO warnings (sibling inputs; detect, do not predict)
```

Convergence points: the launch itself (everything downstream depends on it, and it is the only node with no redundancy for in-situ profiles), and SPC watches (where model guidance becomes a decision).

## 10. Degradation clock

Levels: 0 operating, 1 diminished, 2 forecasts lose skill or currency, 3 decision capability seriously degraded, 4 collapsed or irretrievably lost observation.

| Cut | 1 day | 1 week | 1 month | 6 months | 1 year | 5 years | Basis |
|---|---|---|---|---|---|---|---|
| Morning (12Z) launches at Plains sites, staffing | 2 same-day severe outlook loses its pre-convective profile | 2–3 during active pattern | 3 in season | 3 | 3 | 3; IGRA holes at 4 from day one | documented (Apr–May 2026 record; ECMWF 2015 analog) |
| All launches at one site | 1 (neighbors cover) | 1–2 | 2 | 2–3 | 3 | 3; site record at 4 | documented (NWS 2022 notice says neighbors partially compensate) |
| 17% of network (the March 2025 state) | 2 regionally | 2–3 | 3 | 3 | 3–4 | 4 for the record | documented (AP count; ECMWF 2015 propagation) |
| Consumables supply (helium, sondes) | 1 (stock on hand) | 1–2 | 2–3 | 3 | 3 | 3 | documented (2022 helium shortage behavior) |
| NCEP assimilation of soundings | 3 immediately | 3–4 | 4 | 4 | 4 | 4 | inferred_from_operational_cadence |
| SPC watch function | 4 for watches | 4 | 4 | 4 | 4 | 4 | inferred_from_operational_cadence |
| IGRA curation at NCEI | 0 (files persist) | 1 | 2 (daily updates stop) | 3 | 3 | 4 if preservation lapses | inferred (SEDAC analog) |

## 11. Three scenarios for the simulator

**Scenario A: Pull the plug on the 7 a.m. launch.** Cut staffing hours, not the program. Nothing shows in the budget. The balloon goes up at noon instead. On a quiet day nothing happens. On April 13 the watch comes 30 minutes before the first tornado. This is the scenario that already happened and the one the public will recognize. Lesson: the program line survived intact; the capability didn't.

**Scenario B: Pull the plug on the network.** Cut 17% of sites, the March 2025 state. Models keep running on satellites and GNSS-RO. Hemispheric skill scores barely move, which is what NOAA says. Regional forecasts for the Plains and Upper Midwest, where the sites were cut, lose the profiles that matter for convection. ECMWF's 2015 Russia case shows the degradation spreading downstream within days. Lesson: redundancy at the global scale is not redundancy where the tornadoes are.

**Scenario C: Pull the plug on the archive.** Cut IGRA curation. Every forecast still runs. Nobody notices for months. Then the 120-year temperature record stops updating, RATPAC stops, European reanalyses lose their U.S. source. Lesson: the forecast and the record are the same balloon; defund one link and you lose both, on different clocks.

## 12. Philanthropic bridge (draft, for SC to shape)

What philanthropy cannot do: pay federal forecasters directly (Antideficiency Act). What it can do, through cooperative institutes and universities:

- Fund supplemental soundings during severe weather periods from university meteorology programs with mobile sounding capability (OU, Texas Tech, Nebraska, Iowa State, and others run such programs). Order of $1M to $3M per season for a Plains corridor. Estimate.
- Fund autolauncher procurement at the sites with the worst staffing record, if NWS can accept the equipment under a partnership agreement. Unit cost unresolved; the 2018 plan put autolaunchers at 25% of the network.
- Fund an independent monitor: a public dashboard of launch completion by site and hour, built from the GTS record, so that "25 of 30 missed" is visible in real time rather than discovered by a Congressional office months later. Low six figures. This is the cheapest intervention and the one most aligned with KCF's role.
- Fund IGRA continuity: a mirror and a curation partnership with NCEI, SEDAC-pattern insurance. Low six figures per year.

## 13. Open items

1. No autolauncher unit cost or current deployment count. Ask NWS Office of Observations or find the procurement notice.
2. No authoritative per-release cost. The $200 and $300–325 figures are secondary.
3. The NPR source names a meteorologist "Morales" analyzing launch gaps; identify and cite properly before quoting.
4. Resolved Oct 6, 2026: Kevin Schrab confirmed as Office of Observations Portfolio Manager. He is the right person to verify the dependency graph in section 9, the autolauncher deployment count (open item 1), and the per-release cost (open item 2) in one conversation.
5. The GTS record of actual launch times by site for 2025–26 would turn the Kansas anecdote into a national dataset. This is a scraping task against NCEI's or Wyoming's sounding archives and would be the single most valuable addition to the system's `dated_events`.

---

*Sources are given inline. Figures tagged "estimate" are secondary or derived and should display with a confidence flag. All dates are as reported by the cited source.*
