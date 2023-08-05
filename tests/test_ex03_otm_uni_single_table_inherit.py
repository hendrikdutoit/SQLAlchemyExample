"""Testing sqlalchemyexample__init__()"""
import pytest
from sqlalchemy import inspect


class TestSimple:
    def test_tables_exist(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti

        inspector = inspect(engine)
        assert 'parent' in inspector.get_table_names()
        assert 'child' in inspector.get_table_names()

    def test_parent(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        parent = tab_cfg.Parent(name='John')
        session.add(parent)
        qry = session.query(tab_cfg.Parent).filter_by(name='John').first()
        session.commit()

        assert parent.name == 'John'
        assert str(parent) == 'John'
        assert qry.name == 'John'
        pass

    def test_parent_dunder_repr_ok(self, setup_db_otm_uni_sti):
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        engine, session, base = setup_db_otm_uni_sti

        parent = tab_cfg.Parent(name='John')
        session.add_all([parent])
        session.commit()

        assert repr(parent) == '<Parent(id=1 name=John)>'
        pass

    def test_parent_dunder_str_ok(self, setup_db_otm_uni_sti):
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        parent = tab_cfg.Parent(name='John')

        assert str(parent) == 'John'
        pass

    def test_child(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        child = tab_cfg.Parent(name='Little Johnny')
        session.add(child)
        qry = session.query(tab_cfg.Parent).filter_by(name='Little Johnny').first()
        session.commit()

        assert child.name == 'Little Johnny'
        assert str(child) == 'Little Johnny'
        assert qry.name == 'Little Johnny'
        pass

    def test_child_dunder_repr_ok(self, setup_db_otm_uni_sti):
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        engine, session, base = setup_db_otm_uni_sti

        child = tab_cfg.Child(name='Little Johnny')
        session.add_all([child])
        session.commit()

        assert repr(child) == '<Child(id=1 name=Little Johnny)>'
        pass

    def test_child_dunder_str_ok(self, setup_db_otm_uni_sti):
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        child = tab_cfg.Child(name='Little Johnny')

        assert str(child) == 'Little Johnny'
        pass


class TestSTI:
    def test_parent_sti(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        parent = tab_cfg.ParentSTI(name="John")
        session.add(parent)
        qry = session.query(tab_cfg.ParentSTI).filter_by(name="John").first()
        session.commit()

        assert parent.name == 'John'
        assert str(parent) == 'John'
        assert qry.name == 'John'
        pass

    def test_child_sti_with_parent(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        parent_sti = tab_cfg.ParentSTI(name="John")
        child_sti = tab_cfg.ChildSTI(name="Little Johnny", parent_id=parent_sti.id)
        session.add(parent_sti)
        session.add(child_sti)
        session.commit()

        assert parent_sti.name == 'John'
        assert str(parent_sti) == 'John'
        assert child_sti.name == 'Little Johnny'
        assert str(child_sti) == 'Little Johnny'
        pass

    def test_child_sti_no_parent(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        child_sti = tab_cfg.ChildSTI(name="Little Johnny", parent_id=1)
        session.add(child_sti)
        with pytest.raises(Exception) as e_info:
            session.commit()
        assert e_info.typename == 'IntegrityError'
        pass

    def test_parent_sti_dunder_repr_ok(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        parent_sti = tab_cfg.ParentSTI(name='John')
        session.add_all([parent_sti])
        session.commit()

        assert repr(parent_sti) == '<ParentSTI(id=1 name=John)>'
        pass

    def test_parent_sti_dunder_str_ok(self):
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        parent_sti = tab_cfg.ParentSTI(name='John')

        assert str(parent_sti) == 'John'
        pass

    def test_child_sti_dunder_repr_ok(self, setup_db_otm_uni_sti):
        engine, session, base = setup_db_otm_uni_sti
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        parent_sti = tab_cfg.ParentSTI(name='John')
        child_sti = tab_cfg.ChildSTI(name='Little Johnny', parent_id=parent_sti.id)
        session.add_all([child_sti])
        session.commit()

        assert repr(child_sti) == '<ChildSTI(id=1 name=Little Johnny parent_id=None)>'
        pass

    def test_child_sti_dunder_str_ok(self, setup_db_otm_uni_sti):
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        child_sti = tab_cfg.ChildSTI(name='Little Johnny')

        assert str(child_sti) == 'Little Johnny'
        pass
