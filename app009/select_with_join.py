from sqlalchemy import select
from sqlalchemy.orm import Session
from engine_creation import engine
from declare import User, Address

engine.echo = False


stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy@sqlalchemy.org")
)

with Session(bind=engine) as session:
    sandy_address = session.scalars(stmt).one()
    print(sandy_address)
