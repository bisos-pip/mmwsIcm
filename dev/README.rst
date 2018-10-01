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

This module’s primary documentation is in
http://www.by-star.net/PLPC/180047

On the invoker side, a Swagger (Open-API) specification is digested with
bravado and is mapped to command line with ICM.

On the performer side, a Swagger (Open-API) specification is used with
the code-generator to create a consistent starting point.

An ICM can be auto-converted to become a web service.

Example Usage
=============

::

    from  mmwsIcm import rinvoker
