"""
fetch_calendar.py
Fetches today's events from Google Calendar using a Service Account.
Writes results to scripts/calendar_events.json for the agenda builder.
"""

import os
import json
import datetime
import pytz
from googleapiclient.discovery import build
from google.oauth2 import service_account

# ── Configuration ──────────────────────────────────────────────────────────────
SERVICE_ACCOUNT_FILE = "scripts/service_account.json"
CALENDAR_ID = os.environ.get("GCAL_CALENDAR_ID", "primary")
TIMEZONE = "America/Los_Angeles"
OUTPUT_FILE = "scripts/calendar_events.json"

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# ── Auth ───────────────────────────────────────────────────────────────────────
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

service = build("calendar", "v3", credentials=credentials, cache_discovery=False)

# ── Time range: full calendar day in local timezone ────────────────────────────
tz = pytz.timezone(TIMEZONE)
now_local = datetime.datetime.now(tz)
start_of_day = now_local.replace(hour=0, minute=0, second=0, microsecond=0)
end_of_day   = now_local.replace(hour=23, minute=59, second=59, microsecond=0)

time_min = start_of_day.isoformat()
time_max = end_of_day.isoformat()

print(f"Fetching calendar events for {now_local.strftime('%A, %B %d, %Y')}")
print(f"  Range: {time_min}  →  {time_max}")
print(f"  Calendar ID: {CALENDAR_ID}")

# ── Fetch events ───────────────────────────────────────────────────────────────
events_result = service.events().list(
    calendarId=CALENDAR_ID,
    timeMin=time_min,
    timeMax=time_max,
    singleEvents=True,
    orderBy="startTime",
).execute()

events = events_result.get("items", [])
print(f"  Found {len(events)} event(s)")

# ── Serialize to JSON for agenda builder ──────────────────────────────────────
output = []
for event in events:
    start = event["start"].get("dateTime", event["start"].get("date", ""))
    end   = event["end"].get("dateTime",   event["end"].get("date", ""))

    # Parse and reformat to human-readable local time
    try:
        start_dt = datetime.datetime.fromisoformat(start).astimezone(tz)
        end_dt   = datetime.datetime.fromisoformat(end).astimezone(tz)
        time_str = f"{start_dt.strftime('%I:%M %p')} – {end_dt.strftime('%I:%M %p')}"
    except Exception:
        time_str = start  # fallback: raw string

    output.append({
        "summary":     event.get("summary", "(No title)"),
        "time":        time_str,
        "location":    event.get("location", ""),
        "description": event.get("description", ""),
    })

with open(OUTPUT_FILE, "w") as f:
    json.dump(output, f, indent=2)

print(f"  Saved to {OUTPUT_FILE}")
