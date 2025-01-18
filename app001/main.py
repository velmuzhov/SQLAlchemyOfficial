"""
Начало любого приложения SqlAlchemy - объект Engine. Он работает как центральный источник соединений с
отдельной базой данных, удерживает connection pool (пул подключений). Как правило, это глобальный объект, созданный
один раз для конкретного сервера базы данных, конфигурируется с помощью строки URL.

Будучи впервые возвращенным из create_engine(), engine еще не пытается подключиться к базе данных. Он делает это, когда первый раз
получает указание выполнить задачу в БД - lazy initialization.
"""

from sqlalchemy import create_engine, text, CursorResult

URL = "sqlite+pysqlite:///my.db"

engine = create_engine(url=URL, echo=True)
# echo=True будет логировать в стандартный вывод

with engine.connect() as conn:
    result: CursorResult = conn.execute(text("select 'hello world'")) # объект Result. Его лучше не использовать вне этого блока соединения
    print(result.all())

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table(x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [
            {"x": 1, "y": 1},
            {"x": 2, "y": 4},
        ],
    )
    conn.commit()  # стиль "commit as you go"

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM some_table WHERE x=2"))
    print(result.all())

# стиль "begin once" с использованием Engine.begin(),
# создается блок транзакции, которая вся завершается COMMIT или ROLLBACK
# более предпочтительный стиль
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [
            {"x": 6, "y": 8},
            {"x": 9, "y": 10}, # стиль "executemany", не поддерживает возврат result rows
        ],
    )

with engine.connect() as conn:
    result = conn.execute(statement=text("Select x, y from some_table;"))
    for row in result:
        print(row.x, row.y)
    print()

with engine.connect() as conn:
    result = conn.execute(
        statement=text("SELECT x, y FROM some_table WHERE y > :y;"),
        parameters={"y": 2}, # делать с параметрами, а не другими манипуляциями со строками, т.к. помогает избегать инъекций
    )
    for x, y in result:
        print(x, y)
