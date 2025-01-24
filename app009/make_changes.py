from sqlalchemy import select
from sqlalchemy.orm import Session
from engine_creation import engine
from declare import User, Address

engine.echo = False

session = Session(bind=engine)

stmt = select(User).where(User.name == "patrick")
patrick = session.scalars(stmt).one()

patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))

stmt1 = (
    select(Address)
    .join(Address.user)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy@sqlalchemy.org")
)

sandy_address = session.scalars(stmt).one()

sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"

session.commit()
session.close()