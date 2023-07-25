import pytest
from sqlalchemy import inspect
import default_tables as dt


class TestDeleteTable:
    def test_table_creation(self, setup_db):
        engine, session, base = setup_db
        inspector = inspect(engine)

        assert 'parent' in inspector.get_table_names()
        assert 'child' in inspector.get_table_names()
        pass

    def test_parent_table_deletion(self, setup_db):
        engine, session, base = setup_db
        base.metadata.tables['parent'].drop()
        inspector = inspect(engine)

        assert 'parent' not in inspector.get_table_names()
        assert 'child' in inspector.get_table_names()
        pass

    @pytest.mark.select
    def test_parent_assign_data(self, setup_db):
        engine, session, base = setup_db
        parent_list = [dt.Parent(name='John Doe'), dt.Parent(name='Jane Smith')]
        session.add_all(parent_list)
        session.commit()

        qry = session.query(dt.Parent).all()
        assert len(qry) > 0
        for i, x in enumerate(qry):
            assert x.name == parent_list[i].name
            pass
        pass

    @pytest.mark.select
    def test_parent_assign_data_dup(self, setup_db):
        engine, session, base = setup_db
        parent_list = [dt.Parent(name='John Doe'), dt.Parent(name='Jane Smith')]
        session.add_all(parent_list)
        session.commit()

        qry = session.query(dt.Parent).all()
        assert len(qry) > 0
        for i, x in enumerate(qry):
            assert x.name == parent_list[i].name
            pass
        pass
