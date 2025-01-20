from sqlalchemy.orm import Session
from db import engine, User, Address

session = Session(bind=engine)

st = session.get(User, 1)

print(st)

session.delete(st) # объект помечен на удаление, до flush на самом деле
                   # ничего не происходит
