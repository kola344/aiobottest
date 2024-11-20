import db

replic_new_data = 'Введите новые данные'
replic_form = 'Форма'
replic_sended = 'Отправлено'

async def replic_user_data(user_id):
    data = await db.users.get_user(user_id)
    return f'Ваши данные:\n{data}'