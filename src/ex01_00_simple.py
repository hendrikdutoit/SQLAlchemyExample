from os import environ
from sqlalchemy import Column, Integer, String, Identity
import db_connection


Base = db_connection.Base
engine = db_connection.engine
session = db_connection.session


class Person(Base):
    __tablename__ = 'person'
    __table_args__ = {'schema': environ.get("MYSQL_DB_NAME")}

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(45))
    pass

    def __repr__(self):
        return f"<Person(id={self.id} name={self.name})>"

    def __str__(self):
        return f"{self.name}"
