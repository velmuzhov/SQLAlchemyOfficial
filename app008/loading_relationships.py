from sqlalchemy import select
from sqlalchemy.orm import Session
from db import User, Address, engine


session = Session(bind=engine)

print(select(Address.email_address).select_from(User).join(User.addresses))
print()
print(select(Address.email_address).join_from(User, Address))