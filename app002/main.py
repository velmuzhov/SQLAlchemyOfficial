"""
Работа с метаданными базы данных.

Database metadata - питоновские объекты, которые представляют такие концепты
базы данных, как таблицы и колонки.

Наиболее фундаментальные из таких объектов - Metadata, Table и Column.
"""

from sqlalchemy import MetaData, ForeignKey, create_engine
from sqlalchemy import Table, Column, Integer, String

URL = "sqlite+pysqlite:///:memory:"

engine = create_engine(URL, echo=True)

metadata_obj = MetaData()

# Если не использовать декларативные модели ORM, каждый объект Table
# создается напрямую, обычно через присваивание переменным
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True), # без указания специфики можно передать сам класс, не инстанциируя
    Column("name", String(30)),
    Column("fullname", String()),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False), # можно опустить тип данных, будет задан автоматически
    Column("email_address", String, nullable=False)
)

# print(user_table.c) # доступ к коллекции клонок таблицы
# print(address_table.c)

