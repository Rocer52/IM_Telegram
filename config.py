# config.py 
# **please set up Environment variable in your deployment**
import os

# If it's not set, you can set a default value or handle the error
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'default')

print(f"Using Access Token: {TELEGRAM_BOT_TOKEN}")
# You can add additional configuration settings here if needed