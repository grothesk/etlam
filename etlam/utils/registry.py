from sqlalchemy import Column, DateTime, Boolean, String, Integer, or_
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
Base.metadata.schema = 'public'


class FileRegistryModel(Base):
    __tablename__ = 'file_registry'

    file = Column(String, nullable=False, primary_key=True)
    version = Column(Integer, nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    completed = Column(Boolean, nullable=False)
    in_progress = Column(Boolean, nullable=False)

    @classmethod
    def create_table(cls, engine):
        cls.__table__.create(engine)

    @classmethod
    def drop_table(cls, engine):
        cls.__table__.drop(engine)