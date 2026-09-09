from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.application import AppState
from keyboards.inline import service_kb

rt_app = Router()


@rt_app.message(F.text == "Оставить заявку")
async def start_creating_app(message: Message, state: FSMContext):
    await message.answer("Введите вид услуги", reply_markup=service_kb)

    await state.set_state(AppState.choosing_service)


@rt_app.callback_query(
    AppState.choosing_service,
    F.data.in_({"telegram_bot", "website", "rework_python", "other"})
)
async def telegram_bot(callback: CallbackQuery, state: FSMContext):
    await state.update_data(service=callback.data)

    await callback.message.answer('Введите свое имя')

    await state.set_state(AppState.entering_name)
