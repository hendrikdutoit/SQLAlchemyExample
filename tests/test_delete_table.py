import pytest
from sqlalchemy import inspect
import db_connection as dbc


class TestDeleteTable:
    def test_table_creation(self, setup_db):
        # import default_tables as dt
        inspector = inspect(dbc.engine)
        assert 'parent' in inspector.get_table_names()
        assert 'child' in inspector.get_table_names()
        pass

    def test_parent_table_deletion(self, setup_db):
        # import default_tables as dt
        from db_connection import Base

        Base.metadata.tables['parent'].drop()
        inspector = inspect(dbc.engine)
        assert 'parent' not in inspector.get_table_names()
        pass

    @pytest.mark.select
    def test_parent_assign_data(self, setup_db):
        import default_tables as dt

        parent_list = [dt.Parent(name='John Doe'), dt.Parent(name='Jane Smith')]
        dbc.session.add_all(parent_list)
        dbc.session.commit()

        qry = dbc.session.query(dt.Parent).all()
        assert len(qry) > 0
        for i, x in enumerate(qry):
            assert x.name == parent_list[i].name
            pass
        pass

    @pytest.mark.select
    def test_parent_assign_data_dup(self, setup_db):
        import default_tables as dt

        parent_list = [dt.Parent(name='John Doe'), dt.Parent(name='Jane Smith')]
        dbc.session.add_all(parent_list)
        dbc.session.commit()

        qry = dbc.session.query(dt.Parent).all()
        assert len(qry) > 0
        for i, x in enumerate(qry):
            assert x.name == parent_list[i].name
            pass
        pass
