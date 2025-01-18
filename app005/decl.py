"""
database metadata - обобщенное название питоновских объектов,
представляющих такие концепты баз данных, как таблицы и колонки.

Объекты MetaData, Table, Column

Объект MetaData - надстройка над питоновским словарем, который хранит
объекты Table и строки с их именами
"""

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    create_engine,
)

URL = "sqlite+pysqlite:///md.db"

engine = create_engine(url=URL, echo=True)

metadata_obj = MetaData()

user_table = Table(  # схоже с выражением CREATE TABLE
    "user_account",
    metadata_obj,  # таблица user_table присваивает себя коллекции metadata_obj
    Column(
        "id", Integer, primary_key=True
    ),  # коллекция с колонками находится в ассоциативном массиве Table.c
    Column("name", String(30)),
    Column("fullname", String),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

metadata_obj.create_all(engine)
