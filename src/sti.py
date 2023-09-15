"""
Single Table Inheritance
========================
In this inheritance mechanism, multiple subclasses (entities) share a single database table. Each row in the table
includes a special discriminator column that indicates which subclass it belongs to.
"""
from os import environ
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists, drop_database

url = engine.URL.create(
    'mysql+mysqlconnector',
    username='root',
    password=environ.get('MYSQL_ROOT_PWD'),
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


class LogIn(Base):
    __tablename__ = 'login'
    __table_args__ = {'schema': environ.get('MYSQL_DATABASE')}

    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    type = Column(String(20))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'login',
    }
    pass

    def __repr__(self):
        return f'<LogIn(id={self.id} email={self.email})>'

    def __str__(self):
        return f'{self.email}'


class Student(LogIn):
    name = Column(String(45))
    surname = Column(String(45))
    __mapper_args__ = {
        'polymorphic_identity': 'Student',
    }

    def __repr__(self):
        return f'<Student(id={self.id} name={self.name} surname = {self.surname} email={self.email})>'

    def __str__(self):
        return f'{self.name} {self.surname}'
