# Morning Brief Automation

## Dates
- Created: 2026-07-31
- Last Updated: 2026-07-31
- Current Stage: Active

## AI Company
- Company: Fortun's Kitchen & Bar
- Model(s): Claude (planning/log), LibreOffice Basic macro runtime
- Owner: Keith

## Goal
Keep Morning Brief reliable every day by freezing the working weather macro baseline and running a hybrid model where GitHub Actions provides calendar/news feed support.

## Inputs
- LibreOffice macro in spreadsheet (weather + timestamp on open)
- `/home/runner/work/Keith-Otter/Keith-Otter/.github/workflows/daily_agenda.yml` (calendar/news pipeline)
- Google Calendar source
- RSS/news source

## Output
- Morning Brief sheet weather block stays production-stable in LibreOffice.
- Daily agenda pipeline remains available for calendar/news collection via GitHub Actions.

## Workflow Diagram (Horizontal)
```mermaid
flowchart LR
    A[Open Morning Brief in LibreOffice Calc] --> B[Run RefreshBrief macro]
    B --> C[Fetch weather from Open-Meteo]
    C --> D[Write High/Low + Last Updated timestamp]
    E[GitHub Actions Schedule/Manual Trigger] --> F[/home/runner/work/Keith-Otter/Keith-Otter/.github/workflows/daily_agenda.yml]
    F --> G[Fetch Google Calendar + News]
    G --> H[Build agenda output]
    D --> I[Hybrid Morning Brief Operations]
    H --> I
```

## Milestones
- 2026-07-30 — Weather macro verified end-to-end in LibreOffice.
- 2026-07-31 — Baseline frozen: weather-in-LibreOffice treated as production-stable.
- 2026-07-31 — Hybrid mode documented: LibreOffice macro (weather/timestamp) + GitHub Actions (calendar/news).
- 2026-07-31 — Gmail unread summary deferred until calendar/news flow is consistently reliable.
- 2026-07-31 — Canonical repo decision set as required gate before any automation revival changes.

## Notes Learned
- What worked:
  - Keep current LibreOffice weather macro unchanged as the stable foundation.
  - Use the existing GitHub Actions workflow for calendar/news instead of expanding macro scope right now.
- What failed:
  - Prior external automation dependency (n8n subscription path) was not durable for this use case.
- What to improve:
  - Resolve canonical repository ownership/path before further automation changes.
  - Revisit Gmail unread summary only after calendar/news reliability is confirmed.
