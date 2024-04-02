.. role:: raw-html(raw)
    :format: html


Conventions
===========

This document explains conventions and other important structural information.


File names
----------

#. Not knowing what's to come and what will be added, it is difficult to determine a naming convention for source, test and other file names.  The owner will therefore be a "benevolent dictator" to rename and change names.
#. Link the file name of the source code and the test so that it is easily linked.

Branch names
------------
"enhancement" | "bug" | "hotfix"/< ticket_nr>_<description>

where
    enhancement - Planned improvement or addition to functionality; non-urgent.

    bug - An error or defect causing incorrect or unexpected behavior; typically fixed in regular development cycles.

    hotfix - An urgent, critical fix applied directly to the live environment, often bypassing regular development cycles.

    ticket_nr: Ticket number assigned to the issue in GitHub.  Once an issue is registered, the owner will assign a ticket.

    description: GitHub issue title or combination of titles is more than one issue is addressed.

PEP 8
-----
`PEP 8 <https://peps.python.org/pep-0008/>`_ applies.  The maximum line length for text is relaxed to 120.

Ordering
-------
Attribute-, method-, class-, etc names are ordered alphabetically (where possible) within the local scope.  Should there
be a dependency, the item (stuff) are moved to the bottom, in alphabetical order, to accommodate the dependency.
