import requests

BOT_TOKEN = "8876106077:AAFP4Hbi5tC2UBuU4VxK2rUR6SyLdrVP_Ds"
CHANNEL = "@sociologywithshekhar"

message = """
📚 Sociology Daily Insight

Topic: Urbanization

Thinkers:
• Durkheim
• Louis Wirth

UPSC Relevance:
Paper 1 + Paper 2
"""

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHANNEL,
        "text": message
    }
)
