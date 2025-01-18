"""
Запросы через ORM-сессию.
Сессия - фундаментальный объект для взаимодействия с базовй данных при
использовании ORM. Внутри обращается к объекту Connection.
"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

URL = "sqlite+pysqlite:///my.db"

engine = create_engine(url=URL, echo=True)

stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")

with Session(engine) as session:
    result = session.execute(
        statement=text("UPDATE some_table SET y=:y WHERE x=:x"),
        params={"x": 6, "y": 12},
    )
    session.commit()

with Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for row in result:
        print(f"x: {row.x} y: {row.y}")
