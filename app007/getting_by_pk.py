from sqlalchemy.orm import Session
from db import engine, User, Address

session = Session(bind=engine)

s = session.get(User, 1)

# Identity map - объект, хранящийся в памяти, который связывает загруженные
# в данный момент в память объекты с их первичными ключами. Метод get вернет
# объект из identity map, если он там представлен, в ином случае запустит SELECT.

print(s.name)

session.close()
