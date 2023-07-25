'''Testing sqlalchemyexample__init__()'''
import pytest
import db_connection as dbc
from sqlalchemy import inspect


def test_table_creation(setup_db):
    # import one_to_many_bi_single_table_inheritance as otm_b_si
    inspector = inspect(dbc.engine)
    assert 'parent' in inspector.get_table_names()
    assert 'child' in inspector.get_table_names()
    pass


def test_one_to_many_bi_parent(setup_db):
    import one_to_many_bi_single_table_inheritance as otm_b_si

    parent = otm_b_si.ParentOTMBi(name="ed")
    dbc.session.add(parent)
    qry = dbc.session.query(otm_b_si.ParentOTMBi).filter_by(name="ed").first()
    dbc.session.commit()

    assert parent.name == 'ed'
    assert str(parent) == 'ed'
    assert qry.name == 'ed'
    pass


def test_one_to_many_bi_child_with_parent(setup_db):
    import one_to_many_bi_single_table_inheritance as otm_b_si

    parent = otm_b_si.ParentOTMBi(name="ed")
    child = otm_b_si.ChildOTMBi(name="eddie", parent_id2=1)
    dbc.session.add(parent)
    dbc.session.add(child)
    dbc.session.commit()

    assert parent.name == 'ed'
    assert str(parent) == 'ed'
    assert child.name == 'eddie'
    assert str(child) == 'eddie'
    pass


def test_one_to_many_bi_child_no_parent(setup_db):
    import one_to_many_bi_single_table_inheritance as otm_b_si

    child = otm_b_si.ChildOTMBi(name="eddie", parent_id2=1)
    dbc.session.add(child)
    with pytest.raises(Exception) as e_info:
        dbc.session.commit()
    assert e_info.typename == 'IntegrityError'
    pass
