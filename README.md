# Keith-Otter

AI configuration and workflow hub for Fortune's Kitchen and Bar.

---

## Structure

### /production
**Verified, working configs only.**
Every file here has been tested and confirmed to run without errors.
This is what all AI tools should read first.

| Folder | Purpose |
|---|---|
| `production/shared/master.json` | Universal context — business info every AI needs |
| `production/openai/` | ChatGPT / GPT-5 Mini configs + MCP connection |
| `production/anthropic/` | Claude configs + MCP connection |
| `production/zapier/` | Verified Zapier workflow configs + MCP connection |
| `production/n8n/` | n8n MCP URLs + full credentials map |
| `production/perplexity/` | Perplexity configs |
| `production/copilot/` | GitHub Copilot configs |

### /r-and-d
**Sandbox. Experiments only.**
Nothing here is guaranteed to work.
Do not use in live workflows.

---

## MCP Endpoints

| Service | URL |
|---|---|
| n8n base | `https://app.n8n.cloud/kmo1960` |
| n8n MCP | `https://app.n8n.cloud/kmo1960/mcp-server/http` |
| Zapier MCP | `https://mcp.zapier.com` |

---

## Credentials Setup Order

All API keys are stored **encrypted in n8n only** — never in this repo.
This is the order to add them at `app.n8n.cloud/kmo1960` > Credentials.

### Step 1 — Google (one login covers all three)
- Gmail OAuth2 — `Gmail - Fortune's Kitchen`
- Google Calendar — `Google Calendar - Fortune's Kitchen`
- Google Sheets — `Google Sheets - Fortune's Kitchen`

### Step 2 — OpenAI
- Get key at: https://platform.openai.com/api-keys
- n8n search: `OpenAI`
- Name: `OpenAI - Fortune's Kitchen`

### Step 3 — Anthropic
- Get key at: https://console.anthropic.com/settings/keys
- n8n search: `Anthropic`
- Name: `Anthropic - Fortune's Kitchen`

### Step 4 — GitHub
- Get token at: https://github.com/settings/tokens
- n8n search: `GitHub`
- Name: `GitHub - Fortune's Kitchen`

### Step 5 — QuickBooks
- Connect via QuickBooks login in n8n
- n8n search: `QuickBooks`
- Name: `QuickBooks - Fortune's Kitchen`

### Step 6 — Zapier
- Get key at: https://zapier.com/app/developer
- n8n search: `Zapier`
- Name: `Zapier - Fortune's Kitchen`

### Step 7 — Daily Agenda Webhook
- Create a Webhook node in n8n
- Copy the generated URL
- Paste it into GitHub Secret: `N8N_WEBHOOK_URL`
- Repo secrets: https://github.com/kmo1960-beep/Keith-Otter/settings/secrets/actions

### Step 8 — Zapier Inbound Webhook
- Create a second Webhook node in n8n
- Copy the generated URL
- Paste it into Zapier as the destination for parsed invoice JSON

---

## Security Rules

1. Never store actual API keys in this repo or any config file
2. All keys live encrypted in n8n Credentials vault only
3. This repo maps credential names and sources only
4. Nothing moves to `/production` until it runs without errors
5. Test everything in `/r-and-d` first

---

## AI Stack

| Tool | Plan | Role |
|---|---|---|
| ChatGPT | Plus $20/mo | Agent execution, Zapier, JSON |
| Claude | Pro $20/mo | Reasoning and complex tasks |
| Perplexity | Free | Live research and lookups |
| GitHub Copilot | Free | Code assistance |
| n8n | Cloud | Logic, processing, MCP hub |
| Zapier | — | Triggers and app connections |

---

## MCP Connections

| AI | Method | Server URL |
|---|---|---|
| Claude | OAuth2 | `https://app.n8n.cloud/kmo1960` |
| ChatGPT | Bearer Token | `https://app.n8n.cloud/kmo1960/mcp-server/http` |
| Claude via Zapier | OAuth2 redirect | `https://mcp.zapier.com` |
| ChatGPT via Zapier | Bearer Token | `https://mcp.zapier.com` |

---

*Fortune's Kitchen and Bar — La Quinta, CA*
