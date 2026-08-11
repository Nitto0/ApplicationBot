from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.reply import kb_start

rt_start = Router()


@rt_start.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Hello!",
        reply_markup=kb_start
    )


@rt_start.message(F.text == "О боте")
async def about(message: Message):
    await message.answer("Бот для сбора заявок")
