"""
Simple Example
==============

"""
from os import environ

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy import Identity
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import drop_database

url = engine.URL.create(
    'mysql+mysqlconnector',
    username='root',
    password=environ.get('MYSQL_ROOT_PASSWORD'),
    host=environ.get('MYSQL_HOST'),
    port=environ.get('MYSQL_TCP_PORT'),
    database=environ.get('MYSQL_DATABASE'),
)
# url = 'sqlite:///:memory:'
engine = create_engine(url, echo=False)
if database_exists(engine.url):
    drop_database(engine.url)
create_database(engine.url)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base(bind=engine)


class Student(Base):
    __tablename__ = 'Student'
    __table_args__ = {'schema': environ.get('MYSQL_DATABASE')}

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(45))
    pass

    def __repr__(self):
        return f'<Student(id={self.id} name={self.name})>'

    def __str__(self):
        return f'{self.name}'
