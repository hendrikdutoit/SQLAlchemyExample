from os import environ
import pytest
from sqlalchemy import inspect


class TestSimple:
    def test_table_exist(self, setup_db_simple):
        engine, session, base = setup_db_simple
        inspector = inspect(engine)

        assert 'person' in inspector.get_table_names()
        pass

    def test_person_table_deletion(self, setup_db_simple):
        engine, session, base = setup_db_simple
        base.metadata.tables[f'{environ.get("MYSQL_DB_NAME")}.person'].drop()
        inspector = inspect(engine)

        assert 'person' not in inspector.get_table_names()
        pass

    @pytest.mark.select
    def test_person_assign_data(self, setup_db_simple):
        engine, session, base = setup_db_simple
        import ex01_00_simple as tab_cfg

        person_list = [
            tab_cfg.Person(name='John Doe'),
            tab_cfg.Person(name='Jane Smith'),
        ]
        session.add_all(person_list)
        session.commit()

        qry = session.query(tab_cfg.Person).all()
        assert len(qry) > 0
        for i, x in enumerate(qry):
            assert x.name == person_list[i].name
            pass
        pass

    @pytest.mark.select
    def test_person_table_dunder_repr_ok(self, setup_db_simple):
        engine, session, base = setup_db_simple
        import ex01_00_simple as tab_cfg

        person = tab_cfg.Person(name='John')
        session.add_all([person])
        session.commit()

        assert repr(person) == '<Person(id=1 name=John)>'
        pass

    @pytest.mark.select
    def test_person_table_dunder_str_ok(self, setup_db_simple):
        import ex01_00_simple as tab_cfg

        person = tab_cfg.Person(name='John')

        assert str(person) == 'John'
        pass
