======================
unisos.mmwsIcm Library
======================

.. contents::
   :depth: 3
..

MM-WS-ICM Library: Machine-to-Machine Web Service Interactive Command
Modules (ICM) – A set of facilities for developing Performer and Invoker
web-services based on Swagger (Open-API) specifications through ICMs.

Support
=======

| For support, criticism, comments and questions; please contact the
  author/maintainer
| `Mohsen Banan <http://mohsen.1.banan.byname.net>`__ at:
  http://mohsen.1.banan.byname.net/contact

Documentation
=============

Part of ByStar Digital Ecosystem http://www.by-star.net.

Remote Operations Interactive Command Modules (RO-ICM) – Best Current
(2018) Practices For Web Services Development
    http://www.by-star.net/PLPC/180056

A Generalized Swagger (Open-API) Centered Web Services Testing Framework
    http://www.by-star.net/PLPC/180057

Interactive Command Modules (ICM) and Players
    http://www.by-star.net/PLPC/180050

On the invoker side, a Swagger (Open-API) specification is digested with
bravado and is mapped to command line with ICM.

On the performer side, a Swagger (Open-API) specification is used with
the code-generator to create a consistent starting point.

An ICM can be auto-converted to become a web service.

Binaries
========

“./bin/rinvoker.py”
    A starting point template to be customized for your own swagger
    file.

“./bin/rinvokerPetstore.py”
    Provides a list of Petstore example command line invokations.

“./bin/opScnPetstore.py”
    Points to various scenario files for the Petstore example.

Example Usage
=============

::

    from unisos.mmwsIcm import wsInvokerIcm
    from unisos.mmwsIcm import ro
