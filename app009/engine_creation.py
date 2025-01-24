from sqlalchemy import create_engine

URL = "sqlite+pysqlite:///quickstart.db"

engine = create_engine(url=URL, echo=True)
