"""
SQLAlchemy V1.4.46
Example: One-to_Many Uni-directional

https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer

# import db
import default_tables as dt


class ParentOTMUni(dt.Parent):
    __tablename__ = "parent_onetomany_uni"
    children = relationship("ChildOTMUni")
    super.__init__()

    def __repr__(self):
        return f"<Parent(id={self.id} name={self.name})>"

    def __str__(self):
        return f"{self.name}"


class ChildOTMUni(dt.Child):
    __tablename__ = "child_onetomany_uni"
    parent_id = Column(Integer, ForeignKey("parent_onetomany_uni.id"))
    super.__init__()

    def __repr__(self):
        return f"<Child(id={self.id} name={self.name} parent_id={self.parent_id})>"

    def __str__(self):
        return f"{self.name}"
