import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_DB_DRIVER = os.getenv('DB_DRIVER', 'postgresql')
_DB_HOST = os.getenv('DB_HOST', 'localhost')
_DB_PORT = os.getenv('DB_PORT', 5432)
_DB_USERNAME = os.getenv('DB_USERNAME')
_DB_PASSWORD = os.getenv('DB_PASSWORD')
_DB_DATABASE = os.getenv('DB_DATABASE')

DATABASE_URI = '{driver}://{user}:{password}@{host}:{port}/{database}'.format(
    driver=_DB_DRIVER,
    user=_DB_USERNAME,
    password=_DB_PASSWORD,
    host=_DB_HOST,
    port=_DB_PORT,
    database=_DB_DATABASE
)


def start_session():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker()
    Session.configure(bind=engine)
    return Session()