from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

service_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Разработка Telegram-бота", callback_data="telegram_bot"),
            InlineKeyboardButton(text="Разработка сайта", callback_data="website")
        ],
        [
            InlineKeyboardButton(text="Доработка Python-проекта", callback_data="rework_python"),
            InlineKeyboardButton(text="Другое", callback_data="other")
        ]
    ]
)

confirm_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подтвердить", callback_data="confirm"),
            InlineKeyboardButton(text="Отменить", callback_data="cancel")
        ],
    ]
)

