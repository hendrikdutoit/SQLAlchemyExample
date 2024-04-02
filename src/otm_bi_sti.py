"""
One-to-Many: Bidirectional and Single Inheritance
=================================================
In an Entity-Relationship (ER) diagram, a one-to-many (1:N) relationship exists when one entity instance is associated
with multiple instances of another entity. When we say the relationship is bidirectional, we mean that there is a
meaningful description of the relationship in both directions.

In this inheritance mechanism, multiple subclasses (entities) share a single database table. Each row in the table
includes a special discriminator column that indicates which subclass it belongs to.

Let's consider an example of a one-to-many relationship between "Author" and "Book" entities:

- **Author:** An entity that represents a person who writes books. An author can write multiple books, so there's a one-to-many relationship from Author to Book.
- **Book:** An entity that represents a literary work. Each book is written by one and only one author, so there's a many-to-one relationship from Book to Author.

Diagram
-------

- The "Author" entity has an attribute "author_id" that uniquely identifies each author.
- The "Book" entity has attributes including "book_id" (a unique identifier for each book) and "author_id" (a foreign
  key referencing the "Author" entity).
- A one-to-many relationship is depicted from "Author" to "Book", symbolized by a line connecting these entities. The
  line ends with a crow's foot near "Book", indicating the "many" side, and a straight line near "Author", indicating
  the "one" side.

Bidirectionality
----------------

The bidirectionality of the relationship can be described as:

- One author writes many books (from "Author" to "Book").
- Each book is written by one author (from "Book" to "Author").

This bidirectional understanding helps in understanding how the entities are related in both directions, aiding in both
database design and query formulation.

Here's an illustration of this relationship:

.. code-block::

       1           N
    author <────> book

- The "1" near "Author" signifies the "one" side of the relationship.
- The "N" near "Book" signifies the "many" side of the relationship.
- The "author_id" in "Book" is a foreign key that creates the linkage between the two entities, ensuring referential
  integrity.

See: https://docs.sqlalchemy.org/en/14/_modules/examples/inheritance/single.html
"""
from os import environ

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import drop_database

url = engine.URL.create(
    'mysql+mysqlconnector',
    username='root',
    password=environ.get('MYSQL_ROOT_PASSWORD'),
    host=environ.get('MYSQL_HOST'),
    port=environ.get('MYSQL_TCP_PORT'),
    database=environ.get('MYSQL_DATABASE'),
)
# url = 'sqlite:///:memory:'
engine = create_engine(url, echo=False)
if database_exists(engine.url):
    drop_database(engine.url)
create_database(engine.url)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base(bind=engine)


class LogIn(Base):
    __tablename__ = 'login'
    __table_args__ = {'schema': environ.get('MYSQL_DATABASE')}

    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    type = Column(String(20))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'login',
    }
    pass

    def __repr__(self):
        return f'<LogIn(id={self.id} email={self.email})>'

    def __str__(self):
        return f'{self.email}'


class Author(LogIn):
    name = Column(String(45))
    surname = Column(String(45))

    books = relationship('Book', back_populates='author')
    __mapper_args__ = {
        'polymorphic_identity': 'author',
    }

    def __repr__(self):
        return f'<Author(id={self.id} name={self.name} surname={self.surname} email={self.email})>'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(Base):
    __tablename__ = 'book'
    __table_args__ = {'schema': environ.get('MYSQL_DATABASE')}

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    author_id = Column(Integer, ForeignKey(f"{environ.get('MYSQL_DATABASE')}.login.id"))

    author = relationship('Author', back_populates='books')
    pass

    def __repr__(self):
        return f'<Book(id={self.id} name={self.name})>'

    def __str__(self):
        return f'{self.name}'
