"""
Composing Mapped Hierarchies with Mixins
========================================

"""

from datetime import datetime
from os import environ

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_mixin
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


@declarative_mixin
class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now())


class MyModel(TimestampMixin, Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)
    name = Column(String(1000))

    def __repr__(self):
        return f'<MyModel(id={self.id} name={self.name} created_at={self.created_at})>'

    def __str__(self):
        return f'{self.id},{self.name},{self.created_at}'
