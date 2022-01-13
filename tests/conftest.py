'''Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
'''
from pathlib import Path
import pytest
from tempfile import mkdtemp
from beetools import rm_tree

# from github import Github, GithubException as gh_exc

_DESC = __doc__.split('\n')[0]
_PATH = Path(__file__)


# _CLASSIFIERS = [
#     'Development Status :: 1 - Planning',
#     'Intended Audience :: Developers',
#     'Intended Audience :: System Administrators',
#     'Topic :: Software Development',
#     'Topic :: System :: Systems Administration',
#     'License :: OSI Approved :: MIT License',
#     'Programming Language :: Python :: 3.0',
#     'Programming Language :: Python :: 3.9',
#     'Programming Language :: Python :: 3.10',
# ]
# _INDEX_RST_BADGE_CODECOV = \
# '''.. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/sqlalchemyexample
#     :alt: CodeCov
#     :target: https://app.codecov.io/gh/hendrikdutoit/sqlalchemyexample
#
# '''
# _INDEX_RST_BADGE_GITHUB_CI = \
# '''.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/sqlalchemyexample/CI
#     :alt: GitHub Actions - CI
#     :target: https://github.com/hendrikdutoit/sqlalchemyexample/actions/workflows/ci.yaml
#
# '''
# _INDEX_RST_BADGE_GITHUB_HITS = \
# '''.. image:: https://img.shields.io/github/search/hendrikdutoit/sqlalchemyexample/GitHub hit
#     :alt: GitHub Searches
#
# '''
# _INDEX_RST_BADGE_GITHUB_LICENSE = \
# '''.. image:: https://img.shields.io/github/license/hendrikdutoit/sqlalchemyexample
#     :alt: License
#
# '''
# _INDEX_RST_BADGE_GITHUB_ISSUES = \
# '''.. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/sqlalchemyexample
#     :alt: GitHub issues
#
# '''
# _INDEX_RST_BADGE_GITHUB_PRE_COMMIT = \
# '''.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/sqlalchemyexample/Pre-Commit
#     :alt: GitHub Actions - Pre-Commit
#     :target: https://github.com/hendrikdutoit/sqlalchemyexample/actions/workflows/pre-commit.yaml
#
# '''
# _INDEX_RST_BADGE_GITHUB_RELEASE = \
# '''.. image:: https://img.shields.io/github/v/release/hendrikdutoit/sqlalchemyexample
#     :alt: GitHub release (latest by date)
#
# '''
# _INDEX_RST_BADGE_PYPI_VERSION = \
# '''.. image:: https://img.shields.io/testpypi/v/sqlalchemyexample
#     :alt: PyPi
#
# '''
# _INDEX_RST_BADGE_PYPI_DL = \
# '''.. image:: https://img.shields.io/pypi/dm/sqlalchemyexample
#     :alt: PyPI - Downloads
#
# '''
# _INDEX_RST_BADGE_PYPI_STATUS = \
# '''.. image:: https://img.shields.io/pypi/status/sqlalchemyexample
#     :alt: PyPI - Status
#
# '''
# _INDEX_RST_BADGE_PYPI_WHEEL = \
# '''.. image:: https://img.shields.io/pypi/wheel/sqlalchemyexample
#     :alt: PyPI - Wheel
#
# '''
# _INDEX_RST_BADGE_PYVERSIONS = \
# '''.. image:: https://img.shields.io/pypi/pyversions/sqlalchemyexample
#     :alt: PyPI - Python Version
#
# '''
# _INDEX_RST_CONTENTS = '''.. ======================================================
# .. This file is auto generated by PackageIt. Any changes
# .. to it will be over written
# .. ======================================================
#
# ================================
# sqlalchemyexample
# ================================
#
# .. image:: https://img.shields.io/pypi/status/sqlalchemyexample
#     :alt: PyPI - Status
#
# .. image:: https://img.shields.io/pypi/wheel/sqlalchemyexample
#     :alt: PyPI - Wheel
#
# .. image:: https://img.shields.io/pypi/pyversions/sqlalchemyexample
#     :alt: PyPI - Python Version
#
# .. image:: https://img.shields.io/github/v/release/hendrikdutoit/sqlalchemyexample
#     :alt: GitHub release (latest by date)
#
# .. image:: https://img.shields.io/github/license/hendrikdutoit/sqlalchemyexample
#     :alt: License
#
# .. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/sqlalchemyexample
#     :alt: GitHub issues
#
# .. image:: https://img.shields.io/pypi/dm/sqlalchemyexample
#     :alt: PyPI - Downloads
#
# .. image:: https://img.shields.io/github/search/hendrikdutoit/sqlalchemyexample/GitHub hit
#     :alt: GitHub Searches
#
# .. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/sqlalchemyexample
#     :alt: CodeCov
#     :target: https://app.codecov.io/gh/hendrikdutoit/sqlalchemyexample
#
# .. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/sqlalchemyexample/Pre-Commit
#     :alt: GitHub Actions - Pre-Commit
#     :target: https://github.com/hendrikdutoit/sqlalchemyexample/actions/workflows/pre-commit.yaml
#
# .. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/sqlalchemyexample/CI
#     :alt: GitHub Actions - CI
#     :target: https://github.com/hendrikdutoit/sqlalchemyexample/actions/workflows/ci.yaml
#
# .. image:: https://img.shields.io/testpypi/v/sqlalchemyexample
#     :alt: PyPi
#
# Project Header Description (default ini)
#
#     Project long description goes in here (default ini)
#
# ------------
# Installation
# ------------
#
# .. code-block:: bash
#
#     $ pip install .
#
# -----
# Usage
# -----
#
# .. code-block:: bash
#
#     Insert text in Usage.rst
#
# -------
# Support
# -------
#
# .. code-block:: bash
#
#     Insert text in Support.rst
#
# .. toctree::
#     :maxdepth: 2
#     :caption: Contents
#     :numbered:
#
#     conventions
#     api
#     donotexist
#
# '''
# _PROJECT_CLASSIFIERS = [
#     'Development Status :: 1 - Planning',
#     'Intended Audience :: Developers',
#     'Topic :: Software Development',
#     'License :: OSI Approved :: MIT License',
#     'Programming Language :: Python :: 3.0',
#     'Programming Language :: Python :: 3.10',
# ]


