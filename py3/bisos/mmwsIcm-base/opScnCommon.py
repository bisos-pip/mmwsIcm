#
""" Common Facilities For Remote Operations Scenarios For Verification Of Petstore Service. 
    
    Common Parameter Specification.

    To be imported by Petstore Service opScn-s.
"""

from bisos.mmwsIcm import ro
# from uni sos import icm

import time

def petstoreSvcSpecObtain():
    return "http://petstore.swagger.io/v2/swagger.json"

def petstoreSvcPerfSapObtain():
    return None

def verify_petstoreSvcCommonRo(opExpectation):
    roOp = opExpectation.roOp
    opResults = roOp.roResults
    if opResults.httpResultCode < 400:
        b_io.ann.write("* ==:: SUCCESS")
    else:
        b_io.ann.write("* ==:: FAILED")

def sleep1Sec(opExpectation):
    b_io.ann.write("* XX:: Sleeping For 1 Second")    
    time.sleep(1)
         
