import os
import telebot
from flask import Flask, request

TOKEN = "5538200311:AAG6nurEgpXRLW_2BWhd2Ufe6_SFwqla-2Y"
APP_URL = f"https://github-to-telegram-jjz.herokuapp.com/{TOKEN}"
bot = telebot.TeleBot{TOKEN}
server = Flask(__name__)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello, " + message.from_user.first.name)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def echo(message):
    bot.reply_to(message, message.text)

@server.route("/" + TOKEN, methods=["POST"])
def get_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(so.environ.get("PORT", 5000)))