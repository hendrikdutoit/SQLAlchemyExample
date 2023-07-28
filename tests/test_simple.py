import pytest
from sqlalchemy import inspect
import simple_tables as tab_cfg


class TestSimpleTable:
    def test_table_exist(self, setup_db_st):
        engine, session, base = setup_db_st
        inspector = inspect(engine)

        assert 'parent' in inspector.get_table_names()
        assert 'child' in inspector.get_table_names()
        pass

    def test_parent_table_deletion(self, setup_db_st):
        engine, session, base = setup_db_st
        base.metadata.tables['parent'].drop()
        inspector = inspect(engine)

        assert 'parent' not in inspector.get_table_names()
        assert 'child' in inspector.get_table_names()
        pass

    @pytest.mark.select
    def test_parent_assign_data(self, setup_db_st):
        engine, session, base = setup_db_st
        parent_list = [
            tab_cfg.Parent(name='John Doe'),
            tab_cfg.Parent(name='Jane Smith'),
        ]
        session.add_all(parent_list)
        session.commit()

        qry = session.query(tab_cfg.Parent).all()
        assert len(qry) > 0
        for i, x in enumerate(qry):
            assert x.name == parent_list[i].name
            pass
        pass

    @pytest.mark.select
    def test_parent_table_dunder(self):
        parent = tab_cfg.Parent(name='John')
        assert repr(parent) == '<Parent(name=John)>'
        pass
