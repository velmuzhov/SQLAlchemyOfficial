from sqlalchemy.orm import Session
from db import User, Address, engine

u1 = User(
    name="pkrabs",
    fullname="Pearl Krabs",
)

# print(u1.addresses)

a1 = Address(
    email_address="pearl.krabs@gmail.com",
)

u1.addresses.append(a1)

# print(u1.addresses)

# print(a1.user.fullname)

u2 = Address(
    email_address="pearl@aol.com",
    user=u1,
)

# print(u1.addresses)

session = Session(bind=engine)

session.add(u1)  # a1 и a2 тоже автоматически добавляются в сессию (save-update cascade)

session.commit()
session.close()
