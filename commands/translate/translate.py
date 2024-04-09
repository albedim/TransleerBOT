import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes
from labels.labels import unspecified_language_error_message, not_replying_error_message, general_error_message

load_dotenv()


async def translateCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_html(not_replying_error_message())
        return

    args = update.message.text.split(" ")[1:]
    if len(args) != 1:
        await update.message.reply_html(unspecified_language_error_message())
        return
    res = requests.post("http://localhost:5000/translate", json={
        'text': update.message.reply_to_message.text,
        'language': args[0],
        'api_key': os.getenv('API_KEY')
    }).json()

    if res['success']:
        await update.message.reply_html(res['res'])
        return
    await update.message.reply_html(general_error_message(res['error']))
