import os
import json
import requests
from flask import Flask, request
from telegram import Bot

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

@app.route("/", methods=["GET"])
def index():
    return "Tesla Proxy Aktif!"

@app.route("/notify", methods=["POST"])
def notify():
    data = request.get_json()
    try:
        message = f"Yeni Araç Bulundu!\nModel: {data['model']}\nRenk: {data['color']}\nFiyat: {data['price']}"
        bot.send_message(chat_id=CHAT_ID, text=message)
        return "OK", 200
    except Exception as e:
        return str(e), 400

if __name__ == "__main__":
    app.run()