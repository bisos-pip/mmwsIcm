=============================================================================================
bisos.mmWsCs: MM-WS-CS Library: Machine-to-Machine – Web Services – Command Services (CS) – A
=============================================================================================

.. contents::
   :depth: 3
..

set of facilities for developing Performer and Invoker web-services
based on Swagger (Open-API) specifications through ICMs.

Overview
========

bisos.mmWsCs is a python package for BISOS Capabilities Bundles –
Abstraction, Specification and Materialization.

Package Documentation At Github
===============================

The information below is a subset of the full of documentation for this
bisos-pip package. More complete documentation is available at:
https://github.com/bisos-pip/mmWsCs-cs

Realted Resources
=================

+--------------------------+------------------------------------------+
| bisos Capabilities Panel | file:/panels/capab                       |
|                          | ilities/_nodeBase_/fullUsagePanel-en.org |
+--------------------------+------------------------------------------+
|                          |                                          |
+--------------------------+------------------------------------------+

.. _table-of-contents:

Table of Contents TOC
=====================

-  `Overview <#overview>`__
-  `Package Documentation At
   Github <#package-documentation-at-github>`__
-  `Realted Resources <#realted-resources>`__
-  `Installation <#installation>`__

   -  `Installation With pip <#installation-with-pip>`__
   -  `Installation With pipx <#installation-with-pipx>`__
   -  `Remote Invoker (rinvoker-svc.py)
      Examples <#remote-invoker-rinvoker-svcpy-examples>`__
   -  `Operation Scenario (opScn-svc.py)
      Examples <#operation-scenario-opscn-svcpy-examples>`__

-  `->:: @None@pet@getPetById <#--nonepetgetpetbyid>`__

   -  `->::
      svcSpec=\  <#--svcspechttppetstoreswaggeriov2swaggerjson>`__\ http://petstore.swagger.io/v2/swagger.json
   -  `->:: Header Params: None <#--header-params-none>`__
   -  `->:: Url Params: <#--url-params>`__
   -  `->:: Body Params: None <#--body-params-none>`__

-  `<-:: httpStatus=200 – httpText=OK –
   resultsFormat=json <#--httpstatus200----httptextok----resultsformatjson>`__

   -  `<-:: Operation Result: <#--operation-result>`__

-  `==:: SUCCESS <#-success>`__
-  `XX:: Sleeping For 1 Second <#xx-sleeping-for-1-second>`__
-  `->:: @None@pet@getPetById <#--nonepetgetpetbyid-1>`__

   -  `->::
      svcSpec=\  <#--svcspechttppetstoreswaggeriov2swaggerjson-1>`__\ http://petstore.swagger.io/v2/swagger.json
   -  `->:: Header Params: None <#--header-params-none-1>`__
   -  `->:: Url Params: <#--url-params-1>`__
   -  `->:: Body Params: None <#--body-params-none-1>`__

-  `<-:: httpStatus=200 – httpText=OK –
   resultsFormat=json <#--httpstatus200----httptextok----resultsformatjson-1>`__

   -  `<-:: Operation Result: <#--operation-result-1>`__

-  `==:: SUCCESS <#-success-1>`__
-  `Python Example Usage <#python-example-usage>`__

   -  `Invoker (Client) Development <#invoker-client-development>`__
   -  `Testing Framework <#testing-framework>`__
   -  `Performer (Server) Development <#performer-server-development>`__

-  `Part of BISOS and ByStar — ByStar Internet Services Operating
   System <#part-of-bisos-and-bystar-----bystar-internet-services-operating-system>`__
-  `bisos.mmWsCs as a Standalone Piece of
   BISOS <#bisosmmwscs-as-a-standalone-piece-of-bisos>`__
-  `Documentation and Blee-Panels <#documentation-and-blee-panels>`__

   -  `bisos.mmWsCs Blee-Panels <#bisosmmwscs-blee-panels>`__

-  `Support <#support>`__

Installation
============

The sources for the bisos.mmWsCs pip package is maintained at:
https://github.com/bisos-pip/mmWsCs.

The bisos.mmWsCs pip package is available at PYPI as
https://pypi.org/project/bisos.mmWsCs

You can install bisos.mmWsCs with pip or pipx.

Installation With pip
---------------------

If you need access to bisos.mmWsCs as a python module, you can install
it with pip:

.. code:: bash

   pip install bisos.mmWsCs

Installation With pipx
----------------------

If you only need access to bisos.mmWsCs as a command on command-line,
you can install it with pipx:

.. code:: bash

   pipx install bisos.mmWsCs

The following commands are made available:

-  bin/rinvoker.py A starting point template to be customized for your
   own swagger file.
-  bin/rinvokerPetstore.py Provides a list of Petstore example command
   line invokations.
-  bin/opScnPetstore.py Points to various scenario files for the
   Petstore example.

Remote Invoker (rinvoker-svc.py) Examples
-----------------------------------------

For the example \``Pet Store Service'' at
http://petstore.swagger.io/v2/swagger.json at command-line (or in bash)
you can run:

.. code:: bash

   rinvokerPetstore.py

Which will auto generate a complete list of all supported remote
opperations in the Swagger Service Specification.

You can then invoke any of those remote operations from the
command-line, by executing for example:

