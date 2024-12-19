# config.py 
# **please set up Environment variable in your deployment**
import os

# If it's not set, you can set a default value or handle the error
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7512146056:AAGHv1fbjAGI2crp8omo4j3WSbzKckso_ko")

TELEGRAM_WEBHOOK_URL = os.getenv("TELEGRAM_WEBHOOK_URL", "https://im-microservice.onrender.com")

print(f"Using Access Token: {TELEGRAM_BOT_TOKEN}")
# You can add additional configuration settings here if needed