# Docker-airflow with MySql as backend

This repository contains **Dockerfile** of [apache-airflow](https://github.com/apache/incubator-airflow) .

## Informations

* Based on Python (3.6-slim) official Image [python:3.6-slim](https://hub.docker.com/_/python/) and uses the official [MySql](https://hub.docker.com/_/mysql/) as backend and [Redis](https://hub.docker.com/_/redis/) as queue
* Install [Docker](https://www.docker.com/)
* Install [Docker Compose](https://docs.docker.com/compose/install/)
* Following the Airflow release from [Python Package Index](https://pypi.python.org/pypi/apache-airflow)


## Build

For Building the docker container for airflow you first need to build the docker image using the dockerfile added in the repository.For adding [Extra Packages](https://airflow.incubator.apache.org/installation.html#extra-package) edit the docker file and then build.

    docker build --rm -t jksingh/docker-airflow .

Don't forget to update the airflow images in the docker-compose files to jksingh/docker-airflow:latest.

## Usage

By default, docker-airflow runs Airflow with **SequentialExecutor** :

    docker run -d -p 8080:8080 jksingh/docker-airflow webserver

If you want to run another executor, use the other docker-compose files provided in this repository.

For **LocalExecutor** :

    docker-compose -f docker-compose-mysql-local.yml up -d

For **CeleryExecutor** :

    docker-compose -f docker-compose-mysql-celery.yml up -d

NB : If you want to have DAGs example loaded (default=False), you've to set the following environment variable :

`LOAD_EX=n`

    docker run -d -p 8080:8080 -e LOAD_EX=y jksingh/docker-airflow


## UI Links

- Airflow: [localhost:8080](http://localhost:8080/)
- Flower: [localhost:5555](http://localhost:5555/)


# Issues

- Issue Tracker: https://github.com/jksinghpro/docker-airflow/issues


