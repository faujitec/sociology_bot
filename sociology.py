import feedparser
from rss_sources import RSS_FEEDS

articles = []

for url in RSS_FEEDS:
    feed = feedparser.parse(url)

    for item in feed.entries:
        articles.append({
            "title": item.title,
            "summary": item.get("summary", ""),
            "link": item.link
        })

print(f"Found {len(articles)} articles")
