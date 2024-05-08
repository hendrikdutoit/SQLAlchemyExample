"""
Composing Mapped Hierarchies with Mixins
========================================

"""

from os import environ

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.orm import declared_attr
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


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)


@declarative_mixin
class ReferenceAddressMixin:
    @declared_attr
    def address_id(cls):
        return Column(Integer, ForeignKey("address.id"))


class User(ReferenceAddressMixin, Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f'<User(id={self.id} address_id={self.address_id})>'

    def __str__(self):
        return f'{self.id},{self.address_id}'
