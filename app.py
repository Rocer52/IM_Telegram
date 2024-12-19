from flask import Flask, request, jsonify
from telegram import Update, Bot
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_WEBHOOK_URL
from handlers.classifier import classify_command

app = Flask(__name__)

# 建立 Telegram Bot 和應用
bot = Bot(token=TELEGRAM_BOT_TOKEN)
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Telegram 命令處理
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """回應 /start 指令"""
    user = update.effective_user
    await update.message.reply_text(f"Hi {user.first_name}! Welcome to the bot.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """處理用戶訊息"""
    user_message = update.message.text
    command = classify_command(user_message)  # 使用自定義的命令分類函數
    if command == "turn on the light":
        await update.message.reply_text("Turning on the light!")
    elif command == "turn off the light":
        await update.message.reply_text("Turning off the light~")
    else:
        await update.message.reply_text("Sorry, I don't understand that message.")

# 註冊處理器
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Webhook 路由
@app.route('/webhook', methods=['POST'])
def telegram_webhook():
    """處理 Telegram 發送的 Webhook 更新"""
    json_data = request.get_json()
    if json_data is None:
        return jsonify({"error": "Invalid request"}), 400
    update = Update.de_json(json_data, bot)
    application.process_update(update)
    return jsonify({"status": "success"}), 200

# 測試 API（非 Telegram 專用）
@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({"status": "Bot is running"}), 200

if __name__ == '__main__':
    # 設置 Telegram Webhook
    bot.set_webhook(url=TELEGRAM_WEBHOOK_URL)
    # 啟動 Flask 應用
    app.run(host='0.0.0.0', port=5000)
