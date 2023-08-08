+-------------------+---------------------------------------------------------------------------------------------+
| **General**       | |maintenance_y| |semver|                                                                    |
|                   +---------------------------------------------------------------------------------------------+
|                   | |license|                                                                                   |
+-------------------+---------------------------------------------------------------------------------------------+
| **CI**            | |gha_tests| |gha_docu| |gha_qa| |pre_commit_ci|                                             |
+-------------------+---------------------------------------------------------------------------------------------+
| **PyPI**          | |pypi_release| |pypi_py_versions| |pypi_implementations|                                    |
|                   +---------------------------------------------------------------------------------------------+
|                   | |pypi_format| |pypi_downloads|                                                              |
+-------------------+---------------------------------------------------------------------------------------------+
| **Github**        | |gh_tag| |gh_last_commit|                                                                   |
|                   +---------------------------------------------------------------------------------------------+
|                   | |gh_stars| |gh_forks| |gh_contributors| |gh_watchers|                                       |
+-------------------+---------------------------------------------------------------------------------------------+


.. image:: https://img.shields.io/pypi/status/SQLAlchemyExample
    :alt: PyPI - Status

.. image:: https://img.shields.io/pypi/wheel/SQLAlchemyExample
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/SQLAlchemyExample
    :alt: PyPI - Python Version

.. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/SQLAlchemyExample
    :alt: GitHub issues

.. image:: https://img.shields.io/pypi/dm/SQLAlchemyExample
    :alt: PyPI - Downloads

.. image:: https://img.shields.io/github/search/hendrikdutoit/SQLAlchemyExample/GitHub
    :alt: GitHub Searches

.. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/SQLAlchemyExample
    :alt: CodeCov
    :target: https://app.codecov.io/gh/hendrikdutoit/SQLAlchemyExample

.. image:: https://img.shields.io/github/actions/workflow/status/hendrikdutoit/SQLAlchemyExample/pre-commit.yml?label=pre-commit
    :alt: Pre-Commit

.. image:: https://img.shields.io/pypi/v/SQLAlchemyExample
    :alt: PyPi

Exploring SQLAlchemy
=================

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

.. |gha_tests| image:: https://img.shields.io/github/actions/workflow/status/hendrikdutoit/SQLAlchemyExample/ci.yml?label=ci
    :target: https://github.com/hendrikdutoit/SQLAlchemyExample/blob/master/.github/workflows/ci.yml
    :alt: Test status

.. |gha_docu| image:: https://img.shields.io/github/actions/workflow/status/rstcheck/rstcheck/documentation.yml?branch=main&style=flat-square&logo=github&label=Test%20documentation
    :target: https://github.com/rstcheck/rstcheck/actions/workflows/documentation.yaml
    :alt: Documentation status

.. |gha_qa| image:: https://img.shields.io/github/actions/workflow/status/rstcheck/rstcheck/qa.yml?branch=main&style=flat-square&logo=github&label=QA
    :target: https://github.com/rstcheck/rstcheck/actions/workflows/qa.yaml
    :alt: QA status

.. |pre_commit_ci| image:: https://results.pre-commit.ci/badge/github/rstcheck/rstcheck/main.svg
    :target: https://results.pre-commit.ci/latest/github/rstcheck/rstcheck/main
    :alt: pre-commit status


.. PyPI

.. |pypi_release| image:: https://img.shields.io/pypi/v/rstcheck.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/rstcheck/
    :alt: PyPI - Package latest release

.. |pypi_py_versions| image:: https://img.shields.io/pypi/pyversions/rstcheck.svg?style=flat-square&logo=python&logoColor=FBE072
    :target: https://pypi.org/project/rstcheck/
    :alt: PyPI - Supported Python Versions

.. |pypi_implementations| image:: https://img.shields.io/pypi/implementation/rstcheck.svg?style=flat-square&logo=python&logoColor=FBE072
    :target: https://pypi.org/project/rstcheck/
    :alt: PyPI - Supported Implementations

.. |pypi_format| image:: https://img.shields.io/pypi/format/rstcheck.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/rstcheck/
    :alt: PyPI - Format

.. |pypi_downloads| image:: https://img.shields.io/pypi/dm/rstcheck.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/rstcheck/
    :alt: PyPI - Monthly downloads



.. GitHub

.. |gh_tag| image:: https://img.shields.io/github/v/tag/rstcheck/rstcheck.svg?sort=semver&style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck/tags
    :alt: Github - Latest Release

.. |gh_last_commit| image:: https://img.shields.io/github/last-commit/rstcheck/rstcheck.svg?style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck/commits/main
    :alt: GitHub - Last Commit

.. |gh_stars| image:: https://img.shields.io/github/stars/rstcheck/rstcheck.svg?style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck/stargazers
    :alt: Github - Stars

.. |gh_forks| image:: https://img.shields.io/github/forks/rstcheck/rstcheck.svg?style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck/network/members
    :alt: Github - Forks

.. |gh_contributors| image:: https://img.shields.io/github/contributors/rstcheck/rstcheck.svg?style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck/graphs/contributors
    :alt: Github - Contributors

.. |gh_watchers| image:: https://img.shields.io/github/watchers/rstcheck/rstcheck.svg?style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck/watchers/
    :alt: Github - Watchers
