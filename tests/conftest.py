from datetime import date
from datetime import datetime
from os import environ

import pytest
import time_machine
from sqlalchemy.orm import close_all_sessions

ts_20240105_1330 = {
    'ts': datetime(2024, 1, 5, 13, 30),
    'ds': date(2024, 1, 5),
    'short_fmt': datetime(2024, 1, 5, 13, 30).strftime('%Y%m%d'),
    'long_fmt': datetime(2024, 1, 5, 13, 30).strftime('%Y-%m-%d'),
}


@pytest.fixture
def setup_db_mixin_declared_attr():
    environ['MYSQL_DATABASE'] = 'mixin_declared_attr'

    from inheritance import mixin_declared_attr as tab_cfg

    tab_cfg.Base.metadata.drop_all()
    tab_cfg.Base.metadata.create_all()
    yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
    close_all_sessions()
    pass


@pytest.fixture
def setup_db_mixin_column():
    environ['MYSQL_DATABASE'] = 'mixin_column'

    with time_machine.travel(ts_20240105_1330['ts']):
        from inheritance import mixin_column as tab_cfg

        tab_cfg.Base.metadata.drop_all()
        tab_cfg.Base.metadata.create_all()
        yield tab_cfg.engine, tab_cfg.session, tab_cfg.Base
        close_all_sessions()
    pass


@pytest.fixture
def setup_db_mixin_simple():
    environ['MYSQL_DATABASE'] = 'mixin_simple'
    from inheritance import mixin_simple as tab_cfg

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
