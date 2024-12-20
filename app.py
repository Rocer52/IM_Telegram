import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from responses import get_message_handler

app = Flask(__name__)

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_WEBHOOK_URL = os.getenv("TELEGRAM_WEBHOOK_URL")  # Render 部署後的完整 Webhook URL

# 初始化 Telegram Bot Application
application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

# 設定訊息處理器
application.add_handler(get_message_handler())

@app.route('/webhook', methods=['POST'])
def webhook():
    """接收 Telegram Webhook 的更新"""
    data = request.get_json()
    update = Update.de_json(data, application.bot)
    application.process_update(update)
    return {"ok": True}

if __name__ == "__main__":
    # 設定 Webhook
    application.bot.set_webhook(TELEGRAM_WEBHOOK_URL)
    app.run(host="0.0.0.0", port=5000)
