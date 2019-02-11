etlam
-----

etlam is a basic structure for ETL projects.


Requirements
------------

You need the following:

1. A broker for Celery, e.g. Redis
2. Python


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
