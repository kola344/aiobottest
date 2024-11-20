from database import db
import aiosqlite

users = db.Users()
async def init():
    database = await aiosqlite.connect('database/db.db')

    await users.connect(database)
    await users.create_table()

