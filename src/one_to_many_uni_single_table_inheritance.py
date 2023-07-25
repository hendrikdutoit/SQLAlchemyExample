"""
SQLAlchemy V1.4.46
Example: One-to_Many Uni-directional

https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
"""
import default_tables as dt
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer


class ParentOTMUni(dt.Parent):
    __mapper_args__ = {
        "polymorphic_identity": "parent_onetomany_uni",
    }
    children = relationship("ChildOTMUni")


class ChildOTMUni(dt.Child):
    parent_id = Column(Integer, ForeignKey("parent.id"))
    __mapper_args__ = {
        "polymorphic_identity": "child_onetomany_uni",
    }

    def __repr__(self):
        return f"<Child(id={self.id} name={self.name} parent_id={self.parent_id})>"
