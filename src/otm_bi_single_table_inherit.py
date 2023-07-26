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


class ParentOTMBi(Base):
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
        return f"<ParentOTMBi(id={self.id} name={self.name})>"

    def __str__(self):
        return f"{self.name}"


class ChildOTMBi(Base):
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
        return f"<ChildOTMBi(id={self.id} name={self.name}>"

    def __str__(self):
        return f"{self.name}"


class ParentOTMBiSTI(ParentOTMBi):
    __mapper_args__ = {
        "polymorphic_identity": "parent_otm_bi_sti",
    }
    children = relationship("ChildOTMBiSTI", back_populates="parent")


class ChildOTMBiSTI(ChildOTMBi):
    parent_id = Column(Integer, ForeignKey("parent_otm_bi.id"))
    parent = relationship("ParentOTMBiSTI", back_populates="children")
    __mapper_args__ = {
        "polymorphic_identity": "child_otm_bi_sti",
    }

    def __repr__(self):
        return (
            f"<ChildOTMBiSTI(id={self.id} name={self.name} parent_id={self.parent_id})>"
        )
