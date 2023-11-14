amazonlinux2-nodejs
===================

A GitLab pipeline to build [Node.js](https://nodejs.org/) 18.x and 20.x for Amazon Linux 2.

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

Original work
-------------

Original code provided by AWS.

Author Information
------------------

ECGALAXY team.
