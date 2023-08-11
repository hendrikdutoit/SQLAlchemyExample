"""Testing sqlalchemyexample__init__()"""
# import pytest
from sqlalchemy import inspect


class TestOtmBiSti:
    def test_tables_exist(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti

        inspector = inspect(engine)
        assert 'login' in inspector.get_table_names()
        assert 'book' in inspector.get_table_names()

    def test_login(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti
        import otm_bi_sti as tab_cfg

        login = tab_cfg.LogIn(email='ford@bar.foo')
        session.add(login)
        qry = session.query(tab_cfg.LogIn).filter_by(email='ford@bar.foo').first()
        session.commit()

        assert login.email == 'ford@bar.foo'
        assert str(login) == 'ford@bar.foo'
        assert qry.email == 'ford@bar.foo'
        pass

    def test_login_dunder_repr_ok(self, setup_db_otm_bi_sti):
        import otm_bi_sti as tab_cfg

        engine, session, base = setup_db_otm_bi_sti

        login = tab_cfg.LogIn(email='ford@bar.foo')
        session.add_all([login])
        session.commit()

        assert repr(login) == '<LogIn(id=1 email=ford@bar.foo)>'
        pass

    def test_login_dunder_str_ok(self):
        import otm_bi_sti as tab_cfg

        login = tab_cfg.LogIn(email='ford@bar.foo')

        assert str(login) == 'ford@bar.foo'
        pass

    def test_author(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti
        import otm_bi_sti as tab_cfg

        author = tab_cfg.Author(email='ford@bar.foo', name='Ford', surname='Prefect')
        session.add(author)
        qry = session.query(tab_cfg.LogIn).filter_by(email='ford@bar.foo').first()
        session.commit()

        assert qry.email == 'ford@bar.foo'
        assert qry.name == 'Ford'
        assert qry.surname == 'Prefect'
        pass

    def test_author_dunder_repr_ok(self, setup_db_otm_bi_sti):
        import otm_bi_sti as tab_cfg

        engine, session, base = setup_db_otm_bi_sti

        author = tab_cfg.Author(email='ford@bar.foo', name='Ford', surname='Prefect')
        session.add_all([author])
        session.commit()

        assert repr(author) == '<Author(id=1 name=Ford surname=Prefect email=ford@bar.foo)>'
        pass

    def test_author_dunder_str_ok(self):
        import otm_bi_sti as tab_cfg

        author = tab_cfg.Author(email='ford@bar.foo', name='Ford', surname='Prefect')

        assert str(author) == 'Ford Prefect'
        pass

    def test_book(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti
        import otm_bi_sti as tab_cfg

        book = tab_cfg.Book(name='Physics')
        session.add(book)
        qry = session.query(tab_cfg.Book).filter_by(name='Physics').first()
        session.commit()

        assert qry.name == 'Physics'
        pass

    def test_book_dunder_repr_ok(self, setup_db_otm_bi_sti):
        import otm_bi_sti as tab_cfg

        engine, session, base = setup_db_otm_bi_sti

        book = tab_cfg.Book(name='Physics')
        session.add_all([book])
        session.commit()

        assert repr(book) == '<Book(id=1 name=Physics)>'
        pass

    def test_book_dunder_str_ok(self):
        import otm_bi_sti as tab_cfg

        book = tab_cfg.Book(name='Physics')

        assert str(book) == 'Physics'
        pass
