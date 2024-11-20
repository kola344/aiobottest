class Users:
    def __init__(self):
        self.db = None

    async def connect(self, db):
        self.db = db

    async def create_table(self):
        await self.db.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER,
            username TEXT,
            first_name_tg TEXT,
            last_name_tg TEXT,
            name TEXT,
            phone_number TEXT,
            email TEXT
            )
            ''')
        await self.db.commit()

    async def add_user(self, user_id, username, first_name_tg, last_name_tg, name, phone_number, email):
        await self.db.execute('''INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)''', (user_id, username, first_name_tg, last_name_tg, name, phone_number, email))
        await self.db.commit()

    async def get_user(self, user_id):
        cursor = await self.db.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        data = await cursor.fetchone()
        return data
