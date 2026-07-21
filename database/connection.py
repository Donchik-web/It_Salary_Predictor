import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


def get_database_url():
    """Возвращает URL подключения к БД"""
    user = os.getenv("USER_DB")
    password = os.getenv("PASSWORD_DB")
    host = os.getenv("LOCALHOST_DB")
    port = os.getenv("PORT_DB")
    db_name = os.getenv("NAME_DB")

    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


engine = create_engine(get_database_url())
Session_DB = sessionmaker(bind=engine)


def get_db_session():
    """Возвращает сессию подключения"""
    db = Session_DB()
    try:
        yield db
    finally:
        db.close()
