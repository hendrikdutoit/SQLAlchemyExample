"""Testing sqlalchemyexample__init__()"""
import pytest
import db

# import default_tables as dt
import one_to_many_uni


@pytest.mark.otmuni
class OTMUni:
    def test_one_to_many_uni_parent(self, setup_db):
        parent = one_to_many_uni.ParentOTMUni(name="ed")
        db.session.add(parent)
        qry = (
            db.session.query(one_to_many_uni.ParentOTMUni).filter_by(name="ed").first()
        )
        db.session.commit()

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

    def test_one_to_many_bi_child_no_parent(self, setup_db):
        db = setup_db
        one_to_many_uni.Base.metadata.create_all(db.engine)
        session = db.session()
        child = one_to_many_uni.ChildOTMUni(name="eddie", parent_id=1)
        session.add(child)
        # with pytest.raises(Exception) as e_info:
        session.commit()
        # assert e_info.typename == 'IntegrityError'
        pass
