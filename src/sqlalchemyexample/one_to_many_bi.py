from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Sequence, String


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String)
    surname = Column(String)
    nickname = Column(String)

    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return f"<User(name={self.name}, surname={self.surname}, nickname={self.nickname})>"

    def __str__(self):
        return f"{self.name} {self.surname}"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"<Address(email_address={self.email_address})>"

    def __str__(self):
        return f"{self.email_address}"
