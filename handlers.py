# handlers.py
import re
import os
import requests
from nltk.stem import PorterStemmer

# 初始化詞幹提取器
stemmer = PorterStemmer()

# 定義關鍵字
KEYWORDS = {
    'on': ['on', 'activate', 'enable'],
    'off': ['off', 'deactivate', 'disable'],
    'turn': ['turn', 'switch'],
    'light': ['light', 'lights', 'lamp']
}

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def classify_command(message_text):
    """根據關鍵字和上下文分類指令。"""
    # 預處理訊息：小寫、詞幹提取和分詞
    message_text = message_text.lower()
    tokens = re.findall(r'\w+', message_text)  # 提取單詞
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # 檢查詞幹是否在關鍵字中
    has_turn = any(stem in KEYWORDS['turn'] for stem in stemmed_tokens)
    has_on = any(stem in KEYWORDS['on'] for stem in stemmed_tokens)
    has_off = any(stem in KEYWORDS['off'] for stem in stemmed_tokens)
    has_light = any(stem in KEYWORDS['light'] for stem in stemmed_tokens)

    # 根據檢測到的關鍵字確定操作
    if has_turn and has_light:
        if has_on:
            return "turn on the light"
        elif has_off:
            return "turn off the light"

    # 如果意圖不明確，返回預設值
    return "other"

def send_message(chat_id, text):
    """透過 Telegram API 發送訊息"""
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    requests.post(url, json=payload)
