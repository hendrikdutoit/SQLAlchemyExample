"""Testing sqlalchemyexample__init__()"""
import pytest
from sqlalchemy import inspect


class TestEx03Simple:
    def test_tables_exist(self, setup_db_03_01):
        engine, session, base = setup_db_03_01

        inspector = inspect(engine)
        assert 'login' in inspector.get_table_names()
        assert 'child' in inspector.get_table_names()

    def test_login(self, setup_db_03_01):
        engine, session, base = setup_db_03_01
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        login = tab_cfg.LogIn(email='john@somewhere.com')
        session.add(login)
        qry = session.query(tab_cfg.LogIn).filter_by(email='john@somewhere.com').first()
        session.commit()

        assert login.email == 'john@somewhere.com'
        assert str(login) == 'john@somewhere.com'
        assert qry.email == 'john@somewhere.com'
        pass

    def test_login_dunder_repr_ok(self, setup_db_03_01):
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        engine, session, base = setup_db_03_01

        login = tab_cfg.LogIn(email='john@somewhere.com')
        session.add_all([login])
        session.commit()

        assert repr(login) == '<Parent(id=1 email=john@somewhere.com)>'
        pass

    def test_login_dunder_str_ok(self, setup_db_03_01):
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        login = tab_cfg.LogIn(email='john@somewhere.com')

        assert str(login) == 'john@somewhere.com'
        pass

    def test_child(self, setup_db_03_01):
        engine, session, base = setup_db_03_01
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        child = tab_cfg.LogIn(name='Little Johnny')
        session.add(child)
        qry = session.query(tab_cfg.LogIn).filter_by(name='Little Johnny').first()
        session.commit()

        assert child.email == 'Little Johnny'
        assert str(child) == 'Little Johnny'
        assert qry.email == 'Little Johnny'
        pass

    def test_child_dunder_repr_ok(self, setup_db_03_01):
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        engine, session, base = setup_db_03_01

        child = tab_cfg.Child(name='Little Johnny')
        session.add_all([child])
        session.commit()

        assert repr(child) == '<Child(id=1 name=Little Johnny)>'
        pass

    def test_child_dunder_str_ok(self, setup_db_03_01):
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        child = tab_cfg.Child(name='Little Johnny')

        assert str(child) == 'Little Johnny'
        pass


class TestEx0300:
    def test_parent_sti(self, setup_db_03_01):
        engine, session, base = setup_db_03_01
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        parent = tab_cfg.ParentSTI(name="John")
        session.add(parent)
        qry = session.query(tab_cfg.ParentSTI).filter_by(name="John").first()
        session.commit()

        assert parent.email == 'John'
        assert str(parent) == 'John'
        assert qry.email == 'John'
        pass

    def test_child_sti_with_parent(self, setup_db_03_01):
        engine, session, base = setup_db_03_01
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        parent_sti = tab_cfg.ParentSTI(name="John")
        child_sti = tab_cfg.ChildSTI(name="Little Johnny", parent_id=parent_sti.id)
        session.add(parent_sti)
        session.add(child_sti)
        session.commit()

        assert parent_sti.email == 'John'
        assert str(parent_sti) == 'John'
        assert child_sti.name == 'Little Johnny'
        assert str(child_sti) == 'Little Johnny'
        pass

    def test_child_sti_no_parent(self, setup_db_03_01):
        engine, session, base = setup_db_03_01
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        child_sti = tab_cfg.ChildSTI(name="Little Johnny", parent_id=1)
        session.add(child_sti)
        with pytest.raises(Exception) as e_info:
            session.commit()
        assert e_info.typename == 'IntegrityError'
        pass

    def test_parent_sti_dunder_repr_ok(self, setup_db_03_01):
        engine, session, base = setup_db_03_01
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        parent_sti = tab_cfg.ParentSTI(name='John')
        session.add_all([parent_sti])
        session.commit()

        assert repr(parent_sti) == '<ParentSTI(id=1 name=John)>'
        pass

    def test_parent_sti_dunder_str_ok(self):
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        parent_sti = tab_cfg.ParentSTI(name='John')

        assert str(parent_sti) == 'John'
        pass

    def test_child_sti_dunder_repr_ok(self, setup_db_03_01):
        engine, session, base = setup_db_03_01
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        parent_sti = tab_cfg.ParentSTI(name='John')
        child_sti = tab_cfg.ChildSTI(name='Little Johnny', parent_id=parent_sti.id)
        session.add_all([child_sti])
        session.commit()

        assert repr(child_sti) == '<ChildSTI(id=1 name=Little Johnny parent_id=None)>'
        pass

    def test_child_sti_dunder_str_ok(self, setup_db_03_01):
        import ex03_01_otm_uni_single_table_inherit as tab_cfg

        child_sti = tab_cfg.ChildSTI(name='Little Johnny')

        assert str(child_sti) == 'Little Johnny'
        pass


class TestEx0301:
    def test_login(self, setup_db_03_00):
        engine, session, base = setup_db_03_00
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        login = tab_cfg.LogIn(email="john@somewhere.com")
        session.add(login)
        qry = session.query(tab_cfg.LogIn).filter_by(email="john@somewhere.com").first()
        session.commit()

        assert login.email == 'john@somewhere.com'
        assert str(login) == 'john@somewhere.com'
        assert qry.email == 'john@somewhere.com'
        pass

    def test_person(self, setup_db_03_00):
        engine, session, base = setup_db_03_00
        import ex03_00_otm_uni_single_table_inherit as tab_cfg

        person = tab_cfg.Person(
            email="john@somewhere.com", name='john@somewhere.com', surname='Doe'
        )
        session.add(person)
        qry = session.query(tab_cfg.LogIn).filter_by(email="john@somewhere.com").first()
        session.commit()

        assert person.email == 'john@somewhere.com'
        assert str(person) == 'john@somewhere.com'
        assert qry.email == 'john@somewhere.com'
        pass
