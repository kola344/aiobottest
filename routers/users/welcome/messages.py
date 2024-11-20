from aiogram import Router, F
from aiogram.types import Message
from routers.users.welcome import keyboards
from routers.users.welcome.replics import *
from aiogram.fsm.context import FSMContext

from routers.users.form import models
from routers.users.form.keyboards import form_keyboard

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer(replic_welcome, reply_markup=keyboards.main_keyboard)

@router.message(F.text == 'Заполнить форму')
async def form(message: Message, state: FSMContext):
    await state.update_data(name="ФИО")
    await state.update_data(phone_number="Номер телефона")
    await state.update_data(email="Email")
    markup = await form_keyboard(state)
    await message.answer(replic_form, reply_markup=markup)
    await state.set_state(models.UserModel.form)
