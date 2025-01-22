from sqlalchemy.orm import Session
from db import User, Address, engine

session = Session(bind=engine)

s = session.get(User, 1)

print(s.addresses[1].email_address)

# Collections and related attributes in the SQLAlchemy ORM
# are persistent in memory; once the collection or attribute
# is populated, SQL is no longer emitted until that collection
# or attribute is expired.

print(s.addresses[0].id)
