from sqlalchemy import update
from decl import user_table, address_table, engine

stmt = (
    update(user_table)
    .where(user_table.c.name == "leo")
    .values(fullname="Leopold Bloom from Dublin")
)

print(stmt)

with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()


