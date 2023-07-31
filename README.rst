.. image:: https://img.shields.io/pypi/status/SQLAlchemyExample
    :alt: PyPI - Status

.. image:: https://img.shields.io/pypi/wheel/SQLAlchemyExample
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/SQLAlchemyExample
    :alt: PyPI - Python Version

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

.. image:: https://img.shields.io/github/actions/workflow/status/hendrikdutoit/SQLAlchemyExample/pre-commit.yaml?label=pre-commit
    :alt: GitHub Workflow Status (with event)

.. image:: https://img.shields.io/github/actions/workflow/status/hendrikdutoit/SQLAlchemyExample/ci.yaml?label=ci
    :alt: GitHub Workflow Status (with event)

.. image:: https://img.shields.io/pypi/v/SQLAlchemyExample
    :alt: PyPi

====================
Exploring SQLAlchemy
====================

    This project provide a sandbox to experiment with SQLAlchemy. This idea is to build an example sequentially in steps to give new users the idea on where to start and how to progress.

    Along the way some principles will be exhibited. The code should be self-explanatory.

    The source code in ``src`` by itself does not do much, it basically only defines the tables and some setup code.  The "examples" are in the the ``pytest's`` since we are experimenting to see howe it works and if it was successfull.


    References:

    - https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_many_to_many_relationships.htm
    - https://docs.sqlalchemy.org/en/14/orm/tutorial.html#building-a-relationship
    - https://cyruslab.net/2020/07/16/pythoncreate-database-if-not-exists-with-sqlalchemy/

==================
Get Up-and-Running
==================

    1. Set the following environment variables:
::

$ SET XYZ=DEF
$

    2. Start Docker.  The ``docker-rebuild.bat`` script will git docker up and running.
    3. dasd

``pytest``

=======
Testing
=======

This project uses ``pytest`` to run tests and also to test docstring examples.

Install the test dependencies.

.. code-block::bash

    $ pip install -r requirements_test.txt




Run the tests.

.. code-block:: bash

    $ pytest tests
    === XXX passed in SSS seconds ===

==========
Developing
==========
    The setup and installation is for Windows.  Feel free to add contribute to get it running on Linux as well.

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
