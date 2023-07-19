import pytest
import db


@pytest.fixture
def setup_db():
    db.Base.metadata.drop_all()
    db.Base.metadata.create_all()
    yield db.session.is_active
    db.Session.close_all()
    pass
