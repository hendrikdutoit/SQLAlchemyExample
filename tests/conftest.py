import pytest
from sqlalchemy.orm import close_all_sessions


@pytest.fixture
def setup_db_st():
    import simple_tables as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_otm_bi_sti():
    import otm_bi_single_table_inherit as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_otm_uni_sti():
    import otm_uni_single_table_inherit as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass
