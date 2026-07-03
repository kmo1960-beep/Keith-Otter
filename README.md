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
| `production/openai/` | ChatGPT / GPT-5 Mini configs |
| `production/anthropic/` | Claude configs |
| `production/zapier/` | Verified Zapier workflow configs |
| `production/perplexity/` | Perplexity configs |

### /r-and-d
**Sandbox. Experiments only.**
Nothing here is guaranteed to work.
Do not use in live workflows.

---

## Rules

1. Nothing moves to `/production` until it runs without errors
2. Test everything in `/r-and-d` first
3. When a config works — move it to the matching `/production` folder
4. Keep `master.json` updated with current business info

---

## AI Stack

| Tool | Plan | Role |
|---|---|---|
| ChatGPT | Plus $20/mo | Agent execution, Zapier, JSON |
| Claude | Pro $20/mo | Reasoning and complex tasks |
| Perplexity | Free | Live research and lookups |
| GitHub Copilot | Free | Code assistance |

---

*Fortune's Kitchen and Bar — La Quinta, CA*
