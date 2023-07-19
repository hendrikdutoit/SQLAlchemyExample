import pytest
from sqlalchemy import inspect
import db
import default_tables as dt


def test_table_creation(setup_db):
    inspector = inspect(db.engine)
    assert 'parent' in inspector.get_table_names()
    assert 'child' in inspector.get_table_names()
    pass


def test_parent_table_deletion(setup_db):
    db.Base.metadata.tables['parent'].drop()
    inspector = inspect(db.engine)
    assert 'parent' not in inspector.get_table_names()
    pass


@pytest.mark.select
def test_parent_assign_data(setup_db):
    # db.Base.metadata.tables['parent'].drop()
    parent_list = [dt.Parent(name='John Doe'), dt.Parent(name='Jane Smith')]
    db.session.add_all(parent_list)
    db.session.commit()

    qry = db.session.query(dt.Parent).all()
    assert len(qry) > 0
    for i, x in enumerate(qry):
        assert x.name == parent_list[i].name
        pass
    pass


@pytest.mark.select
def test_parent_assign_data_dup(setup_db):
    # db.Base.metadata.tables['parent'].drop()
    parent_list = [dt.Parent(name='John Doe'), dt.Parent(name='Jane Smith')]
    db.session.add_all(parent_list)
    db.session.commit()

    qry = db.session.query(dt.Parent).all()
    assert len(qry) > 0
    for i, x in enumerate(qry):
        assert x.name == parent_list[i].name
        pass
    pass
