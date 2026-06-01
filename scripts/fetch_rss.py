"""
fetch_rss.py
Fetches the latest headlines from the Fox News RSS feed.
Writes results to scripts/rss_headlines.json for the agenda builder.

RSS feed used: https://moxie.foxnews.com/google-publisher/latest.xml
Fallback feed: https://feeds.foxnews.com/foxnews/latest
"""

import json
import feedparser

RSS_FEEDS = [
    "https://moxie.foxnews.com/google-publisher/latest.xml",
    "https://feeds.foxnews.com/foxnews/latest",
]
OUTPUT_FILE  = "scripts/rss_headlines.json"
MAX_ARTICLES = 10   # Number of top headlines to include

def try_feed(url: str):
    print(f"  Trying feed: {url}")
    feed = feedparser.parse(url)
    if feed.entries:
        print(f"  OK — {len(feed.entries)} entries found")
        return feed
    print("  No entries; trying next feed...")
    return None

feed = None
for url in RSS_FEEDS:
    feed = try_feed(url)
    if feed:
        break

if not feed or not feed.entries:
    print("WARNING: Could not fetch any Fox News entries. Writing empty list.")
    headlines = []
else:
    headlines = []
    for entry in feed.entries[:MAX_ARTICLES]:
        headlines.append({
            "title":   entry.get("title", "(No title)"),
            "link":    entry.get("link", ""),
            "summary": entry.get("summary", ""),
        })
    print(f"  Collected {len(headlines)} headlines")

with open(OUTPUT_FILE, "w") as f:
    json.dump(headlines, f, indent=2)

print(f"  Saved to {OUTPUT_FILE}")
