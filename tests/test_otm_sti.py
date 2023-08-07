"""Testing sqlalchemyexample__init__()"""
# import pytest
from sqlalchemy import inspect


class TestOtmUniSti:
    def test_tables_exist(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti

        inspector = inspect(engine)
        assert 'login' in inspector.get_table_names()
        assert 'course' in inspector.get_table_names()

    def test_login(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        import otm_uni_sti as tab_cfg

        login = tab_cfg.LogIn(email='john@bar.foo')
        session.add(login)
        qry = session.query(tab_cfg.LogIn).filter_by(email='john@bar.foo').first()
        session.commit()

        assert login.email == 'john@bar.foo'
        assert str(login) == 'john@bar.foo'
        assert qry.email == 'john@bar.foo'
        pass

    def test_login_dunder_repr_ok(self, setup_db_otm_uni_sti):
        import otm_uni_sti as tab_cfg

        engine, session, base = setup_db_otm_uni_sti

        login = tab_cfg.LogIn(email='john@bar.foo')
        session.add_all([login])
        session.commit()

        assert repr(login) == '<LogIn(id=1 email=john@bar.foo)>'
        pass

    def test_login_dunder_str_ok(self):
        import otm_uni_sti as tab_cfg

        login = tab_cfg.LogIn(email='john@bar.foo')

        assert str(login) == 'john@bar.foo'
        pass

    def test_student(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        import otm_uni_sti as tab_cfg

        student = tab_cfg.Student(email='john@bar.foo', name='John', surname='Doe')
        session.add(student)
        qry = session.query(tab_cfg.LogIn).filter_by(email='john@bar.foo').first()
        session.commit()

        assert qry.email == 'john@bar.foo'
        assert qry.name == 'John'
        assert qry.surname == 'Doe'
        pass

    def test_student_dunder_repr_ok(self, setup_db_otm_uni_sti):
        import otm_uni_sti as tab_cfg

        engine, session, base = setup_db_otm_uni_sti

        student = tab_cfg.Student(email='john@bar.foo', name='John', surname='Doe')
        session.add_all([student])
        session.commit()

        assert (
            repr(student) == '<Student(id=1 name=John surname=Doe email=john@bar.foo)>'
        )
        pass

    def test_student_dunder_str_ok(self):
        import otm_uni_sti as tab_cfg

        student = tab_cfg.Student(email='john@bar.foo', name='John', surname='Doe')

        assert str(student) == 'John Doe'
        pass

    def test_course(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        import otm_uni_sti as tab_cfg

        course = tab_cfg.Course(name='Physics')
        session.add(course)
        qry = session.query(tab_cfg.Course).filter_by(name='Physics').first()
        session.commit()

        assert qry.name == 'Physics'
        pass

    def test_course_dunder_repr_ok(self, setup_db_otm_uni_sti):
        import otm_uni_sti as tab_cfg

        engine, session, base = setup_db_otm_uni_sti

        course = tab_cfg.Course(name='Physics')
        session.add_all([course])
        session.commit()

        assert repr(course) == '<Course(id=1 name=Physics)>'
        pass

    def test_course_dunder_str_ok(self):
        import otm_uni_sti as tab_cfg

        course = tab_cfg.Course(name='Physics')

        assert str(course) == 'Physics'
        pass
