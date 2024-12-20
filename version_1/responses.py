from telegram.ext import MessageHandler, filters
from classifier import classify_command

async def handle_message(update, context):
    """根據訊息分類回應用戶。"""
    user_message = update.message.text
    command = classify_command(user_message)  # 使用 classify_command 進行分類

    # 根據分類結果進行回應
    if command == "turn on the light":
        await update.message.reply_text("Turning on the light!")
    elif command == "turn off the light":
        await update.message.reply_text("Turning off the light~")
    else:
        await update.message.reply_text("Sorry, I don't understand that message.")

# 傳回 MessageHandler 以供主程式使用
def get_message_handler():
    """取得用於處理文字訊息的 MessageHandler。"""
    return MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
