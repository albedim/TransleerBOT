from telegram import Update
from telegram.ext import ContextTypes
from labels.labels import help_message


async def helpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(help_message())