"""
SQLAlchemy V1.4.46
Example: One-to_Many Bi-directional

https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
import db_connection as dbc


Base = dbc.Base
engine = dbc.engine
session = dbc.session


class Parent(Base):
    __tablename__ = 'parent_otm_bi'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    type = Column(String(20))

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "parent_otm_bi",
    }
    pass

    def __repr__(self):
        return f"<Parent(id={self.id} name={self.name})>"

    def __str__(self):
        return f"{self.name}"


class Child(Base):
    __tablename__ = 'child_otm_bi'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    type = Column(String(20))

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "child_otm_bi",
    }
    pass

    def __repr__(self):
        return f"<Child(id={self.id} name={self.name}>"

    def __str__(self):
        return f"{self.name}"


class ParentOTMBi(Parent):
    __mapper_args__ = {
        "polymorphic_identity": "parent_onetomany_bi",
    }
    children = relationship("ChildOTMBi", back_populates="parent")


class ChildOTMBi(Child):
    parent_id2 = Column(Integer, ForeignKey("parent_otm_bi.id"))
    parent = relationship("ParentOTMBi", back_populates="children")
    __mapper_args__ = {
        "polymorphic_identity": "child_onetomany_bi",
    }

    def __repr__(self):
        return f"<Child(id={self.id} name={self.name} parent_id={self.parent_id2})>"
