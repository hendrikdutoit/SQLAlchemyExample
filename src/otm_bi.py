"""
SQLAlchemy V1.4.x
Example: One-to_Many bi-directional

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


class Author(Base):
    __tablename__ = 'author'
    __table_args__ = {'schema': environ.get("MYSQL_DB_NAME")}

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    surname = Column(String(45))

    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"<Author(id={self.id} name={self.name} surname={self.surname})>"

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(Base):
    __tablename__ = 'book'
    __table_args__ = {'schema': environ.get("MYSQL_DB_NAME")}

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    author_id = Column(Integer, ForeignKey(f"{environ.get('MYSQL_DB_NAME')}.author.id"))

    author = relationship("Author", back_populates="books")
    pass

    def __repr__(self):
        return f"<Book(id={self.id} name={self.name})>"

    def __str__(self):
        return f"{self.name}"
