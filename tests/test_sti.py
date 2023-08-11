"""Testing sqlalchemyexample__init__()"""
# import pytest
from sqlalchemy import inspect


class TestSTI:
    def test_tables_exist(self, setup_db_sti):
        engine, session, base = setup_db_sti

        inspector = inspect(engine)
        assert 'login' in inspector.get_table_names()

    def test_login(self, setup_db_sti):
        engine, session, base = setup_db_sti
        import sti as tab_cfg

        login = tab_cfg.LogIn(email='john@bar.foo')
        session.add(login)
        qry = session.query(tab_cfg.LogIn).filter_by(email='john@bar.foo').first()
        session.commit()

        assert login.email == 'john@bar.foo'
        assert str(login) == 'john@bar.foo'
        assert qry.email == 'john@bar.foo'
        pass

    def test_login_dunder_repr_ok(self, setup_db_sti):
        import sti as tab_cfg

        engine, session, base = setup_db_sti

        login = tab_cfg.LogIn(email='john@bar.foo')
        session.add_all([login])
        session.commit()

        assert repr(login) == '<LogIn(id=1 email=john@bar.foo)>'
        pass

    def test_login_dunder_str_ok(self):
        import sti as tab_cfg

        login = tab_cfg.LogIn(email='john@bar.foo')

        assert str(login) == 'john@bar.foo'
        pass

    def test_student(self, setup_db_sti):
        engine, session, base = setup_db_sti
        import sti as tab_cfg

        student = tab_cfg.Student(email='john@bar.foo', name='John', surname='Doe')
        session.add(student)
        qry = session.query(tab_cfg.LogIn).filter_by(email='john@bar.foo').first()
        session.commit()

        assert qry.email == 'john@bar.foo'
        assert qry.name == 'John'
        assert qry.surname == 'Doe'
        pass

    def test_student_dunder_repr_ok(self, setup_db_sti):
        engine, session, base = setup_db_sti
        import sti as tab_cfg

        student = tab_cfg.Student(email='john@bar.foo', name='John', surname='Doe')
        session.add_all([student])
        session.commit()

        assert repr(student) == '<Student(id=1 name=John surname = Doe email=john@bar.foo)>'
        pass

    def test_student_dunder_str_ok(self):
        import sti as tab_cfg

        student = tab_cfg.Student(email='john@bar.foo', name='John', surname='Doe')

        assert str(student) == 'John Doe'
        pass
