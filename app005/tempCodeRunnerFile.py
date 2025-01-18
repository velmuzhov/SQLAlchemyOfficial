subq = (
#     select(func.count(address_table.c.id).label("count"), address_table.c.user_id)
#     .group_by(address_table.c.user_id)
#     .subquery("aux")
# )

# print(subq.name)

# stmt = select(func.min(user_table.c.name))