_PROJECT_NAME = "sqlalchemyexample"
_RELEASE_YAML_PROD = '''name: Build distribution

on: [push, pull_request]

jobs:
  ReleaseToPyPi:
    runs-on: "ubuntu-latest"

    steps:
      - name: Checkout source
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        uses: actions/setup-python@v1
        with:
          python-version: 3.9

      - name: Install build dependencies
        run: python -m pip install build wheel

      - name: Build distributions
        shell: bash -l sqlalchemyexample
        run: python setup.py sdist bdist_wheel

      - name: Publish package to PyPI
        uses: pypa/gh-action-pypi-publish@master
        with:
          user: __token__
          password: ${{ secrets.PYPI_API_TOKEN }}
          repository_url: https://upload.pypi.org/legacy/
          verbose: true
'''
_RELEASE_YAML_TEST = '''name: Build distribution

on: [push, pull_request]

jobs:
  ReleaseToPyPi:
    runs-on: "ubuntu-latest"

    steps:
      - name: Checkout source
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        uses: actions/setup-python@v1
        with:
          python-version: 3.9

      - name: Install build dependencies
        run: python -m pip install build wheel

      - name: Build distributions
        shell: bash -l sqlalchemyexample
        run: python setup.py sdist bdist_wheel

      - name: Publish package to PyPI
        uses: pypa/gh-action-pypi-publish@master
        with:
          user: __token__
          password: ${{ secrets.TEST_PYPI_API_TOKEN }}
          repository_url: https://test.pypi.org/legacy/
          verbose: true
'''


class WorkingDir:
    def __init__(self):
        self.dir = Path(mkdtemp(prefix='packageit_'))


class EnvSetUp:
    def __init__(self, p_make_project_ini=False):
        self.dir = WorkingDir().dir
        self.external_arc_dir = self.dir / 'external_archive'
        self.external_arc_dir.mkdir(parents=True)
        self.project_ini_pth = None


@pytest.fixture
def env_setup_self_destruct():
    '''Set up the environment base structure'''
    setup_env = EnvSetUp()
    yield setup_env
    rm_tree(setup_env.dir, p_crash=False)


@pytest.fixture
def env_setup_with_project_ini_self_destruct():
    '''Set up the environment base structure'''
    setup_env = EnvSetUp(p_make_project_ini=True)
    yield setup_env
    rm_tree(setup_env.dir, p_crash=False)


@pytest.fixture
def working_dir_self_destruct():
    '''Set up the environment base structure'''
    working_dir = WorkingDir()
    yield working_dir
    rm_tree(working_dir.dir, p_crash=False)
