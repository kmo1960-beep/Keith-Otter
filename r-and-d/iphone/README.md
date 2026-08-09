# Morning Brief Dashboard
**Date:** 2026-08-09

---

## What It Does
A mobile-first HTML dashboard that loads on your iPhone each morning and shows:

| Card | Data Source |
|---|---|
| Date & Clock | Browser (live) |
| Weather — La Quinta | n8n → weather API |
| Unread Email | n8n → Gmail |
| GitHub Open Issues | n8n → GitHub API |
| Today's Calendar | n8n → Google Calendar |
| AI Summary | n8n → OpenAI |

---

## How to Use

### Step 1 — Build the n8n Workflow
In n8n (`app.n8n.cloud/kmo1960`), create a workflow with:

```
[Webhook Trigger (GET)] → [Weather Node] → [Gmail Node] → [GitHub Node] → [Google Calendar Node] → [OpenAI Node] → [Respond to Webhook]
```

The **Respond to Webhook** node returns JSON shaped like:
```json
{
  "weather":  { "icon": "☀️", "description": "88°F, Sunny" },
  "email":    { "unread": 3 },
  "github":   { "open_issues": 2, "open_prs": 0 },
  "calendar": [
    { "time": "9:00 AM", "title": "Staff Meeting" }
  ],
  "summary": "Good morning Keith! Here's your day…"
}
```

### Step 2 — Open the Dashboard on iPhone
1. Copy `morning-brief-dashboard.html` to iCloud Drive or host it on GitHub Pages
2. Open in Safari → tap Share → **Add to Home Screen**
3. Name it **Morning Brief** and pick the GitHub icon

### Step 3 — Connect the Webhook
When you first open the dashboard, a setup banner appears.
Paste your n8n webhook URL and tap **Save**. The URL is stored locally on your phone.

---

## n8n Workflow Diagram (Horizontal)

```
[Webhook GET]──►[Weather API]──►[Gmail Unread]──►[GitHub Issues]──►[Google Calendar Today]──►[OpenAI Summary]──►[Respond to Webhook]
```

---

## Status
- [x] Dashboard HTML created
- [ ] n8n workflow built and webhook URL saved
- [ ] Added to iPhone Home Screen
- [ ] Weather node connected
- [ ] Calendar node connected
- [ ] AI Summary node connected
