"""
fetch_calendar.py
Fetches today's events from Google Calendar using a service account.
Outputs scripts/calendar_events.json for use by build_agenda.py.

Required environment variables:
  GCAL_CALENDAR_ID  — your Google Calendar ID
  (service_account.json must be present at scripts/service_account.json)
"""

import json
import os
import datetime
import pytz

from google.oauth2 import service_account
from googleapiclient.discovery import build

# ── Config ─────────────────────────────────────────────────────────────────────
SCOPES           = ["https://www.googleapis.com/auth/calendar.readonly"]
SERVICE_ACCOUNT  = "scripts/service_account.json"
OUTPUT_FILE      = "scripts/calendar_events.json"
TIMEZONE         = "America/Los_Angeles"
CALENDAR_ID      = os.environ.get("GCAL_CALENDAR_ID", "primary")

# ── Time window — today only ───────────────────────────────────────────────────
tz    = pytz.timezone(TIMEZONE)
now   = datetime.datetime.now(tz)
start = now.replace(hour=0,  minute=0,  second=0,  microsecond=0)
end   = now.replace(hour=23, minute=59, second=59, microsecond=0)

time_min = start.isoformat()
time_max = end.isoformat()

# ── Auth ───────────────────────────────────────────────────────────────────────
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT, scopes=SCOPES
)
service = build("calendar", "v3", credentials=credentials)

# ── Fetch events ───────────────────────────────────────────────────────────────
print(f"Fetching events for {now.strftime('%A, %B %d, %Y')} ...")
print(f"Calendar ID: {CALENDAR_ID}")

result = service.events().list(
    calendarId=CALENDAR_ID,
    timeMin=time_min,
    timeMax=time_max,
    singleEvents=True,
    orderBy="startTime",
    maxResults=20
).execute()

raw_events = result.get("items", [])
print(f"Found {len(raw_events)} event(s)")

# ── Format for build_agenda.py ─────────────────────────────────────────────────
events = []
for e in raw_events:
    start_data = e.get("start", {})

    # All-day event vs timed event
    if "dateTime" in start_data:
        dt = datetime.datetime.fromisoformat(start_data["dateTime"])
        dt = dt.astimezone(tz)
        time_str = dt.strftime("%I:%M %p")
    else:
        time_str = "All Day"

    events.append({
        "time":        time_str,
        "summary":     e.get("summary", "No title"),
        "location":    e.get("location", ""),
        "description": e.get("description", "")
    })

# ── Write output ───────────────────────────────────────────────────────────────
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(events, f, indent=2, ensure_ascii=False)

print(f"Calendar events written to {OUTPUT_FILE}")
