from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.application import AppState
from keyboards.inline import service_kb
from keyboards.reply import kb_phone
from utils.validators import check_name
from utils.validators import parse_phone, validate_phone

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


@rt_app.message(
    AppState.entering_phone
)
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
        await message.answer("Длина номера должна быть 10-15 символов!")
        return

    await state.update_data(phone=phone)
    await message.answer("Номер сохранен")

    await state.set_state(AppState.confirming)
