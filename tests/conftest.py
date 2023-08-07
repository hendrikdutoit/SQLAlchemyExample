from os import environ
import pytest
from sqlalchemy.orm import close_all_sessions


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
    environ['MYSQL_DB_NAME'] = 'ex02_00_otm_bi_single_table_inherit'
    import ex02_00_otm_bi_single_table_inherit as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def sti():
    environ['MYSQL_DB_NAME'] = 'ex03_00_sti'
    import sti as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_otm_uni_sti():
    environ['MYSQL_DB_NAME'] = 'ex03_00_sti_otm_uni'
    import otm_uni_sti as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass
