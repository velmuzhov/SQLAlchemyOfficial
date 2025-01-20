from sqlalchemy.orm import Session, sessionmaker
from db import User, Address, engine

# session: Session = sessionmaker(bind=engine)
session = Session(bind=engine)

# Экземпляры классов представляют строки таблицы

squidward = User(
    name="squidward",
    fullname="Squidward Tentacles",
)

krabs = User(
    name="ehkrabs",
    fullname="Eugene H. Krabs",
)

print(krabs)

session.add(squidward)
session.add(krabs)

print(session.new)  # просмотр ожидающих объектов, которые еще на добавлены в БД

# Сессия использует паттерн unit of work - аккумулирует изменения по одному за раз, но
# не сообщает о них в БД, пока не возникнет необходимость. Это позволяет принять
# лучшее решение о том, как именно SQL DML должен быть запущен в транзакции.
# flush - процесс отправки SQL в БД, чтобы запушить текущий набор изменений.

session.flush()
session.commit() # объекты все еще останутся привязанными к сессии, пока она не закрыта
session.close()
