from os import environ

import pytest
from sqlalchemy.orm import close_all_sessions


@pytest.fixture
def setup_db_mixin():
    environ['MYSQL_DATABASE'] = 'mixin'
    from inheritance import mixin as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_otm_bi():
    # import pdb;pdb.set_trace()
    environ['MYSQL_DATABASE'] = 'otm_bi'
    from directional import otm_bi as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_otm_uni():
    environ['MYSQL_DATABASE'] = 'otm_uni'
    from directional import otm_uni as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_otm_bi_sti():
    environ['MYSQL_DATABASE'] = 'otm_bi_sti'
    from inheritance import otm_bi_sti as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_simple():
    environ['MYSQL_DATABASE'] = 'simple'
    from simple import simple as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_sti():
    environ['MYSQL_DATABASE'] = 'sti'
    from inheritance import sti as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass
