from os import environ
from sqlalchemy import Column, Integer, String, Identity
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
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


class Student(Base):
    __tablename__ = 'Student'
    __table_args__ = {'schema': environ.get("MYSQL_DB_NAME")}

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(45))
    pass

    def __repr__(self):
        return f"<Student(id={self.id} name={self.name})>"

    def __str__(self):
        return f"{self.name}"
