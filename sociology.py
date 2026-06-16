import feedparser

from rss_sources import RSS_FEEDS
from topics import TOPICS
from telegram_sender import send_message

articles = []

# Fetch news
for feed_url in RSS_FEEDS:

    feed = feedparser.parse(feed_url)

    for item in feed.entries:

        articles.append({
            "title": item.title,
            "summary": item.get("summary", ""),
            "link": item.link
        })

# Score articles
matches = []

for article in articles:

    text = (
        article["title"] +
        " " +
        article["summary"]
    ).lower()

    score = 0

    for topic, keywords in TOPICS.items():

        for keyword in keywords:

            if keyword in text:
                score += 1

    if score > 0:
        matches.append(
            (score, article)
        )

# Sort
matches.sort(
    key=lambda x: x[0],
    reverse=True
)

# Best article
if matches:

    score, best = matches[0]

    message = f"""
📚 Sociology Daily Insight

📰 News:
{best['title']}

🔗 Source:
{best['link']}

📊 Relevance Score:
{score}
"""

    send_message(message)

else:

    send_message(
        "No sociology article found today."
    )
