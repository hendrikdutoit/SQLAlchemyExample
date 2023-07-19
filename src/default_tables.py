from sqlalchemy import Column, Integer, String
import db


class Parent(db.Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))


class Child(db.Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))


# db.Base.metadata.create_all()
pass