.. code:: bash

   rinvokerPetstore.py --svcSpec="http://petstore.swagger.io/v2/swagger.json" --resource="pet" --opName="getPetById"  -i rinvoke petId=1

Which will produce something like:

.. code:: bash

   Operation Status: 200 OK
   Operation Result: {   u'category': {   u'id': 0, u'name': u'string'},
       u'id': 1,
       u'name': u'testsw',
       u'photoUrls': [u'string'],
       u'status': u'tttest',
       u'tags': [{   u'id': 0, u'name': u'string'}]}

By turning on verbosity to level 15 (rinvokerPetstore.py -v 15) you can
observe complete http traffic as reported by requests library.

Operation Scenario (opScn-svc.py) Examples
------------------------------------------

For the example \``Pet Store Service'' at
http://petstore.swagger.io/v2/swagger.json using python with RO\\_
abstractions you can specify remote invokation and expectations.

To get a list of some example scenatios run:

.. code:: bash

   opScnPetstore.py

To run a particular example scenario, you can then run:

.. code:: bash

   opScnPetstore.py  --load /tmp/py2v1/local/lib/python2.7/site-packages/bisos/mmwsIcm-base/opScn-1.py -i roListExpectations

Which will produce something like:

.. code:: bash

   * ->:: @None@pet@getPetById
   ** ->:: svcSpec=http://petstore.swagger.io/v2/swagger.json
   ** ->:: Header Params: None
   ** ->:: Url Params:
   {   'petId': 1}
   ** ->:: Body Params: None
   * <-:: httpStatus=200 -- httpText=OK -- resultsFormat=json
   ** <-:: Operation Result:
   {   u'category': {   u'id': 1, u'name': u'dog'},
       u'id': 1,
       u'name': u'Dog1',
       u'photoUrls': [],
       u'status': u'pending',
       u'tags': []}
   * ==:: SUCCESS
   * XX:: Sleeping For 1 Second
   * ->:: @None@pet@getPetById
   ** ->:: svcSpec=http://petstore.swagger.io/v2/swagger.json
   ** ->:: Header Params: None
   ** ->:: Url Params:
   {   'petId': 9999}
   ** ->:: Body Params: None
   * <-:: httpStatus=200 -- httpText=OK -- resultsFormat=json
   ** <-:: Operation Result:
   {   u'category': {   u'id': 99, u'name': u'SAGScope'},
       u'id': 9999,
       u'name': u'doggie',
       u'photoUrls': [u'string'],
       u'status': u'available',
       u'tags': [{   u'id': 99, u'name': u'SAGTags'}]}
   * ==:: SUCCESS

Python Example Usage
====================

Invoker (Client) Development
----------------------------

.. code:: bash

   from bisos.mmwsIcm import wsInvokerIcm
   from bisos.mmwsIcm import ro

Testing Framework
-----------------

.. code:: bash

   from bisos.mmwsIcm import wsInvokerIcm
   from bisos.mmwsIcm import ro

Performer (Server) Development
------------------------------

.. code:: bash

   from bisos.mmwsIcm import wsInvokerIcm
   from bisos.mmwsIcm import ro

Part of BISOS and ByStar — ByStar Internet Services Operating System
====================================================================

| Layered on top of Debian, **BISOS**: (By\* Internet Services Operating
  System) is a unified and universal framework for developing both
  internet services and software-service continuums that use internet
  services. See `Bootstrapping ByStar, BISOS and
  Blee <https://github.com/bxGenesis/start>`__ for information about
  getting started with BISOS.
| **BISOS** is a foundation for **The Libre-Halaal ByStar Digital
  Ecosystem** which is described as a cure for losses of autonomy and
  privacy in a book titled: `Nature of
  Polyexistentials <https://github.com/bxplpc/120033>`__

*bisos.mmWsCs* is part of BISOS.

bisos.mmWsCs as a Standalone Piece of BISOS
===========================================

bisos.mmWsCs is a standalone piece of BISOS. It can be used as a
self-contained Python package separate from BISOS. Follow the
installation and usage instructions below for your own use.

Documentation and Blee-Panels
=============================

bisos.mmWsCs is part of ByStar Digital Ecosystem http://www.by-star.net.

This module's primary documentation is in the form of Blee-Panels.
Additional information is also available in:
http://www.by-star.net/PLPC/180047

bisos.mmWsCs Blee-Panels
------------------------

bisos.mmWsCs Blee-Panels are in ./panels directory. From within Blee and
BISOS these panels are accessible under the Blee "Panels" menu.

-  Remote Operations Interactive Command Modules (RO-ICM) – Best Current
   (2019) Practices For Web Services Development
   http://www.by-star.net/PLPC/180056
-  A Generalized Swagger (Open-API) Centered Web Services Testing
   Framework http://www.by-star.net/PLPC/180057
-  Interactive Command Modules (ICM) and Players
   http://www.by-star.net/PLPC/180050

On the invoker side, a Swagger (Open-API) specification is digested with
bravado and is mapped to command line with ICM.

On the performer side, a Swagger (Open-API) specification is used with
the code-generator to create a consistent starting point.

An ICM can be auto-converted to become a web service.

Support
=======

| For support, criticism, comments and questions; please contact the
  author/maintainer
| `Mohsen Banan <http://mohsen.1.banan.byname.net>`__ at:
  http://mohsen.1.banan.byname.net/contact
