#
""" Remote Operations Scenarios For Verification Of Petstore Service. 
    rosList creates a list of Ro_Op-s which are to be invoked/validated/etc.
"""

from bisos.mmwsIcm import ro

# import opScnCommon   # is a better way of doing it when  you have multiple scn files.

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
         

petstoreSvcSpec = petstoreSvcSpecObtain()
petstoreSvcPerfSap = petstoreSvcPerfSapObtain()

#headerParams = opScnCommon.petstoreSvcHeaderParamsObtain()
#verify_petstoreSvcCommonRo = opScnCommon.verify_petstoreSvcCommonRo  # Alias function, for brevity

rosList = ro.Ro_OpsList()
roExpectationsList = ro.Ro_OpExpectationsList()

thisRo = ro.Ro_Op(
    svcSpec=petstoreSvcSpec,
    perfSap=petstoreSvcPerfSap,
    resource="pet",
    opName="getPetById",
    roParams=ro.Ro_Params(
        headerParams=None,
        urlParams={ "petId": 1},
        bodyParams=None,
        ),
    roResults=None,
    )

thisExpectation = ro.Ro_OpExpectation(
    roOp=thisRo,
    preInvokeCallables=[],
    postInvokeCallables=[ verify_petstoreSvcCommonRo, ],        
    expectedResults=None,
    )

rosList.opAppend(thisRo)
roExpectationsList.opExpectationAppend(thisExpectation)


thisRo = ro.Ro_Op(
    svcSpec=petstoreSvcSpec,
    perfSap=petstoreSvcPerfSap,
    resource="pet",
    opName="getPetById",
    roParams=ro.Ro_Params(
        headerParams=None,
        urlParams={ "petId": 9999},
        bodyParams=None,
        ),
    roResults=None,
    )

thisExpectation = ro.Ro_OpExpectation(
    roOp=thisRo,
    preInvokeCallables=[sleep1Sec],
    postInvokeCallables=[ verify_petstoreSvcCommonRo, ],        
    expectedResults=None,
    )

rosList.opAppend(thisRo)
roExpectationsList.opExpectationAppend(thisExpectation)
