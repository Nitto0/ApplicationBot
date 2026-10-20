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

kb_phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить номер телефона", request_contact=True)
        ]
    ],
    resize_keyboard=True
)
