from sqlalchemy import select
from sqlalchemy.orm import Session
from engine_creation import engine
from declare import User, Address

engine.echo = False

session = Session(bind=engine)

stmt = select(User)

for user in session.scalars(stmt):  # возвращает результаты как скаляры
    print(user.addresses)
