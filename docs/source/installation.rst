Installation & dev environment
==============================

This part of the documentation describes how to install the local development environment.

Prerequisites
-------------

- GitHub account with access to the repository: https://github.com/Mothraa/Python-OC-Lettings-FR
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher


Clone the Repository
--------------------

.. code-block:: bash

   cd /path/to/put/project/in
   git clone git@github.com:Mothraa/Python-OC-Lettings-FR.git

Create the Virtual Environment
------------------------------

macOS / Linux
^^^^^^^^^^^^^
.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   python -m venv venv
   apt-get install python3-venv  # if the previous step fails due to a missing package on Ubuntu
   source venv/bin/activate

Windows
^^^^^^^

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   python -m venv venv
   venv/scripts/activate


Other usefull commands
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   which python  # confirm the `python command` used (in the virtual environment)
   python --version  # confirm the Python version
   which pip  # confirm the `pip command` used (in the virtual environment)
   deactivate  # to close/deactivate the environment

On Windows powershell, replace ``which <my-command>`` with ``(Get-Command <my-command>).Path``

Environment Variables
---------------------
The application requires environment variables.

These variables should be stored in a `.env` file. Here is a file structure example:

.. code-block:: ini

   ENV="development"  # "production" for deployement
   # DJANGO
   DJANGO_SECRET_KEY="my_django_secret_key"
   DEBUG=True
   DEV_DATABASE_PATH="oc-lettings-site.sqlite3"
   RENDER_URL="https://oc-lettings-site-hlhz.onrender.com"

   # SENTRY
   SENTRY_DSN="my_sentry_secret_key"
   SENTRY_DEBUG=False

Replace the secret key values `DJANGO_SECRET_KEY` or `SENTRY_DSN` with yours!


Run the web app
---------------

macOS / Linux
^^^^^^^^^^^^^

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   source venv/bin/activate
   pip install --requirement requirements.txt
   python manage.py runserver

Windows
^^^^^^^

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   venv/scripts/activate
   pip install --requirement requirements.txt
   python manage.py runserver


Open `http://localhost:8080` in a web browser.


Linting
-------

.. code-block:: bash

   flake8

Unit Tests
----------

.. code-block:: bash

   pytest

Coverage
--------

To generate and check code coverage, use the commands:

.. code-block:: bash

   coverage run -m pytest  # run tests with coverage
   coverage report         # Display the coverage report in the terminal
   coverage html           # Generate an HTML report

You can open the HTML report : `htmlcov/index.html` in your web browser.
