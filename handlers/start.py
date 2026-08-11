from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

rt_start = Router()


@rt_start.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello!")
