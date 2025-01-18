from app005.decl import user_table, address_table, engine
from sqlalchemy import insert

stmt = insert(user_table).values(
    name="spongebob",
    fullname="Spongebob Squarepantd",
)

print(stmt)

with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()

