import telegram.error
from telegram import Bot, BotCommand
from telegram.ext import (
    Updater, Dispatcher, Filters,
    CommandHandler, MessageHandler,
    CallbackQueryHandler,
    InlineQueryHandler,
    CallbackContext
)
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.utils.helpers import escape_markdown

from dtb.celery import app  # event processing in async mode
from dtb.settings import TELEGRAM_TOKEN, DEBUG
from .function import inlinequery





def start(update, context):
	username = update.message.from_user.first_name
	update.message.reply_html(f'Hello, {username}!\n\
        \nВведите: @логин_бота и через пробел какое либо сообщение.')



def run_pooling():
    """ Run bot in pooling mode """
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher
    # dp = setup_dispatcher(dp)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(InlineQueryHandler(inlinequery))

    bot_info = Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Pooling of '{bot_link}' started")
    # it is really useful to send '👋' emoji to developer
    # when you run local test
    # bot.send_message(text='👋', chat_id=<YOUR TELEGRAM ID>)

    updater.start_polling()
    updater.idle()
