'''Testing sqlalchemyexample__init__()'''
import pytest
import one_to_many_uni
import one_to_many_bi


class TestSQLAlchemyExample:
    def test__init__(self, setup_db):
        """Assert class __init__"""
        db = setup_db

        assert db.success
        assert db.engine.url[0] == 'mysql+mysqlconnector'
        assert db.engine.url[1] == 'root'
        assert db.engine.url[2] == 'N0tS0S3curePassw0rd'
        assert db.engine.url[3] == 'localhost'
        assert db.engine.url[4] == 50002
        assert db.engine.url[5] == 'SQLAlchemyExample'
        pass

    def test_one_to_many_bi_parent(self, setup_db):
        db = setup_db
        one_to_many_bi.Base.metadata.create_all(db.engine)
        session = db.session()
        parent = one_to_many_bi.ParentOTMBi(name="ed")
        session.add(parent)
        qry = session.query(one_to_many_bi.ParentOTMBi).filter_by(name="ed").first()
        session.commit()

        assert parent.name == 'ed'
        assert str(parent) == 'ed'
        assert qry.name == 'ed'
        pass

    def test_one_to_many_bi_child_with_parent(self, setup_db):
        db = setup_db
        one_to_many_bi.Base.metadata.create_all(db.engine)
        session = db.session()
        parent = one_to_many_bi.ParentOTMBi(name="ed")
        child = one_to_many_bi.ChildOTMBi(name="eddie", parent_id=1)
        session.add(parent)
        session.add(child)
        session.commit()

        assert parent.name == 'ed'
        assert str(parent) == 'ed'
        assert child.name == 'eddie'
        assert str(child) == 'eddie'
        pass

    def test_one_to_many_bi_child_no_parent(self, setup_db):
        db = setup_db
        one_to_many_bi.Base.metadata.create_all(db.engine)
        session = db.session()
        child = one_to_many_bi.ChildOTMBi(name="eddie", parent_id=1)
        session.add(child)
        with pytest.raises(Exception) as e_info:
            session.commit()
        assert e_info.typename == 'IntegrityError'
        pass

    def test_one_to_many_uni_parent(self, setup_db):
        db = setup_db
        one_to_many_uni.Base.metadata.create_all(db.engine)
        session = db.session()
        parent = one_to_many_uni.ParentOTMUni(name="ed")
        session.add(parent)
        qry = session.query(one_to_many_uni.ParentOTMUni).filter_by(name="ed").first()
        session.commit()

        assert parent.name == 'ed'
        assert str(parent) == 'ed'
        assert qry.name == 'ed'
        pass

    def test_one_to_many_uni_child_with_parent(self, setup_db):
        db = setup_db
        one_to_many_uni.Base.metadata.create_all(db.engine)
        session = db.session()
        parent = one_to_many_uni.ParentOTMUni(name="ed")
        child = one_to_many_uni.ChildOTMUni(name="eddie", parent_id=1)
        session.add(parent)
        session.add(child)
        session.commit()

        assert parent.name == 'ed'
        assert str(parent) == 'ed'
        assert child.name == 'eddie'
        assert str(child) == 'eddie'
        pass

    def test_one_to_many_bi_child_no_parent_2(self, setup_db):
        db = setup_db
        one_to_many_uni.Base.metadata.create_all(db.engine)
        session = db.session()
        child = one_to_many_uni.ChildOTMUni(name="eddie", parent_id=1)
        session.add(child)
        # with pytest.raises(Exception) as e_info:
        session.commit()
        # assert e_info.typename == 'IntegrityError'
        pass
