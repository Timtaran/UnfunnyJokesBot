import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src import config, routers

logging.basicConfig(level=logging.DEBUG)


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(*routers)

    bot = Bot(
        token=config.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
