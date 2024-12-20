# routes.py
from flask import Blueprint, request
from handlers import classify_command, send_message

webhook_route = Blueprint('webhook_route', __name__)

@webhook_route.route('/webhook', methods=['POST'])
def webhook():
    """處理 Telegram 傳入的訊息"""
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # 使用 classify_command 分類訊息
        command = classify_command(text)

        # 根據分類結果回應用戶
        if command == "turn on the light":
            send_message(chat_id, "Turning on the light!")
        elif command == "turn off the light":
            send_message(chat_id, "Turning off the light~")
        else:
            send_message(chat_id, "Sorry, I don't understand that message.")

    return {"ok": True}