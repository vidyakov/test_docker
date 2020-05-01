from gino import Gino
from sqlalchemy import Column, Integer, BigInteger, String
import asyncio

from config import DB_PASS, DB_USER, HOST


db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    language = Column(String(2))
    full_name = Column(String(100))
    username = Column(String(50))

    def __repr__(self):
        return "<User(id='{}', fullname='{}', username='{}')>".format(
            self.id, self.full_name, self.username)


async def create_db():
    await db.set_bind(f'postgresql://{DB_USER}:{DB_PASS}@{HOST}/gino')
    await db.gino.drop_all()
    await db.gino.create_all()
    await db.pop_bind().close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(create_db())
