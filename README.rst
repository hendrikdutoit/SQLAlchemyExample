.. image:: https://img.shields.io/pypi/status/SQLAlchemyExample
    :alt: PyPI - Status

.. image:: https://img.shields.io/pypi/wheel/SQLAlchemyExample
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/SQLAlchemyExample
    :alt: PyPI - Python Version

.. image:: https://img.shields.io/github/v/release/hendrikdutoit/SQLAlchemyExample
    :alt: GitHub release (latest by date)

.. image:: https://img.shields.io/github/license/hendrikdutoit/SQLAlchemyExample
    :alt: License

.. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/SQLAlchemyExample
    :alt: GitHub issues

.. image:: https://img.shields.io/pypi/dm/SQLAlchemyExample
    :alt: PyPI - Downloads

.. image:: https://img.shields.io/github/search/hendrikdutoit/SQLAlchemyExample/GitHub
    :alt: GitHub Searches

.. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/SQLAlchemyExample
    :alt: CodeCov
    :target: https://app.codecov.io/gh/hendrikdutoit/SQLAlchemyExample

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/SQLAlchemyExample/Pre-Commit
    :alt: GitHub Actions - Pre-Commit
    :target: https://github.com/hendrikdutoit/SQLAlchemyExample/actions/workflows/pre-commit.yaml

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/SQLAlchemyExample/CI
    :alt: GitHub Actions - CI
    :target: https://github.com/hendrikdutoit/SQLAlchemyExample/actions/workflows/ci.yaml

.. image:: https://img.shields.io/pypi/v/SQLAlchemyExample
    :alt: PyPi

Example for exploring SQLAlchemy

    This project provide code how to use AQLAlchemy. THis idea is to build an example sequentially in steps to give new users the idea on where to start and how to progress. Along the way some principles will be exhibited. The code should be self-explanatory without as little as possible documentation, else the project is failing. This example illustrate the following: -------------------------------------- 1. Establis a link to a MySQL or SQLite database 2. Create tables 3. Populate the tables 4. Configure a many--to-may relationship 5. Query the tables References ---------- - https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_many_to_many_relationships.htm - https://docs.sqlalchemy.org/en/13/orm/tutorial.html#building-a-relationship - https://cyruslab.net/2020/07/16/pythoncreate-database-if-not-exists-with-sqlalchemy/

=======
Testing
=======

This project uses ``pytest`` to run tests and also to test docstring examples.

Install the test dependencies.

.. code-block:: bash

    $ pip install -r requirements_test.txt

Run the tests.

.. code-block:: bash

    $ pytest tests
    === XXX passed in SSS seconds ===

==========
Developing
==========

This project uses ``black`` to format code and ``flake8`` for linting. We also support ``pre-commit`` to ensure these have been run. To configure your local environment please install these development dependencies and set up the commit hooks.

.. code-block:: bash

    $ pip install black flake8 pre-commit
    $ pre-commit install

=========
Releasing
=========

Releases are published automatically when a tag is pushed to GitHub.

.. code-block:: bash

    # Set next version number
    export RELEASE = x.x.x
    
    # Create tags
    git commit --allow -empty -m "Release $RELEASE"
    git tag -a $RELEASE -m "Version $RELEASE"
    
    # Push
    git push upstream --tags

