from sqlalchemy import select
from decl import user_table, address_table, engine

# stmt = select(user_table).where(user_table.c.name == "spongebob")

# with engine.connect() as conn:
#     for row in conn.execute(stmt):
#         print(row)

print(select(user_table.c["name", "fullname"]))