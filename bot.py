import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.start import rt_start
from handlers.application import rt_app
from database.database import create_tables


async def main():
    bot = Bot(BOT_TOKEN)

    await create_tables()

    dp = Dispatcher()
    dp.include_routers(
        rt_start,
        rt_app
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
