from os import environ
from pathlib import Path

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# from beetools import beevenv, beescript
# import pytest

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
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base(bind=engine)
project_dir: Path = Path(environ.get("PROJECTS_BASE_DIR"), "BEE", "SQLAlchemyExample")
venv_base_dir: Path = Path(environ.get("VENV_BASE_DIR"))
