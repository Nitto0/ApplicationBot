import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.start import rt_start
from handlers.application import rt_app


async def main():
    bot = Bot(BOT_TOKEN)

    dp = Dispatcher()
    dp.include_routers(
        rt_start,
        rt_app
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
