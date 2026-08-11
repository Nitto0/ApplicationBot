from aiogram.fsm.state import StatesGroup, State


class AppState(StatesGroup):
    choosing_service = State()
    entering_name = State()
    entering_phone = State()
    confirming = State()
