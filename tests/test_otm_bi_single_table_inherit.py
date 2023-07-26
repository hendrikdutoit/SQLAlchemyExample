'''Testing sqlalchemyexample__init__()'''
import pytest
from sqlalchemy import inspect
import otm_bi_single_table_inherit as tab_cfg


class TestOTMBiSTI:
    # def test_table_creation(self, setup_db_otm_bi_sti):
    #     engine, session, base = setup_db_otm_bi_sti
    #
    #     inspector = inspect(engine)
    #     assert 'parent' in inspector.get_table_names()
    #     assert 'child' in inspector.get_table_names()
    #     pass
    #
    def test_otm_bi_parent(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti

        inspector = inspect(engine)
        assert 'parent_otm_bi' in inspector.get_table_names()
        assert 'child_otm_bi' in inspector.get_table_names()

        parent = tab_cfg.ParentOTMBiSTI(name="ed")
        session.add(parent)
        qry = session.query(tab_cfg.ParentOTMBiSTI).filter_by(name="ed").first()
        session.commit()

        assert parent.name == 'ed'
        assert str(parent) == 'ed'
        assert qry.name == 'ed'
        pass

    def test_otm_bi_child_with_parent(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti

        inspector = inspect(engine)
        assert 'parent_otm_bi' in inspector.get_table_names()
        assert 'child_otm_bi' in inspector.get_table_names()

        parent = tab_cfg.ParentOTMBiSTI(name="ed")
        child = tab_cfg.ChildOTMBiSTI(name="eddie", parent_id=1)
        session.add(parent)
        session.add(child)
        session.commit()

        assert parent.name == 'ed'
        assert str(parent) == 'ed'
        assert child.name == 'eddie'
        assert str(child) == 'eddie'
        pass

    def test_otm_bi_child_no_parent(self, setup_db_otm_bi_sti):
        engine, session, base = setup_db_otm_bi_sti

        child = tab_cfg.ChildOTMBiSTI(name="eddie", parent_id=1)
        session.add(child)
        with pytest.raises(Exception) as e_info:
            session.commit()
        assert e_info.typename == 'IntegrityError'
        pass
