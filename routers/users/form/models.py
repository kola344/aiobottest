from aiogram.fsm.state import State, StatesGroup

class UserModel(StatesGroup):
    form = State()
    name = State()
    phone_number = State()
    email = State()
    nan = State()
