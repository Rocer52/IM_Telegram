from telegram.ext import Application
from responses import get_message_handler

def main():
    """啟動 Telegram 機器人。"""
    # 替換為您的機器人 Token
    TOKEN = "7512146056:AAGHv1fbjAGI2crp8omo4j3WSbzKckso_ko"

    # 建立 Telegram 應用
    application = Application.builder().token(TOKEN).build()

    # 註冊訊息處理器
    application.add_handler(get_message_handler())

    # 啟動機器人
    application.run_polling()

if __name__ == "__main__":
    main()
