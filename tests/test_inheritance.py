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
        from inheritance import sti as tab_cfg

        login = tab_cfg.LogIn(email='john@bar.foo')
        session.add(login)
        qry = session.query(tab_cfg.LogIn).filter_by(email='john@bar.foo').first()
        session.commit()

        assert login.email == 'john@bar.foo'
        assert str(login) == 'john@bar.foo'
        assert qry.email == 'john@bar.foo'
        pass

    def test_login_dunder_repr_ok(self, setup_db_sti):
        from inheritance import sti as tab_cfg

        engine, session, base = setup_db_sti

        login = tab_cfg.LogIn(email='john@bar.foo')
        session.add_all([login])
        session.commit()

        assert repr(login) == '<LogIn(id=1 email=john@bar.foo)>'
        pass

    def test_login_dunder_str_ok(self):
        from inheritance import sti as tab_cfg

        login = tab_cfg.LogIn(email='john@bar.foo')

        assert str(login) == 'john@bar.foo'
        pass

    def test_student(self, setup_db_sti):
        engine, session, base = setup_db_sti
        from inheritance import sti as tab_cfg

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
        from inheritance import sti as tab_cfg

        student = tab_cfg.Student(email='john@bar.foo', name='John', surname='Doe')
        session.add_all([student])
        session.commit()

        assert repr(student) == '<Student(id=1 name=John surname = Doe email=john@bar.foo)>'
        pass

    def test_student_dunder_str_ok(self):
        from inheritance import sti as tab_cfg

        student = tab_cfg.Student(email='john@bar.foo', name='John', surname='Doe')

        assert str(student) == 'John Doe'
        pass


class TestOtmBiSti:
    def test_tables_exist(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti

        inspector = inspect(engine)
        assert 'login' in inspector.get_table_names()
        assert 'book' in inspector.get_table_names()

    def test_login(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti
        from inheritance import otm_bi_sti as tab_cfg

        login = tab_cfg.LogIn(email='ford@bar.foo')
        session.add(login)
        qry = session.query(tab_cfg.LogIn).filter_by(email='ford@bar.foo').first()
        session.commit()

        assert login.email == 'ford@bar.foo'
        assert str(login) == 'ford@bar.foo'
        assert qry.email == 'ford@bar.foo'
        pass

    def test_login_dunder_repr_ok(self, setup_db_otm_bi_sti):
        from inheritance import otm_bi_sti as tab_cfg

        engine, session, base = setup_db_otm_bi_sti

        login = tab_cfg.LogIn(email='ford@bar.foo')
        session.add_all([login])
        session.commit()

        assert repr(login) == '<LogIn(id=1 email=ford@bar.foo)>'
        pass

    def test_login_dunder_str_ok(self):
        from inheritance import otm_bi_sti as tab_cfg

        login = tab_cfg.LogIn(email='ford@bar.foo')

        assert str(login) == 'ford@bar.foo'
        pass

    def test_author(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti
        from inheritance import otm_bi_sti as tab_cfg

        author = tab_cfg.Author(email='ford@bar.foo', name='Ford', surname='Prefect')
        session.add(author)
        qry = session.query(tab_cfg.LogIn).filter_by(email='ford@bar.foo').first()
        session.commit()

        assert qry.email == 'ford@bar.foo'
        assert qry.name == 'Ford'
        assert qry.surname == 'Prefect'
        pass

    def test_author_dunder_repr_ok(self, setup_db_otm_bi_sti):
        from inheritance import otm_bi_sti as tab_cfg

        engine, session, base = setup_db_otm_bi_sti

        author = tab_cfg.Author(email='ford@bar.foo', name='Ford', surname='Prefect')
        session.add_all([author])
        session.commit()

        assert repr(author) == '<Author(id=1 name=Ford surname=Prefect email=ford@bar.foo)>'
        pass

    def test_author_dunder_str_ok(self):
        from inheritance import otm_bi_sti as tab_cfg

        author = tab_cfg.Author(email='ford@bar.foo', name='Ford', surname='Prefect')

        assert str(author) == 'Ford Prefect'
        pass

    def test_book(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti
        from inheritance import otm_bi_sti as tab_cfg

        book = tab_cfg.Book(name='Physics')
        session.add(book)
        qry = session.query(tab_cfg.Book).filter_by(name='Physics').first()
        session.commit()

        assert qry.name == 'Physics'
        pass

    def test_book_dunder_repr_ok(self, setup_db_otm_bi_sti):
        from inheritance import otm_bi_sti as tab_cfg

        engine, session, base = setup_db_otm_bi_sti

        book = tab_cfg.Book(name='Physics')
        session.add_all([book])
        session.commit()

        assert repr(book) == '<Book(id=1 name=Physics)>'
        pass

    def test_book_dunder_str_ok(self):
        from inheritance import otm_bi_sti as tab_cfg

        book = tab_cfg.Book(name='Physics')

        assert str(book) == 'Physics'
        pass


class TestMixin:
    def test_tables_exist(self, setup_db_mixin):
        engine, session, base = setup_db_mixin

        inspector = inspect(engine)
        assert 'mymodel' in inspector.get_table_names()

    def test_book_dunders(self, setup_db_mixin):
        from inheritance import mixin as tab_cfg

        engine, session, base = setup_db_mixin

        mymodel = tab_cfg.MyModel(id=1, name='Model 1')
        session.add_all([mymodel])
        session.commit()

        assert repr(mymodel) == '<MyModel(id=1 name=Model 1)>'
        assert str(mymodel) == '1,Model 1'
        pass
