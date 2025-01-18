from sqlalchemy import select, func
from decl import user_table, address_table, engine

# stmt = select(user_table).where(user_table.c.name == "spongebob")

# with engine.connect() as conn:
#     for row in conn.execute(stmt):
#         print(row)

# print(select(user_table.c["name", "fullname"]))

# stmt = select(user_table).where(user_table.c.name == "spongebob")

# with engine.connect() as conn:
#     for row in conn.execute(stmt):
#         print(row)

# stmt = select(user_table.c.name, address_table.c.email_address).join_from(
#     user_table, address_table
# )

# with engine.connect() as conn:
#     for row in conn.execute(stmt):
#         print(row)

# subq = (
#     select(func.count(address_table.c.id).label("count"), address_table.c.user_id)
#     .group_by(address_table.c.user_id)
#     .subquery("aux")
# )

# print(subq.name)

stmt = select(user_table)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)
