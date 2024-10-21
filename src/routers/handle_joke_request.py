import logging

from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from src.methods import get_joke

router = Router()


@router.inline_query()
async def show_user_links(inline_query: InlineQuery):
    logging.debug("Got inline query")

    variants = [
        InlineQueryResultArticle(
            id="get_joke",
            title="Несмешная шутка",
            description="Получить несмешную шутку",
            input_message_content=InputTextMessageContent(message_text=get_joke()),
            thumbnail_url="https://clwn.su/fs/clowns%20prod%20new%20tp.png",
        )
    ]

    await inline_query.answer(variants, cache_time=3, is_personal=True)
