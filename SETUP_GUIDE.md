# Daily Agenda Workflow — Setup Guide

This guide walks you through every step required to get the hands-free daily briefing running in your GitHub repository. Once complete, the workflow fires at **6:00 AM Pacific time** every morning with no interaction needed from you.

---

## What the workflow does

1. Connects to Google Calendar with a service account key you generate once
2. Pulls all events scheduled for today
3. Pulls the top 10 headlines from the Fox News RSS feed
4. Combines them into a formatted text file at `agenda/daily_agenda.txt`
5. Auto-commits and pushes that file back to your repo

---

## Step 1 — Enable the Google Calendar API

1. Go to [https://console.cloud.google.com/](https://console.cloud.google.com/) and sign in with the Google account that owns your calendar.
2. Click **Select a project** at the top, then **New Project**. Name it something like `daily-agenda-bot` and click **Create**.
3. From the left menu, go to **APIs & Services → Library**.
4. Search for **Google Calendar API** and click on it, then click **Enable**.

---

## Step 2 — Create a Service Account

A service account lets GitHub Actions authenticate to Google without ever asking for a password.

1. Go to **APIs & Services → Credentials**.
2. Click **Create Credentials → Service Account**.
3. Give it any name (e.g., `agenda-reader`) and click **Create and Continue**.
4. For the role, select **Viewer** (or skip the role — it isn't needed for calendar access via sharing). Click **Done**.
5. On the Credentials page, click the service account email you just created.
6. Go to the **Keys** tab → **Add Key → Create new key → JSON**.
7. A `.json` file will download to your computer. **Keep this file safe — it's the only copy.**

---

## Step 3 — Share your Google Calendar with the Service Account

The service account needs to be explicitly invited to see your calendar events.

1. Open [Google Calendar](https://calendar.google.com) in your browser.
2. In the left sidebar, hover over the calendar you want to share, click the three dots **⋮**, and select **Settings and sharing**.
3. Scroll down to **Share with specific people or groups** and click **Add people**.
4. Paste the service account email (looks like `agenda-reader@your-project-id.iam.gserviceaccount.com`) and set the permission to **See all event details**.
5. Click **Send**.

> **Your Calendar ID** is shown on that same Settings page under **Integrate calendar**. It looks like `yourname@gmail.com` for your primary calendar, or a long string like `abc123@group.calendar.google.com` for other calendars. Copy it — you'll need it in the next step.

---

## Step 4 — Add GitHub Secrets

GitHub Secrets store sensitive values so they never appear in your code.

1. Go to your repository on GitHub: `https://github.com/kmo1960-beep/Keith-Otter`
2. Click **Settings → Secrets and variables → Actions → New repository secret**.

Add these two secrets:

| Secret name | Value |
|---|---|
| `GCAL_SERVICE_ACCOUNT_JSON` | The **entire contents** of the `.json` key file you downloaded in Step 2. Open the file in a text editor, select all, and paste it here. |
| `GCAL_CALENDAR_ID` | Your Calendar ID from Step 3 (e.g., `yourname@gmail.com`) |

---

## Step 5 — Add the workflow files to your repository

Copy the following files from this package into your `Keith-Otter` repository, preserving the folder structure:

```
Keith-Otter/
├── .github/
│   └── workflows/
│       └── daily_agenda.yml      ← the workflow
├── scripts/
│   ├── fetch_calendar.py         ← Google Calendar fetcher
│   ├── fetch_rss.py              ← Fox News RSS fetcher
│   └── build_agenda.py           ← combines both into the output file
└── agenda/
    └── .gitkeep                  ← keeps the folder tracked by git
```

Commit and push these files to your `main` branch.

---

## Step 6 — Verify it works

### Run it manually first
1. Go to your repo on GitHub → **Actions** tab.
2. Click **Daily Agenda Builder** in the left sidebar.
3. Click **Run workflow → Run workflow**.
4. Watch the run complete (takes ~30 seconds).
5. Check the `agenda/daily_agenda.txt` file in your repo — it should contain today's events and headlines.

### Automatic schedule
After the manual test passes, the workflow will run automatically every day at **6:00 AM Pacific (1:00 PM UTC)**. You can verify the next scheduled run in the Actions tab.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `google.auth.exceptions.DefaultCredentialsError` | The `GCAL_SERVICE_ACCOUNT_JSON` secret is empty or malformed — re-paste the full JSON content |
| Calendar returns 0 events (but you have some) | Double-check you shared the calendar with the exact service account email; wait a few minutes for Google to sync |
| `403 Forbidden` on the Calendar API | The Google Calendar API may not be enabled in your project — re-check Step 1 |
| RSS headlines are empty | Fox News occasionally changes their feed URL — check `fetch_rss.py` and update the URL if needed |
| Workflow doesn't run at 6 AM | GitHub Actions scheduled workflows can run up to ~15 min late during high load; this is normal |

---

## Customization

### Change the time zone or run time
Edit the `cron` line in `.github/workflows/daily_agenda.yml`:
```yaml
- cron: '0 13 * * *'   # 1:00 PM UTC = 6:00 AM PDT
```
Use [crontab.guru](https://crontab.guru) to calculate the UTC equivalent of your desired local time. Remember to also update `TIMEZONE` in `fetch_calendar.py` and `build_agenda.py`.

### Add more news sources
In `fetch_rss.py`, add any RSS feed URL to the `RSS_FEEDS` list:
```python
RSS_FEEDS = [
    "https://moxie.foxnews.com/google-publisher/latest.xml",
    "https://feeds.foxnews.com/foxnews/latest",
    "https://your-other-feed.com/rss",   # ← add here
]
```

### Change the number of headlines
Edit `MAX_ARTICLES` in `scripts/fetch_rss.py` (default is 10).

### Add multiple calendars
In `fetch_calendar.py`, you can loop over multiple calendar IDs by modifying the fetch section to call `service.events().list()` for each calendar ID and merge the results before writing the JSON file.
