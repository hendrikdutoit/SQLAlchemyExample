"""
One-to-Many: Unidirectional
===========================
In a one-to-many (1:N) relationship in an Entity-Relationship (ER) diagram, one entity from Entity Set A is associated
with multiple entities from Entity Set B, but each entity in Entity Set B is associated with only one entity in Entity
Set A. This relationship is unidirectional when there's a clear direction of the association, meaning Entity Set A
influences Entity Set B, but not vice versa.

Example: Students and Courses
-----------------------------
Let's consider an example where we have two entities: "Student" and "Course."

- ``Student:`` This entity represents the students in a school.

- ``Course:`` This entity represents the courses offered by the school.

In this case, a Student can enroll in multiple Courses, but each Course is enrolled by one Student at a time. This
establishes a one-to-many relationship from Student to Course.

.. code-block::

    Student 1  ────< Enrolls_In >─────┤ N Course

In the diagram, the "1" near the Student entity indicates that each student enrolls in one or many courses, and the "N"
near the Course entity indicates that a course may be enrolled in by many students.


Constraints and Considerations
------------------------------
**Unidirectional:** The relationship is unidirectional from Student to Course. The student influences the course
enrollment, but the course does not influence the student's attributes.

**Multiplicity:** The multiplicity of the relationship is 1:N, meaning one student can enroll in many courses.

**Participation:** Depending on the business rules, the participation can be total or partial. For instance, if every
student must enroll in at least one course, it's total participation from the Student side.

This simple example captures the essence of a typical one-to-many, unidirectional relationship in an ER diagram.
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


class Student(Base):
    __tablename__ = 'student'
    __table_args__ = {'schema': environ.get('MYSQL_DATABASE')}

    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    name = Column(String(45))
    surname = Column(String(45))

    children = relationship('Course')

    def __repr__(self):
        return f'<Student(id={self.id} name={self.name} surname={self.surname} email={self.email})>'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Course(Base):
    __tablename__ = 'course'
    __table_args__ = {'schema': environ.get('MYSQL_DATABASE')}

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

    student_id = Column(Integer, ForeignKey(f"{environ.get('MYSQL_DATABASE')}.student.id"))
    pass

    def __repr__(self):
        return f'<Course(id={self.id} name={self.name})>'

    def __str__(self):
        return f'{self.name}'
