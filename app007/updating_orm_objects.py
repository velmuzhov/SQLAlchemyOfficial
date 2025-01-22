from sqlalchemy import select
from sqlalchemy.orm import Session
from db import engine, User, Address

session = Session(bind=engine)

s = session.execute(select(User).filter_by(name="ehkrabs")).scalar_one()

print(s)

s.fullname = "Eugene H. Krabs the Great"

print(s in session.dirty)  # True, объект помещается в эту коллекцию

s_fullname = session.execute(select(User.fullname).where(User.id == 2)).scalar_one()
print(s_fullname)

print(s in session.dirty)  # True, объект помещается в эту коллекцию

session.close()
