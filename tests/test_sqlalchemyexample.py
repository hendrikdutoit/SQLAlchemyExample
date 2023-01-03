'''Testing sqlalchemyexample__init__()'''

from src import sqlalchemyexample as sae
import src.sqlalchemyexample.one_to_many_bi as otmb


class TestSQLAlchemyExample:
    def test__init__(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_sqlalchemyexample = sae.DB(env_setup.dir)

        assert t_sqlalchemyexample.success
        pass

    def test_populate_user(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        db = sae.DB(env_setup.dir)
        session = db.session()
        user = otmb.User(name="ed", surname="Jones", nickname="edsnickname")
        session.add(user)
        qry = session.query(otmb.User).filter_by(name="ed").first()
        session.commit()

        assert user.name == 'ed'
        assert user.surname == 'Jones'
        assert user.nickname == 'edsnickname'
        assert str(user) == 'ed Jones'
        assert qry.name == 'ed'
        assert qry.surname == 'Jones'
        assert qry.nickname == 'edsnickname'
        assert str(qry) == 'ed Jones'
        pass

    def test_populate_user_address(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        db = sae.DB(env_setup.dir)
        session = db.session()
        user = otmb.User(name="jack", surname="Bean", nickname="gjffdd")
        user.addresses = [
            otmb.Address(email_address="jack@google.com"),
            otmb.Address(email_address="j25@yahoo.com"),
        ]
        session.add(user)
        qry = session.query(otmb.User).filter_by(name="jack").first()
        session.commit()

        assert user.name == 'jack'
        assert user.surname == 'Bean'
        assert user.nickname == 'gjffdd'
        assert str(user) == 'jack Bean'
        assert qry.name == 'jack'
        assert qry.surname == 'Bean'
        assert qry.nickname == 'gjffdd'
        # assert str(qry) ==
        pass
