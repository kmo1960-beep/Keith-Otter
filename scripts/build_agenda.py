"""
build_agenda.py
Reads calendar_events.json and rss_headlines.json, then writes
agenda/daily_agenda.txt — the final formatted daily briefing file.
"""

import json
import os
import datetime
import pytz

CALENDAR_FILE  = "scripts/calendar_events.json"
RSS_FILE       = "scripts/rss_headlines.json"
OUTPUT_DIR     = "agenda"
TIMEZONE       = "America/Los_Angeles"

tz = pytz.timezone(TIMEZONE)
today = datetime.datetime.now(tz)
date_str = today.strftime("%A, %B %d, %Y")

os.makedirs(OUTPUT_DIR, exist_ok=True)
output_file = os.path.join(OUTPUT_DIR, "daily_agenda.txt")

# ── Load data ──────────────────────────────────────────────────────────────────
with open(CALENDAR_FILE) as f:
    events = json.load(f)

with open(RSS_FILE) as f:
    headlines = json.load(f)

# ── Format ─────────────────────────────────────────────────────────────────────
SEPARATOR = "=" * 60

lines = []

lines.append(SEPARATOR)
lines.append(f"  DAILY BRIEFING — {date_str}")
lines.append(SEPARATOR)
lines.append("")

# ── Calendar Section ───────────────────────────────────────────────────────────
lines.append("📅  TODAY'S AGENDA")
lines.append("-" * 60)

if not events:
    lines.append("  No events scheduled for today.")
else:
    for event in events:
        lines.append(f"  ⏰  {event['time']}")
        lines.append(f"      {event['summary']}")
        if event.get("location"):
            lines.append(f"      📍 {event['location']}")
        if event.get("description"):
            # Truncate long descriptions
            desc = event["description"].strip().replace("\n", " ")
            if len(desc) > 120:
                desc = desc[:117] + "..."
            lines.append(f"      📝 {desc}")
        lines.append("")

lines.append("")

# ── News Section ───────────────────────────────────────────────────────────────
lines.append("📰  FOX NEWS — TOP HEADLINES")
lines.append("-" * 60)

if not headlines:
    lines.append("  No headlines available.")
else:
    for i, item in enumerate(headlines, start=1):
        lines.append(f"  {i:>2}. {item['title']}")
        if item.get("link"):
            lines.append(f"      {item['link']}")
        lines.append("")

lines.append("")
lines.append(SEPARATOR)
lines.append(f"  Generated at {today.strftime('%I:%M %p %Z')} by GitHub Actions")
lines.append(SEPARATOR)

# ── Write output ───────────────────────────────────────────────────────────────
content = "\n".join(lines)
with open(output_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Daily agenda written to {output_file}")
print(f"  Events: {len(events)}")
print(f"  Headlines: {len(headlines)}")
