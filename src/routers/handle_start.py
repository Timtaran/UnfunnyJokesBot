from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        "Привет. Упомяни меня в любом чате чтобы отправить друзьям несмешной анекдот.\n\nПроебать свои деньги: https://www.donationalerts.com/r/timtaran"
    )
