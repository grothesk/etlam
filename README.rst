etlam
-----

etlam is a basic structure for ETL projects - it supports parallel processing of files and provides comfortable handling via the command line. 


Requirements
------------

You'll need the following:

0. Python
1. A DBMS, e.g. PostgreSQL
2. A broker for Celery, e.g. Redis

Run etlam
---------

0. Install etlam, e.g. via pip.
1. Start Broker, e.g. Redis.
2. Run celery, e.g. like this

.. code-block:: bash

  $ celery -A etlam.utils.jobs --loglevel=info -Ofair


3. Run etlam like this

.. code-block:: bash

  $ etlam run-etl my_folder

