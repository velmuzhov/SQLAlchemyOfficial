"""
database metadata - обобщенное название питоновских объектов,
представляющих такие концепты баз данных, как таблицы и колонки.

Объекты MetaData, Table, Column

Объект MetaData - надстройка над питоновским словарем, который хранит
объекты Table и строки с их именами

Использование декларативных форм ORM для определения табличных метаданых
"""

from sqlalchemy import ForeignKey, MetaData, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional


URL = URL = "sqlite+pysqlite:///db.db"

engine = create_engine(URL, echo=True)

metadata_obj = MetaData()


class Base(
    DeclarativeBase
):  # коллекция Metadata в таком случае создается автоматически
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}), name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}), email_address={self.email_address!r}"

Base.metadata.create_all(engine)
