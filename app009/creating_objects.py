from sqlalchemy.orm import Session
from engine_creation import engine
from declare import User, Address

with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )

    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )

    patrick = User(
        name="patrick",
        fullname="Patrick Star",
    )

    session.add_all([spongebob, sandy, patrick])

    session.commit()
