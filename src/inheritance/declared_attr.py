"""
Single Table Inheritance
========================
In this inheritance mechanism, multiple subclasses (entities) share a single database table. Each row in the table
includes a special discriminator column that indicates which subclass it belongs to.
"""

from os import environ

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import relationship
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


class ProvidesUser:
    "A mixin that adds a 'user' relationship to classes."

    @declared_attr
    def user_id(self):
        return Column(ForeignKey('user_account.id'))

    @declared_attr
    def user(self):
        return relationship('User')

    def __repr__(self):
        return f'<LogIn(id={self.id} email={self.email})>'

    def __str__(self):
        return f'{self.email}'


class Employee(Base):
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @declared_attr
    def __mapper_args__(cls):
        if cls.__name__ == 'Employee':
            return {'polymorphic_on': cls.type, 'polymorphic_identity': 'Employee'}
        else:
            return {'polymorphic_identity': cls.__name__}

    def __repr__(self):
        return f'<Student(id={self.id} name={self.name} surname = {self.surname} email={self.email})>'

    def __str__(self):
        return f'{self.name} {self.surname}'
