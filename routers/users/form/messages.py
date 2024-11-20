from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from routers.users.form import models
from routers.users.form import keyboards
from aiogram.types import Message
from routers.users.form.replics import *
import db

router = Router()

@router.message(models.UserModel.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    markup = await keyboards.form_keyboard(state)
    await message.answer(replic_form, reply_markup=markup)
    await state.set_state(models.UserModel.form)

@router.message(models.UserModel.phone_number)
async def phone_num(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    markup = await keyboards.form_keyboard(state)
    await message.answer(replic_form, reply_markup=markup)
    await state.set_state(models.UserModel.form)

@router.message(models.UserModel.email)
async def email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    markup = await keyboards.form_keyboard(state)
    await message.answer(replic_form, reply_markup=markup)
    await state.set_state(models.UserModel.form)


@router.callback_query(models.UserModel.form, F.data == 'form.name')
async def form_name(call, state: FSMContext):
    await call.message.edit_text(text=replic_new_data)
    await state.set_state(models.UserModel.name)

@router.callback_query(models.UserModel.form, F.data == 'form.phone_number')
async def form_name(call, state: FSMContext):
    await call.message.edit_text(text=replic_new_data)
    await state.set_state(models.UserModel.phone_number)

@router.callback_query(models.UserModel.form, F.data == 'form.email')
async def form_name(call, state: FSMContext):
    await call.message.edit_text(text=replic_new_data)
    await state.set_state(models.UserModel.email)

@router.callback_query(models.UserModel.form, F.data == 'form.send')
async def form_name(call, state: FSMContext):
    await call.message.edit_text(text=replic_sended)
    data = await state.get_data()
    user_id = call.message.chat.id
    username = call.message.from_user.username
    first_name = call.message.from_user.first_name
    last_name = call.message.from_user.last_name
    name = data['name']
    phone_number = data['phone_number']
    email = data['email']
    await db.users.add_user(user_id, username, first_name, last_name, name, phone_number, email)

    text = await replic_user_data(call.message.chat.id)
    await call.message.answer(text)
