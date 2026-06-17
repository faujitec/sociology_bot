import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL")


def send_message(text):

    url = (
        f"https://api.telegram.org"
        f"/bot{BOT_TOKEN}/sendMessage"
    )

    # Telegram limit is 4096 characters
    # Keeping a small buffer
    text = text[:4000]

    try:

        response = requests.post(
            url,
            data={
                "chat_id": CHANNEL,
                "text": text,
                "disable_web_page_preview": False
            },
            timeout=30
        )

        print("Telegram Response:")
        print(response.text)

        response.raise_for_status()

    except Exception as e:

        print("Telegram Error:")
        print(str(e))
