import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL")


def send_message(text):

    url = (
        f"https://api.telegram.org"
        f"/bot{BOT_TOKEN}/sendMessage"
    )

    requests.post(
        url,
        data={
            "chat_id": CHANNEL,
            "text": text
        },
        timeout=30
    )
