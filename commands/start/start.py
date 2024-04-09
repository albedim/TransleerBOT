from telegram import Update
from telegram.ext import ContextTypes
from labels.labels import start_message


async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(start_message(update.message.from_user.username))
