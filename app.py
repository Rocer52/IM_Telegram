import os
from flask import Flask, request
import requests

app = Flask(__name__)

# 讀取 Telegram Bot Token（從環境變數中取得）
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


@app.route('/webhook', methods=['POST'])
def webhook():
    """處理 Telegram 傳入的訊息"""
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # 回應用戶的訊息
        if text:
            send_message(chat_id, f"You said: {text}")
    
    return {"ok": True}


def send_message(chat_id, text):
    """透過 Telegram API 發送訊息"""
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    requests.post(url, json=payload)


if __name__ == "__main__":
    # 啟動 Flask 伺服器
    app.run(host="0.0.0.0", port=5000)
