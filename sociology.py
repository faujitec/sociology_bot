import feedparser

from rss_sources import RSS_FEEDS
from taxonomy import TOPICS
from telegram_sender import send_message

from gemini_client import analyze_article
from prompt_templates import SOCIOLOGY_PROMPT

articles = []

# ------------------------
# FETCH ARTICLES
# ------------------------

for feed_url in RSS_FEEDS:

    feed = feedparser.parse(feed_url)

    for item in feed.entries:

        articles.append({
            "title": item.title,
            "summary": item.get("summary", ""),
            "link": item.link
        })

# ------------------------
# SCORE ARTICLES
# ------------------------

matches = []

for article in articles:

    text = (
        article["title"] +
        " " +
        article["summary"]
    ).lower()

    score = 0

    matched_topics = []

    for topic, keywords in TOPICS.items():

        topic_score = 0

        for keyword in keywords:

            if keyword.lower() in text:

                topic_score += 1

        if topic_score > 0:

            matched_topics.append(topic)

            score += topic_score * 10

    if score > 0:

        matches.append({
            "score": score,
            "topics": matched_topics,
            "article": article
        })

# ------------------------
# SORT ARTICLES
# ------------------------

matches.sort(
    key=lambda x: x["score"],
    reverse=True
)

# ------------------------
# NO ARTICLES FOUND
# ------------------------

if not matches:

    send_message(
        "No sociology-related article found today."
    )

    raise SystemExit()

# ------------------------
# BEST ARTICLE
# ------------------------

best = matches[0]

article = best["article"]

print("Selected Article:")
print(article["title"])

# ------------------------
# GEMINI ANALYSIS
# ------------------------

prompt = SOCIOLOGY_PROMPT.format(
    title=article["title"],
    summary=article["summary"]
)

analysis = analyze_article(prompt)

# ------------------------
# TELEGRAM MESSAGE
# ------------------------

message = f"""
{analysis}

🔗 Source:
{article['link']}
"""

send_message(message)

print("Telegram post sent.")
