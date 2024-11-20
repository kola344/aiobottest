import asyncio

from bot_init import bot
from aiogram import Dispatcher

import db

from routers.users.form.messages import router as form_router
from routers.users.welcome.messages import router as welcome_router

dp = Dispatcher()
dp.include_router(form_router)
dp.include_router(welcome_router)

async def main():
    await db.init()
    await dp.start_polling(bot)

asyncio.run(main())