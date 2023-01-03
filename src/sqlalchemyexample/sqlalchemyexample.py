"""Example for exploring SQLAlchemy

This project provide code how to use AQLAlchemy.  This idea is to build an
example sequentially in steps to give new users the idea on where to start
and how to progress.  Along the way some principles will be exhibited.  The
code should be self-explanatory without as little as possible documentation,
else the project is failing.

This example illustrate the following:
--------------------------------------

1. Establish a link to a MySQL or SQLite database

2. Create tables

3. Populate the tables

4. Configure a many--to-may relationship

5. Query the tables

References
----------

- https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_many_to_many_relationships.htm
- https://docs.sqlalchemy.org/en/13/orm/tutorial.html#building-a-relationship
- https://cyruslab.net/2020/07/16/pythoncreate-database-if-not-exists-with-sqlalchemy/
"""

from pathlib import Path
from beetools import msg_info
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import src.sqlalchemyexample.one_to_many_bi as ua


class DB:
    """Class description"""

    def __init__(self, p_source_dir):
        """Method description"""
        print(msg_info('Instantiating the class (example)...'))
        self.success = False
        self.dir = p_source_dir
        self.db_path = Path(self.dir, 'SQLAlchemyExample.db')
        self.url = f'sqlite:///{self.db_path}'
        self.engine = create_engine(self.url, echo=True)
        ua.Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)
        if self.engine:
            self.success = True
        pass

    # def populate_user(self, p_name, p_surname, p_nickname):
    #     return ua.User(name = p_name, surname = p_surname, nickname = p_nickname)
    #     pass

    def run(self):
        """Method description"""
        pass


if __name__ == '__main__':
    t_sqlalchemyexample = DB()
    if t_sqlalchemyexample.success:
        t_sqlalchemyexample.run()
# end __main__
