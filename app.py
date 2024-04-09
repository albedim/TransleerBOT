import os
from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler, MessageHandler, filters

from commands.translate.translate import translateCommand
from commands.start.start import startCommand
from commands.help.help import helpCommand
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("error", context.error)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', startCommand))
    app.add_handler(CommandHandler('help', helpCommand))
    app.add_handler(CommandHandler('tr', translateCommand))
    app.add_handler(CommandHandler('translate', translateCommand))

    # app.add_handler(MessageHandler(filters.TEXT, handleRequest))
    app.add_error_handler(error)

    print("[BOT] - status: running")
    app.run_polling(poll_interval=3)


main()
