# rocketmiles-test
Tests for Rocketmiles.com search functionality

Pipenv used for dependency management; see Pipfile for package list.
Tests use pytest, pytest-bdd, and selenium.
Dockerfile uses webdrivermanager to download drivers for selenium.

To run the tests:
0. Docker takes care of all the dependencies except itself, so...
1. [Install Docker](https://hub.docker.com/?overlay=onboarding)
2. `$ docker pull docker.pkg.github.com/desophos/rocketmiles-test/testenv:0.1.0`
3. `$ docker run docker.pkg.github.com/desophos/rocketmiles-test/testenv:0.1.0`
