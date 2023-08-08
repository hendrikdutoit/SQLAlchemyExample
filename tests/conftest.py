from os import environ
import pytest
from sqlalchemy.orm import close_all_sessions


@pytest.fixture
def setup_db_otm_bi():
    environ['MYSQL_DB_NAME'] = 'otm_bi'
    import otm_bi as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_otm_uni():
    environ['MYSQL_DB_NAME'] = 'otm_uni'
    import otm_uni as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_otm_bi_sti():
    environ['MYSQL_DB_NAME'] = 'otm_bi_sti'
    import otm_bi_sti as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_simple():
    environ['MYSQL_DB_NAME'] = 'simple'
    import simple as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_sti():
    environ['MYSQL_DB_NAME'] = 'ex03_00_sti'
    import sti as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass
