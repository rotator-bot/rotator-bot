from telegram import Bot
import time
import os

TOKEN = os.environ["TOKEN"]
CHANNEL = os.environ["CHANNEL"]

bot = Bot(token=TOKEN)

messages = [
    "🔥 پیام اول",
    "💎 پیام دوم",
    "🚀 پیام سوم"
]

i = 0

while True:
    msg = bot.send_message(CHANNEL, messages[i % len(messages)])
    time.sleep(30)
    bot.delete_message(CHANNEL, msg.message_id)
    i += 1
