from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оставить заявку"),
            KeyboardButton(text="О боте")
        ]
    ],
    resize_keyboard=True
)
