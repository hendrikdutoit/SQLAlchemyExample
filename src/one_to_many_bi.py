"""
SQLAlchemy V1.4.46
Example: One-to_Many Bi-directional

https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, UnicodeText


Base = declarative_base()


class ParentOTMBi(Base):
    __tablename__ = "parent_onetomany_bi"
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText)
    children = relationship("ChildOTMBi", back_populates="parent")

    def __repr__(self):
        return f"<Parent(id={self.id} name={self.name})>"

    def __str__(self):
        return f"{self.name}"


class ChildOTMBi(Base):
    __tablename__ = "child_onetomany_bi"
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText)
    parent_id = Column(Integer, ForeignKey("parent_onetomany_bi.id"))
    parent = relationship("ParentOTMBi", back_populates="children")

    def __repr__(self):
        return f"<Child(id={self.id} name={self.name} parent_id={self.parent_id})>"

    def __str__(self):
        return f"{self.name}"
