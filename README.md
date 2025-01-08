amazonlinux2-nodejs
===================

A GitLab pipeline to build [Node.js](https://nodejs.org/) 18.x, 20.x, 22.x and 23.x for Amazon Linux 2.

Rationale
---------

Starting from 18.x, official Node.js LTS builds cannot be used on Amazon Linux 2, due to
binary incompatibilities (missing glibc symbol versions).

AWS recommends to build those Node.js versions from source, when using Amazon Linux 2 (AL2).

Implementation
--------------

The pipeline launches an `amazonlinux:2` container and:

* Installs prerequisites
* Fetches the latest release tag for a specific Node.js major version
* Builds this release from source code
* Publishes the build to this project's package registry

Downloads
---------

Node.js 18.x, 20.x, 22.x and 23.x builds for Amazon Linux 2 can be downloaded from the
[Package Registry](https://code.europa.eu/ecgalaxy/amazonlinux2-nodejs/-/packages).

Automated setup
---------------

See the [ECGALAXY Node.js Ansible role](https://code.europa.eu/ecgalaxy/nodejs)
to globally install Node.js on Amazon Linux 2 and other distributions, using automation.

Original work
-------------

Original code provided by AWS.

Author Information
------------------

[ECGALAXY](https://code.europa.eu/groups/ecgalaxy/-/wikis/home) team.
