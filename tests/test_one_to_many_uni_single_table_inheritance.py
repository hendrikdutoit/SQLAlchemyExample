"""Testing sqlalchemyexample__init__()"""
# import pytest
import db_connection as dbc
from sqlalchemy import inspect
import one_to_many_uni_single_table_inheritance as tab_cfg


class TestOTMUniSTI:
    def test_table_creation(self, setup_db_otm_uni_sti):
        # import pdb;pdb.set_trace()
        engine, session, base = setup_db_otm_uni_sti
        inspector = inspect(engine)
        assert 'parent' in inspector.get_table_names()
        assert 'child' in inspector.get_table_names()
        pass

    # def test_one_to_many_uni_parent(self, setup_db):
    #     import pdb; pdb.set_trace()
    #     import one_to_many_uni_single_table_inheritance as otm_u_si
    #     parent = otm_u_si.ParentOTMUni(name="ed")
    #     dbc.session.add(parent)
    #     qry = (dbc.session.query(otm_u_si.ParentOTMUni).filter_by(name="ed").first())
    #     dbc.session.commit()
    #
    #     assert parent.name == 'ed'
    #     assert str(parent) == 'ed'
    #     assert qry.name == 'ed'
    #     pass

    def test_one_to_many_uni_child_with_parent(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        parent = tab_cfg.ParentOTMUni(name="ed")
        child = tab_cfg.ChildOTMUni(name="eddie", parent_id=1)
        dbc.session.add(parent)
        dbc.session.add(child)
        dbc.session.commit()

        assert parent.name == 'ed'
        assert str(parent) == 'ed'
        assert child.name == 'eddie'
        assert str(child) == 'eddie'
        pass

    # def test_one_to_many_uni_child_no_parent(self, setup_db):
    #     import one_to_many_uni_single_table_inheritance as otm_u_si
    #     child = otm_u_si.ChildOTMUni(name="eddie", parent_id=1)
    #     dbc.session.add(child)
    #     with pytest.raises(Exception) as e_info:
    #         dbc.session.commit()
    #     assert e_info.typename == 'IntegrityError'
    #     pass
