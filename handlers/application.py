from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.application import AppState

rt_app = Router()


@rt_app.message(F.text == "Оставить заявку")
async def start_creating_app(message: Message, state: FSMContext):
    await message.answer("Введите вид услуги")

    await state.set_state(AppState.choosing_service)
