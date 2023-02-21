from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import os
import naifu

def start(update, context):
    update.message.reply_text('Hi!')

def receive_message(update, context):
    # receive the message
    message = update.message.text
    if message.startswith("draw:"):
        prompt = message.split("draw:")[1]
        update.message.reply_text('Drawing...')
        img = naifu.generate(prompt)
        if img is not None:
            update.message.reply_photo(img)
        else:
            update.message.reply_text('Error! Try again please.')

updater = Updater('') # Telegram bot ID

start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)

receive_message_handler = MessageHandler(Filters.text, receive_message)
updater.dispatcher.add_handler(receive_message_handler)

updater.start_polling()
