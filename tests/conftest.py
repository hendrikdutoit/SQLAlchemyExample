'''Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
'''
from pathlib import Path
import pytest
from tempfile import mkdtemp
from beetools import rm_tree


class WorkingDir:
    def __init__(self):
        self.dir = Path(mkdtemp(prefix='sqlalchemy_'))


class EnvSetUp:
    def __init__(self, p_make_project_ini=False):
        self.dir = WorkingDir().dir


@pytest.fixture
def env_setup_self_destruct():
    '''Set up the environment base structure'''
    setup_env = EnvSetUp()
    yield setup_env
    rm_tree(setup_env.dir, p_crash=False)
