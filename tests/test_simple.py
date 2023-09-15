from os import environ
import pytest
from sqlalchemy import inspect


class TestSimple:
    def test_table_exist(self, setup_db_simple):
        engine, session, base = setup_db_simple
        inspector = inspect(engine)

        assert 'Student' in inspector.get_table_names()
        pass

    def test_Student_table_deletion(self, setup_db_simple):
        engine, session, base = setup_db_simple
        base.metadata.tables[f'{environ.get("MYSQL_DATABASE")}.Student'].drop()
        inspector = inspect(engine)

        assert 'Student' not in inspector.get_table_names()
        pass

    @pytest.mark.select
    def test_Student_assign_data(self, setup_db_simple):
        engine, session, base = setup_db_simple
        import simple as tab_cfg

        Student_list = [
            tab_cfg.Student(name='Ford Prefect'),
            tab_cfg.Student(name='Arthur Dent'),
        ]
        session.add_all(Student_list)
        session.commit()

        qry = session.query(tab_cfg.Student).all()
        assert len(qry) > 0
        for i, x in enumerate(qry):
            assert x.name == Student_list[i].name
            pass
        pass

    @pytest.mark.select
    def test_Student_table_dunder_repr_ok(self, setup_db_simple):
        engine, session, base = setup_db_simple
        import simple as tab_cfg

        Student = tab_cfg.Student(name='John')
        session.add_all([Student])
        session.commit()

        assert repr(Student) == '<Student(id=1 name=John)>'
        pass

    @pytest.mark.select
    def test_Student_table_dunder_str_ok(self, setup_db_simple):
        import simple as tab_cfg

        Student = tab_cfg.Student(name='John')

        assert str(Student) == 'John'
        pass
