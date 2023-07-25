from sqlalchemy import Column, Integer, String
import db_connection as dbc


class Parent(dbc.Base):
    __tablename__ = 'parent'
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


class Child(dbc.Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    type = Column(String(20))

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "child",
    }
    pass

    def __repr__(self):
        return f"<Child(id={self.id} name={self.name}>"

    def __str__(self):
        return f"{self.name}"
