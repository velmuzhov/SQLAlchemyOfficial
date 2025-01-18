stmt = select(user_table).where(user_table.c.name == "spongebob")

# with engine.connect() as conn:
#     for row in conn.execute(stmt):
#         print(row)