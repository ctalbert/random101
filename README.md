Installation
============

>pip install django

Usage
=====
There are two custom manage.py commands:

* generate_couples
* import_past_101

generate_couples takes a filename as first argument and generate couples that can eventually be stored in the db. The file is expected to contain one name per line. An example file (names.txt) is stored in the repo.

import_past_101 takes a csv filename as first argument and generates a past meeting in the db. The csv filename should contain the names of each 101, one per line. An example file (past_101.csv) is included in the repo.