from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.application import AppState
from keyboards.inline import service_kb, confirm_kb
from keyboards.reply import kb_phone, kb_start
from utils.validators import parse_phone, validate_phone, check_name
from data.services import services
from config import ADMIN_ID

rt_app = Router()


@rt_app.message(F.text == "Оставить заявку")
async def start_creating_app(message: Message, state: FSMContext):
    await message.answer("Введите вид услуги", reply_markup=service_kb)

    await state.set_state(AppState.choosing_service)


@rt_app.callback_query(
    AppState.choosing_service,
    F.data.in_({"telegram_bot", "website", "rework_python", "other"})
)
async def choosing_service_handler(callback: CallbackQuery, state: FSMContext):
    await state.update_data(service=callback.data)

    await callback.answer()
    await callback.message.answer('Введите свое имя')

    await state.set_state(AppState.entering_name)


@rt_app.message(
    AppState.entering_name,
    F.text
)
async def entering_name_handler(message: Message, state: FSMContext):
    if not message.text:
        await message.answer("Введите имя!")
        return

    name = message.text.strip()
    if not check_name(name):
        await message.answer("Имя должно быть от 2 символов, и оно не должно состоять только из цифр")
        return

    await state.update_data(name=name)
    await message.answer("Теперь введите свой номер телефона",
                         reply_markup=kb_phone)

    await state.set_state(AppState.entering_phone)


@rt_app.message(AppState.entering_phone)
async def entering_phone_handler(message: Message, state: FSMContext):
    if not (message.contact or message.text):
        await message.answer("Введите телефон!", reply_markup=kb_phone)
        return

    phone = message.contact.phone_number if message.contact else (
        message.text.strip())

    phone = parse_phone(phone)

    if not phone:
        await message.answer("Некорректный номер телефона!", reply_markup=kb_phone)
        return

    if not validate_phone(phone):
        await message.answer("Длина номера должна быть 10-15 цифр!")
        return

    if message.contact and message.contact.user_id != message.from_user.id:
        await message.answer("Это не ваш номер!")
        return

    await state.update_data(phone=phone)

    items = await state.get_data()

    service = services.get(items.get("service"))
    name = items.get("name")

    await message.answer(f"Проверьте данные заявки:\n\n"
                         f"Услуга: {service}\n"
                         f"Имя: {name}\n"
                         f"Телефон: {phone}\n\n"
                         f"Отправить заявку?", reply_markup=confirm_kb)

    await state.set_state(AppState.confirming)


@rt_app.callback_query(
    AppState.confirming,
    F.data == "confirm"
)
async def confirming_handler(callback: CallbackQuery, state: FSMContext, bot: Bot):
    items = await state.get_data()

    name = items.get("name")
    service = services.get(items.get("service"))
    phone = items.get("phone")

    user_id = callback.from_user.id
    user_name = callback.from_user.username if callback.from_user.username \
        else "Отсутствует"

    await bot.send_message(ADMIN_ID,
                           f"Новая заявка\n\n"
                           f"Услуга: {service}\n"
                           f"Имя: {name}\n"
                           f"Телефон: {phone}\n\n"
                           f"Telegram ID: {user_id}"
                           f"Username: @{user_name}")

    await callback.answer()
    await callback.message.answer("Заявка подтверждена")
    await state.clear()


@rt_app.callback_query(
    AppState.confirming,
    F.data == "cancel"
)
async def cancel_handler(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.clear()
    await callback.message.answer("Заявка отменена", reply_markup=kb_start)
