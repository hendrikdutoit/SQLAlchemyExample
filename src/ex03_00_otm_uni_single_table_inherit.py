"""
SQLAlchemy V1.4.46
Example: One-to_Many Uni-directional

https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
"""
from os import environ
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
import db_connection as dbc


Base = dbc.Base
engine = dbc.engine
session = dbc.session


class Parent(Base):
    __tablename__ = 'parent'
    __table_args__ = {'schema': environ.get("MYSQL_DB_NAME")}

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    type = Column(String(20))

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "parent",
    }
    pass

    def __repr__(self):
        return f"<Parent(id={self.id} name={self.name})>"

    def __str__(self):
        return f"{self.name}"


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


class ParentSTI(Parent):
    __mapper_args__ = {
        "polymorphic_identity": "parent_sti",
    }
    children = relationship("ChildSTI")

    def __repr__(self):
        return f"<ParentSTI(id={self.id} name={self.name})>"


class ChildSTI(Child):
    parent_id = Column(Integer, ForeignKey(f"{environ.get('MYSQL_DB_NAME')}.parent.id"))
    __mapper_args__ = {
        "polymorphic_identity": "child_sti",
    }

    def __repr__(self):
        return f"<ChildSTI(id={self.id} name={self.name} parent_id={self.parent_id})>"
