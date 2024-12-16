"""
to access the last messages receved by the bot:
https://api.telegram.org/bot<TOKEN>/getUpdates

for additional information:
https://core.telegram.org/bots/api
"""

import os
import requests
from dotenv import load_dotenv


load_dotenv()


def send_telegram_message(chat_id, message):
    token = os.getenv("TG_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)
