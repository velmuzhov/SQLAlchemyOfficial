"""
Использование Annotated для определения своего типа полей с дополнительными
метаданными, которые могут содержать объект mapped_column
"""

from typing import Annotated
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, Engine, String

URL: str = "sqlite+pysqlite:///annot.db"

engine: Engine = create_engine(url=URL, echo=True)


class MyFields:
    my_pk = Annotated[int, mapped_column(primary_key=True)]
    my_short_string = Annotated[str, mapped_column(String(30))]
    my_long_string = Annotated[str, 1000]


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "post"

    id: Mapped[MyFields.my_pk]
    author: Mapped[MyFields.my_short_string]
    content: Mapped[MyFields.my_long_string]


Base.metadata.create_all(bind=engine)
