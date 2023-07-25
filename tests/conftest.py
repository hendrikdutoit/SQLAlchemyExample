import pytest
import db_connection as dbc
from sqlalchemy.orm import close_all_sessions

# import default_tables as dt


@pytest.fixture
def setup_db():
    dbc.Base.metadata.drop_all()
    # import pdb;pdb.set_trace()
    dbc.Base.metadata.create_all()
    yield dbc.session.is_active
    # db.session.close_all()
    close_all_sessions()
    pass
