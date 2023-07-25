import pytest
from sqlalchemy.orm import close_all_sessions


@pytest.fixture
def setup_db_st():
    import simple_tables as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    # import pdb;pdb.set_trace()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_otm_bi_sti():
    import one_to_many_bi_single_table_inheritance as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    # import pdb;pdb.set_trace()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_otm_uni_sti():
    import one_to_many_uni_single_table_inheritance as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    # import pdb;pdb.set_trace()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass
