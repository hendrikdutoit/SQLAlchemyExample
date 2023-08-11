"""Testing sqlalchemyexample__init__()"""
import pytest
from sqlalchemy import inspect


class TestOtmBi:
    def test_tables_exist(self, setup_db_otm_bi):
        engine, session, base = setup_db_otm_bi

        inspector = inspect(engine)
        assert 'author' in inspector.get_table_names()
        assert 'book' in inspector.get_table_names()

    def test_author(self, setup_db_otm_bi):
        engine, session, base = setup_db_otm_bi
        import otm_bi as tab_cfg

        author = tab_cfg.Author(name='Ford', surname='Prefect')
        session.add(author)
        qry = session.query(tab_cfg.Author).filter_by(surname='Prefect').first()
        session.commit()

        assert author.name == 'Ford'
        assert author.surname == 'Prefect'
        assert qry.name == 'Ford'
        assert qry.surname == 'Prefect'
        pass

    def test_author_dunder_repr_ok(self, setup_db_otm_bi):
        engine, session, base = setup_db_otm_bi
        import otm_bi as tab_cfg

        author = tab_cfg.Author(name='Ford', surname='Prefect')
        session.add_all([author])
        session.commit()

        assert repr(author) == '<Author(id=1 name=Ford surname=Prefect)>'
        pass

    def test_author_dunder_str_ok(self):
        import otm_bi as tab_cfg

        author = tab_cfg.Author(name='Ford', surname='Prefect')

        assert str(author) == 'Ford Prefect'
        pass

    def test_book(self, setup_db_otm_bi):
        engine, session, base = setup_db_otm_bi
        import otm_bi as tab_cfg

        book = tab_cfg.Book(name='Hitchikers Guide')
        session.add(book)
        qry = session.query(tab_cfg.Book).filter_by(name='Hitchikers Guide').first()
        session.commit()

        assert qry.name == 'Hitchikers Guide'
        pass

    def test_book_dunder_repr_ok(self, setup_db_otm_bi):
        engine, session, base = setup_db_otm_bi
        import otm_bi as tab_cfg

        book = tab_cfg.Book(name='Hitchikers Guide')
        session.add_all([book])
        session.commit()

        assert repr(book) == '<Book(id=1 name=Hitchikers Guide)>'
        pass

    def test_book_dunder_str_ok(self):
        import otm_bi as tab_cfg

        book = tab_cfg.Book(name='Hitchikers Guide')

        assert str(book) == 'Hitchikers Guide'
        pass

    def test_book_and_author(self, setup_db_otm_bi):
        engine, session, base = setup_db_otm_bi
        import otm_bi as tab_cfg

        author = tab_cfg.Author(name='Ford', surname='Prefect')
        session.add(author)
        book = tab_cfg.Book(name='Hitchikers Guide', author_id=author.id)
        session.add(book)
        qry = session.query(tab_cfg.Book).filter_by(name='Hitchikers Guide').first()
        session.commit()

        assert qry.name == 'Hitchikers Guide'
        pass

    def test_book_add_with_no_author(self, setup_db_otm_bi):
        engine, session, base = setup_db_otm_bi
        import otm_bi as tab_cfg

        book = tab_cfg.Book(name='Hitchikers Guide', author_id=1)
        session.add(book)
        with pytest.raises(Exception) as e_info:
            session.commit()
        assert e_info.typename == 'IntegrityError'
        pass


class TestOtmUni:
    def test_tables_exist(self, setup_db_otm_uni):
        engine, session, base = setup_db_otm_uni

        inspector = inspect(engine)
        assert 'student' in inspector.get_table_names()
        assert 'course' in inspector.get_table_names()

    def test_student(self, setup_db_otm_uni):
        engine, session, base = setup_db_otm_uni
        import otm_uni as tab_cfg

        student = tab_cfg.Student(name='Arthur', surname='Dent', email='arthur@bar.foo')
        session.add(student)
        qry = session.query(tab_cfg.Student).filter_by(surname='Dent').first()
        session.commit()

        assert student.name == 'Arthur'
        assert student.surname == 'Dent'
        assert student.email == 'arthur@bar.foo'
        assert qry.name == 'Arthur'
        assert qry.surname == 'Dent'
        assert qry.email == 'arthur@bar.foo'
        pass

    def test_student_dunder_repr_ok(self, setup_db_otm_uni):
        engine, session, base = setup_db_otm_uni
        import otm_uni as tab_cfg

        student = tab_cfg.Student(name='Arthur', surname='Dent', email='arthur@bar.foo')
        session.add_all([student])
        session.commit()

        assert repr(student) == '<Student(id=1 name=Arthur surname=Dent email=arthur@bar.foo)>'
        pass

    def test_student_dunder_str_ok(self):
        import otm_uni as tab_cfg

        student = tab_cfg.Student(name='Arthur', surname='Dent', email='arthur@bar.foo')

        assert str(student) == 'Arthur Dent'
        pass

    def test_course(self, setup_db_otm_uni):
        engine, session, base = setup_db_otm_uni
        import otm_uni as tab_cfg

        course = tab_cfg.Course(name='Life, the Universe, and Everything')
        session.add(course)
        qry = session.query(tab_cfg.Course).filter_by(name='Life, the Universe, and Everything').first()
        session.commit()

        assert qry.name == 'Life, the Universe, and Everything'
        pass

    def test_course_dunder_repr_ok(self, setup_db_otm_uni):
        engine, session, base = setup_db_otm_uni
        import otm_uni as tab_cfg

        course = tab_cfg.Course(name='Life, the Universe, and Everything')
        session.add_all([course])
        session.commit()

        assert repr(course) == '<Course(id=1 name=Life, the Universe, and Everything)>'
        pass

    def test_course_dunder_str_ok(self):
        import otm_uni as tab_cfg

        course = tab_cfg.Course(name='Life, the Universe, and Everything')

        assert str(course) == 'Life, the Universe, and Everything'
        pass

    def test_course_and_student(self, setup_db_otm_uni):
        engine, session, base = setup_db_otm_uni
        import otm_uni as tab_cfg

        student = tab_cfg.Student(name='Arthur', surname='Dent')
        session.add(student)
        course = tab_cfg.Course(name='Life, the Universe, and Everything', student_id=student.id)
        session.add(course)
        qry = session.query(tab_cfg.Course).filter_by(name='Life, the Universe, and Everything').first()
        session.commit()

        assert qry.name == 'Life, the Universe, and Everything'
        pass

    def test_course_add_with_no_student(self, setup_db_otm_uni):
        engine, session, base = setup_db_otm_uni
        import otm_uni as tab_cfg

        course = tab_cfg.Course(name='Life, the Universe, and Everything', student_id=1)
        session.add(course)
        with pytest.raises(Exception) as e_info:
            session.commit()
        assert e_info.typename == 'IntegrityError'
        pass
