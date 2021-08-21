#
""" Common Facilities For Remote Operations Scenarios For Verification Of Petstore Service. 
    
    Common Parameter Specification.

    To be imported by Petstore Service opScn-s.
"""

from unisos.mmwsIcm import ro
from unisos import icm

import time

def petstoreSvcSpecObtain():
    return "http://petstore.swagger.io/v2/swagger.json"

def petstoreSvcPerfSapObtain():
    return None

def verify_petstoreSvcCommonRo(opExpectation):
    roOp = opExpectation.roOp
    opResults = roOp.roResults
    if opResults.httpResultCode < 400:
        icm.ANN_write("* ==:: SUCCESS")
    else:
        icm.ANN_write("* ==:: FAILED")

def sleep1Sec(opExpectation):
    icm.ANN_write("* XX:: Sleeping For 1 Second")    
    time.sleep(1)
         
