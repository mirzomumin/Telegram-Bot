#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.utils.helpers import escape_markdown

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

from .models import Post


def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    posts = Post.objects.filter(title__icontains=query)

    if query == "":
        return

    results = [
        InlineQueryResultArticle(
            id=post.id,
            title=post.title,
            url=post.image,
            thumb_url=post.image,
            thumb_height=5,
            thumb_width=5, 
            description=post.text,
            input_message_content=InputTextMessageContent(
                message_text=f'{post.title}\n \n{post.text}',
                parse_mode=None
            ),
        ) for post in posts]

    update.inline_query.answer(results)