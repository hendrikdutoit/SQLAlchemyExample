'''Testing sqlalchemyexample__init__()'''

from src import sqlalchemyexample


class TestSQLAlchemyExample:
    def test__init__(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_sqlalchemyexample = sqlalchemyexample.SQLAlchemyExample(env_setup.dir, True)

        assert t_sqlalchemyexample.success
        pass

    def step_01(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_sqlalchemyexample = sqlalchemyexample.SQLAlchemyExample(
            "SQLAlchemyExample", env_setup.dir
        )

        assert t_sqlalchemyexample.method_1()
        pass
