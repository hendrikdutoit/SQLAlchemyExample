"""
SQLAlchemy V1.4.46
Example: One-to_Many Uni-directional

https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
"""
from os import environ
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists, drop_database

url = engine.URL.create(
    "mysql+mysqlconnector",
    username="root",
    password=environ.get("MYSQL_ROOT_PWD"),
    host=environ.get("MYSQL_HOST"),
    port=environ.get("MYSQL_TCP_PORT_EXAMPLES"),
    database=environ.get("MYSQL_DB_NAME"),
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
    __table_args__ = {'schema': environ.get("MYSQL_DB_NAME")}

    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    type = Column(String(20))

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "login",
    }
    pass

    def __repr__(self):
        return f"<LogIn(id={self.id} name={self.email})>"

    def __str__(self):
        return f"{self.email}"


class Child(Base):
    __tablename__ = 'child'
    __table_args__ = {'schema': environ.get("MYSQL_DB_NAME")}

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    type = Column(String(20))

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "child",
    }
    pass

    def __repr__(self):
        return f"<Child(id={self.id} name={self.name})>"

    def __str__(self):
        return f"{self.name}"


class Person(LogIn):
    __mapper_args__ = {
        "polymorphic_identity": "parent_sti",
    }
    children = relationship("Person")

    def __repr__(self):
        return f"<Person(id={self.id} name={self.email})>"


class ChildSTI(Child):
    parent_id = Column(Integer, ForeignKey(f"{environ.get('MYSQL_DB_NAME')}.parent.id"))
    __mapper_args__ = {
        "polymorphic_identity": "child_sti",
    }

    def __repr__(self):
        return f"<ChildSTI(id={self.id} name={self.name} parent_id={self.parent_id})>"
