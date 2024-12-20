# app.py
from flask import Flask
from routes import webhook_route

app = Flask(__name__)

# 將路由註冊到 Flask 應用
app.register_blueprint(webhook_route)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)