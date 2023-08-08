====================
Exploring SQLAlchemy
====================

+-------------------+---------------------------------------------------------------------------------------------+
| **General**       | |maintenance_y| |semver|                                                                    |
|                   +---------------------------------------------------------------------------------------------+
|                   | |license|                                                                                   |
+-------------------+---------------------------------------------------------------------------------------------+
| **CI**            | |gha_tests| |gha_docu| |pre_commit_ci|                                                      |
+-------------------+---------------------------------------------------------------------------------------------+
| **PyPI**          | |pypi_release| |pypi_py_versions| |pypi_status|                                             |
|                   +---------------------------------------------------------------------------------------------+
|                   | |pypi_format| |pypi_downloads|                                                              |
+-------------------+---------------------------------------------------------------------------------------------+
| **Github**        | |gh_issues| |gh_searches|                                                                   |
+-------------------+---------------------------------------------------------------------------------------------+


This project provide a sandbox to experiment with SQLAlchemy. This idea is to build an example sequentially in steps to give new users the idea on where to start and how to progress.

Along the way some principles will be exhibited. The code should be self-explanatory.

The source code in ``src`` by itself does not do much, it basically only defines the tables and some setup code.  The "examples" are in the the ``pytest's`` since we are experimenting to see howe it works and if it was successfull.

References:

- https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_many_to_many_relationships.htm
- https://docs.sqlalchemy.org/en/14/orm/tutorial.html#building-a-relationship
- https://cyruslab.net/2020/07/16/pythoncreate-database-if-not-exists-with-sqlalchemy/

Installation
------------
.. Detailed instructions on how to install, configure, and get the project running.

:Status: Work In Progress

1. Set the following environment variables:
2. Start Docker.  The ``docker-rebuild.bat`` script will git docker up and running.


Tests
-----

:Status: Work In Progress

This project uses ``pytest`` to run tests and also to test docstring examples.

Install the test dependencies.

.. code-block:: bash

    pip install -r requirements_test.txt

Run the tests.

Instructions about how to run tests.

Contributing
------------

.. Guidelines on how to contribute to this project.

:Status: Work In Progress

The setup and installation is for Windows.  Feel free to add contribute to get it running on Linux as well.

This project uses ``black`` to format code and ``flake8`` for linting. We also support ``pre-commit`` to ensure these have been run. To configure your local environment please install these development dependencies and set up the commit hooks.


.. code-block:: bash

    $ pip install black flake8 pre-commit
    $ pre-commit install


Releasing
---------

:Status: Work In Progress

Releases are published automatically when a tag is pushed to GitHub.

.. code-block:: bash

    # Set next version number
    export RELEASE = x.x.x

    # Create tags
    git commit --allow -empty -m "Release $RELEASE"
    git tag -a $RELEASE -m "Version $RELEASE"

    # Push
    git push upstream --tags

License
-------

:Status: Work In Progress

.. Information about the project's license.

Contact
-------
:Status: Work In Progress

.. General

.. |maintenance_n| image:: https://img.shields.io/badge/Maintenance%20Intended-✖-red.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - not intended

.. |maintenance_y| image:: https://img.shields.io/badge/Maintenance%20Intended-✔-green.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - intended

.. |license| image:: https://img.shields.io/github/license/hendrikdutoit/SQLAlchemyExample
    :target: https://github.com/hendrikdutoit/SQLAlchemyExample/blob/master/LICENSE
    :alt: License

.. |semver| image:: https://img.shields.io/badge/Semantic%20Versioning-2.0.0-brightgreen.svg?style=flat-square
    :target: https://semver.org/
    :alt: Semantic Versioning - 2.0.0


.. CI

.. |pre_commit_ci| image:: https://img.shields.io/github/actions/workflow/status/hendrikdutoit/SQLAlchemyExample/pre-commit.yml?label=pre-commit
    :target: https://github.com/hendrikdutoit/SQLAlchemyExample/blob/master/.github/workflows/pre-commit.yml
    :alt: Pre-Commit

.. |gha_tests| image:: https://img.shields.io/github/actions/workflow/status/hendrikdutoit/SQLAlchemyExample/ci.yml?label=ci
    :target: https://github.com/hendrikdutoit/SQLAlchemyExample/blob/master/.github/workflows/ci.yml
    :alt: Test status

.. |gha_docu| image:: https://img.shields.io/github/actions/workflow/status/hendrikdutoit/SQLAlchemyExample/check-documentation.yml?label=check rst
    :target: https://github.com/hendrikdutoit/SQLAlchemyExample/blob/master/.github/workflows/check-documentation.yml
    :alt: Documentation status

.. |codecov| image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/SQLAlchemyExample
    :target: https://app.codecov.io/gh/hendrikdutoit/SQLAlchemyExample
    :alt: CodeCov


.. PyPI

.. |pypi_release| image:: https://img.shields.io/pypi/v/SQLAlchemyExample
    :target: https://pypi.org/project/SQLAlchemyExample/
    :alt: PyPI - Package latest release

.. |pypi_py_versions| image:: https://img.shields.io/pypi/pyversions/SQLAlchemyExample
    :target: https://pypi.org/project/SQLAlchemyExample/
    :alt: PyPI - Supported Python Versions

.. |pypi_format| image:: https://img.shields.io/pypi/wheel/SQLAlchemyExample
    :target: https://pypi.org/project/SQLAlchemyExample/
    :alt: PyPI - Format

.. |pypi_downloads| image:: https://img.shields.io/pypi/dm/SQLAlchemyExample
    :target: https://pypi.org/project/SQLAlchemyExample/
    :alt: PyPI - Monthly downloads

.. |pypi_status| image:: https://img.shields.io/pypi/status/SQLAlchemyExample
    :target: https://pypi.org/project/SQLAlchemyExample/
    :alt: PyPI - Status


.. GitHub

.. |gh_issues| image:: https://img.shields.io/github/issues-raw/hendrikdutoit/SQLAlchemyExample
    :target: https://github.com/hendrikdutoit/SQLAlchemyExample/issues
    :alt: GitHub - Last Commit

.. |gh_searches| image:: https://img.shields.io/github/search/hendrikdutoit/SQLAlchemyExample/GitHub
    :alt: GitHub Searches
