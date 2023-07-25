"""
SQLAlchemy V1.4.46
Example: One-to_Many Bi-directional

https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
"""
import default_tables as dt
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer


class ParentOTMBi(dt.Parent):
    __mapper_args__ = {
        "polymorphic_identity": "parent_onetomany_bi",
    }
    children = relationship("ChildOTMBi", back_populates="parent")


class ChildOTMBi(dt.Child):
    parent_id2 = Column(Integer, ForeignKey("parent.id"))
    parent = relationship("ParentOTMBi", back_populates="children")
    __mapper_args__ = {
        "polymorphic_identity": "child_onetomany_bi",
    }

    def __repr__(self):
        return f"<Child(id={self.id} name={self.name} parent_id={self.parent_id2})>"
