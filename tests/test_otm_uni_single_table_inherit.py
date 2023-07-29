"""Testing sqlalchemyexample__init__()"""
import pytest
from sqlalchemy import inspect
import otm_uni_single_table_inherit as tab_cfg


class TestOTMUniSTI:
    def test_otm_uni_parent(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti

        inspector = inspect(engine)
        assert 'parent_otm_uni' in inspector.get_table_names()
        assert 'child_otm_uni' in inspector.get_table_names()

        parent = tab_cfg.ParentOTMUniSTI(name="ed")
        session.add(parent)
        qry = session.query(tab_cfg.ParentOTMUniSTI).filter_by(name="ed").first()
        session.commit()

        assert parent.name == 'ed'
        assert str(parent) == 'ed'
        assert qry.name == 'ed'
        pass

    def test_otm_uni_child_with_parent(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti

        inspector = inspect(engine)
        assert 'parent_otm_uni' in inspector.get_table_names()
        assert 'child_otm_uni' in inspector.get_table_names()

        parent = tab_cfg.ParentOTMUniSTI(name="ed")
        child = tab_cfg.ChildOTMUniSTI(name="eddie", parent_id=1)
        session.add(parent)
        session.add(child)
        session.commit()

        assert parent.name == 'ed'
        assert str(parent) == 'ed'
        assert child.name == 'eddie'
        assert str(child) == 'eddie'
        pass

    def test_otm_uni_child_no_parent(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti

        inspector = inspect(engine)
        assert 'parent_otm_uni' in inspector.get_table_names()
        assert 'child_otm_uni' in inspector.get_table_names()

        child = tab_cfg.ChildOTMUniSTI(name="eddie", parent_id=1)
        session.add(child)
        with pytest.raises(Exception) as e_info:
            session.commit()
        assert e_info.typename == 'IntegrityError'
        pass

    def test_parentotmbi_table_dunder_repr_ok(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        parent = tab_cfg.ParentOTMUni(name='John')
        session.add_all([parent])
        session.commit()

        assert repr(parent) == '<ParentOTMUni(id=1 name=John)>'
        pass

    def test_parentotmbi_table_dunder_str_ok(self):
        parent = tab_cfg.ParentOTMUni(name='John')

        assert str(parent) == 'John'
        pass
