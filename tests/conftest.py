from os import environ
import pytest
from sqlalchemy.orm import close_all_sessions


@pytest.fixture
def setup_db_simple():
    environ['MYSQL_DB_NAME'] = 'ex01_00_simple'
    import ex01_00_simple as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_ex_02_00():
    environ['MYSQL_DB_NAME'] = 'ex02_00_otm_bi_single_table_inherit'
    import ex02_00_otm_bi_single_table_inherit as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_03_00():
    environ['MYSQL_DB_NAME'] = 'ex03_00_otm_uni_single_table_inherit'
    import ex03_00_otm_uni_single_table_inherit as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_03_01():
    environ['MYSQL_DB_NAME'] = 'ex03_01_otm_uni_single_table_inherit'
    import ex03_01_otm_uni_single_table_inherit as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass
