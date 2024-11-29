Orange County Lettings documentation
====================================

.. important::

   This project is a scholar exercise developed in response to a specific scenario.
   It is not designed for direct use in production.


.. image:: _static/logo_OCL.png
   :alt: Logo Orange County Lettings
   :align: center


Introduction
============


Welcome to the homepage of the **Orange County Lettings** documentation, a web application designed to manage lettings.  

This project is primarily developed in Python (3.12) using the Django framework.

The application uses several other tools and libraries:

- **Database**: SQLite3

- **Linting**: Flake8

- **Monitoring**: Sentry, for tracking errors and performances

- **Testing**:  Coverage for test coverage and SonarCloud for code quality/security reports

- **Documentation**: Sphinx/Read the Docs for generating and hosting the doc

- **Deployment**: Docker, Gunicorn, GitHub Actions, and Render


This documentation covers installation (dev and deployement), configuration, user guide and source code details.


The source code is available here: https://github.com/Mothraa/Python-OC-Lettings-FR


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   quickstart
   installation
   user_guide
   technical_doc
   deployement


Index and tables
================

* :ref:`genindex`
