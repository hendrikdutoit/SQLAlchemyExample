import pytest
from sqlalchemy.orm import close_all_sessions
import default_tables as dt


@pytest.fixture
def setup_db():
    dt.Base.metadata.drop_all()
    #     # import pdb;pdb.set_trace()
    dt.Base.metadata.create_all()
    yield dt.engine, dt.session, dt.Base
    # db.session.close_all()
    close_all_sessions()
    pass
