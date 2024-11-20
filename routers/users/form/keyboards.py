from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext

async def form_keyboard(state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    phone_number = data.get('phone_number')
    email = data.get('email')

    keyboard = [
        [InlineKeyboardButton(text=name, callback_data=f'form.name')],
        [InlineKeyboardButton(text=phone_number, callback_data=f'form.phone_number')],
        [InlineKeyboardButton(text=email, callback_data=f'form.email')],
        [InlineKeyboardButton(text='Отправить', callback_data='form.send')]
    ]

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup