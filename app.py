from flask import Flask, request, jsonify
from telegram import Bot, Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_WEBHOOK_URL
from handlers.classifier import classify_command

app = Flask(__name__)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# 定義指令處理函數
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the bot!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    command = classify_command(user_message)
    if command == "turn on the light":
        await update.message.reply_text("Turning on the light!")
    elif command == "turn off the light":
        await update.message.reply_text("Turning off the light!")
    else:
        await update.message.reply_text("Command not recognized.")

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    if json_data is None:
        return jsonify({"error": "Invalid request"}), 400
    update = Update.de_json(json_data, bot)
    application.process_update(update)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    bot.set_webhook(url=TELEGRAM_WEBHOOK_URL)
    app.run(host="0.0.0.0", port=5000)
