Quickstart
==========

This guide helps you quickly start the **Orange County Lettings** app using Docker.

Install docker
--------------

https://docs.docker.com/get-started/get-docker/

The application image is available on Docker Hub under the reference:

**mattmatt78/oc-lettings-site:latest**

Docker Desktop must be running in the background. Verify its status with the command:

.. code-block:: bash

  docker version

Here is the method through a terminal:

Log into Docker Hub
-------------------
if not already done in docker desktop, should open your web browser:

.. code-block:: bash

  docker login


Download the docker image
-------------------------
Download the latest version of the image from docker hub:

.. code-block:: bash

  docker pull mattmatt78/oc-lettings-site:latest


Run the docker image
--------------------
-e option to set environment variables

For **Linux**:

.. code-block:: bash

  docker run -d --name oc-lettings-site 
    -e DEBUG=False \
    -e SENTRY_DEBUG=False \
    -e DJANGO_SECRET_KEY="my_django_secret_key" \
    -e SENTRY_DSN=my_sentry_secret_key \
    -p 8080:8080 \
    mattmatt78/oc-lettings-site:latest


For **windows powershell**, replace "\" by "`":

.. code-block:: bash

  docker run -d --name oc-lettings-site `
    -e DEBUG=False `
    -e SENTRY_DEBUG=False `
    -e DJANGO_SECRET_KEY="my_django_secret_key" `
    -e SENTRY_DSN=my_sentry_secret_key `
    -p 8080:8080 `
    mattmatt78/oc-lettings-site:latest

The application will be accessible at: http://localhost:8080

Stop the app
------------
To stop the application:

.. code-block:: bash

  docker stop oc-lettings-site

Remove docker container
-----------------------
To remove the container, first list all containers:

.. code-block:: bash

  docker ps -a

retrieve the Container ID then:

.. code-block:: bash

  docker rm [Container_ID]
