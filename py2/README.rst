======================
unisos.mmwsIcm Library
======================

.. contents::
   :depth: 3
..

MM-WS-ICM Library: Machine-to-Machine Web Service Interactive Command
Modules (ICM) – A set of facilities for developing Performer and Invoker
web-services based on Swagger (Open-API) specifications through ICMs.

Sources And Packages
====================

Sources Repositories
--------------------

-  GitHub: https://github.com/bisos-pip/mmwsIcm

Packages Repositories
---------------------

-  PyPi: https://pypi.org/project/unisos.mmwsIcm

Support
=======

| For support, criticism, comments and questions; please contact the
  author/maintainer
| `Mohsen Banan <http://mohsen.1.banan.byname.net>`__ at:
  http://mohsen.1.banan.byname.net/contact

Documentation
=============

Part of ByStar Digital Ecosystem http://www.by-star.net.

-  | Remote Operations Interactive Command Modules (RO-ICM) – Best
     Current (2019) Practices For Web Services Development
   | http://www.by-star.net/PLPC/180056

-  | A Generalized Swagger (Open-API) Centered Web Services Testing
     Framework
   | http://www.by-star.net/PLPC/180057

-  | Interactive Command Modules (ICM) and Players
   | http://www.by-star.net/PLPC/180050

On the invoker side, a Swagger (Open-API) specification is digested with
bravado and is mapped to command line with ICM.

On the performer side, a Swagger (Open-API) specification is used with
the code-generator to create a consistent starting point.

An ICM can be auto-converted to become a web service.

Binaries And Command-Line Examples
==================================

-  | bin/rinvoker.py
   | A starting point template to be customized for your own swagger
     file.

-  | bin/rinvokerPetstore.py
   | Provides a list of Petstore example command line invokations.

-  | bin/opScnPetstore.py
   | Points to various scenario files for the Petstore example.

Remote Invoker (rinvoker-svc.py) Examples
-----------------------------------------

For the example “Pet Store Service” at
http://petstore.swagger.io/v2/swagger.json at command-line (or in bash)
you can run:

::

   rinvokerPetstore.py

Which will auto generate a complete list of all supported remote
opperations in the Swagger Service Specification.

You can then invoke any of those remote operations from the
command-line, by executing for example:

::

   rinvokerPetstore.py --svcSpec="http://petstore.swagger.io/v2/swagger.json" --resource="pet" --opName="getPetById"  -i rinvoke petId=1

Which will produce something like:

::

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

For the example “Pet Store Service” at
http://petstore.swagger.io/v2/swagger.json using python with RO\_
abstractions you can specify remote invokation and expectations.

To get a list of some example scenatios run:

::

   opScnPetstore.py

To run a particular example scenario, you can then run:

::

   opScnPetstore.py  --load /tmp/py2v1/local/lib/python2.7/site-packages/unisos/mmwsIcm-base/opScn-1.py -i roListExpectations

Which will produce something like:

::

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

::

   from unisos.mmwsIcm import wsInvokerIcm
   from unisos.mmwsIcm import ro

Testing Framework
-----------------

::

   from unisos.mmwsIcm import wsInvokerIcm
   from unisos.mmwsIcm import ro

Performer (Server) Development
------------------------------

::

   from unisos.mmwsIcm import wsInvokerIcm
   from unisos.mmwsIcm import ro
