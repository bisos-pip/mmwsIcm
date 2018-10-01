# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* ::  A /library/ for Abstracting Remote Operations.
"""


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "ro"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201809210755"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Beta"
__status__ = "Beta"
####+END:

__credits__ = [""]

####+BEGINNOT: bx:dblock:global:file-insert-cond :cond "./blee.el" :file ""
icmInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
}
####+END:

####+BEGIN: bx:icm:python:topControls 
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

"""
* 
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/pythonWb.org"
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "pep8 %s" (bx:buf-fname))))][pep8]] | [[elisp:(python-check (format "flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
####+END:
"""


####+BEGIN: bx:icm:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

#import os
import collections
#import enum

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__

####+END:


import pprint
#import datetime
#import random
#import struct
#import sys
#import json
#import base64

#import jwt

#from unisos.mmwsIcm import wsInvokerIcm
import wsInvokerIcm

####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "icmBegin_libOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /icmBegin_libOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class icmBegin_libOverview(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        moduleDescription="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]	Model and Terminology 					   :Overview:
This module is part of BISOS and its primary documentation is in  http://www.by-star.net/PLPC/180047
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  ICM Common       :: Add -i cmndFpUpdate .  and -i cmndFpShow . [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: Add -p headers=fileName  [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: Auto generate cmndsList with no args  [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: Instead of parName=parNameVALUE do parName=partType (int64) [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  rinvokerXxxx     :: Create a thin template for using wsIcmInvoker [[elisp:(org-cycle)][| ]]

**      [End-Of-Status]
"""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        icm.unusedSuppressForEval(moduleUsage, moduleStatus)
        actions = self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)
        if actions[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            actions = argChoices
        for each in actions:
            print each
            if interactive:
                #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                #version(interactive=True)
                exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="actions",
            argDefault='all',
            argChoices=['all', 'moduleDescription', 'moduleUsage', 'moduleStatus'],
            argDescription="Output relevant information",
        )

        return cmndArgsSpecDict
####+END:

####+BEGIN: bx:icm:python:subSection :title "Common Arguments Specification"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Common Arguments Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "commonParamsSpecify" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "icmParams"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /commonParamsSpecify/ retType=bool argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:

    icmParams.parDictAdd(
        parName='placeHolder',
        parDescription="Name Of The User",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--userName',
    )
    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################## [[elisp:(delete-other-windows)][(1)]]        *Common Examples Sections*
"""

####+BEGIN: bx:icm:python:func :funcName "examples_remoteOperations" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "roListLoadFile roExpectListLoadFile"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /examples_remoteOperations/ retType=bool argsList=(roListLoadFile roExpectListLoadFile)  [[elisp:(org-cycle)][| ]]
"""
def examples_remoteOperations(
    roListLoadFile,
    roExpectListLoadFile,
):
####+END:
    """."""
    
    def cpsInit(): return collections.OrderedDict()
    #def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    icm.cmndExampleMenuChapter('/Remote Operation Scenario Files/ *roListInv*')

    loadOpScenariosArgs=""" --load {}""".format(roListLoadFile)

    thisCmndAction= " -i roListInv"
    
    icm.cmndExampleMenuItem(format(loadOpScenariosArgs + thisCmndAction),
                            verbosity='none')                            
    icm.cmndExampleMenuItem(format(loadOpScenariosArgs + thisCmndAction),
                            verbosity='full')

    loadOpScenariosArgs=""" --load {}""".format(roExpectListLoadFile)

    thisCmndAction= " -i roListExpectations"
    
    icm.cmndExampleMenuItem(format(loadOpScenariosArgs + thisCmndAction),
                            verbosity='none')                            
    icm.cmndExampleMenuItem(format(loadOpScenariosArgs + thisCmndAction),
                            verbosity='full')                            
    


####+BEGIN: bx:icm:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "roListInv" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /roListInv/ parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class roListInv(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:

        rosList = Ro_OpsList().opsListGet()

        @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
        def rosListProc(rosList):
            """Process List of Remote Operations"""
            @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
            def roProc(thisRo):
                """Process One Remote Operation"""

                return ( wsInvokerIcm.ro_opInvokeCapture(thisRo) )

            for thisRo in rosList:
                invokedOp = roProc(thisRo)
                opReport(invokedOp)

            return

        rosListProc(rosList)

        return( cmndOutcome )

    
    def cmndDocStr(self): return """
** Place holder for ICM's experimental or test code.  [[elisp:(org-cycle)][| ]]
 You can use this Cmnd for rapid prototyping and testing of newly developed functions.
"""

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
        ***** Cmnd Args Specification
        """
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="actionPars",
            argDefault=None,
            argChoices='any',
            argDescription="Rest of args for use by action"
            )

        return cmndArgsSpecDict
        


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "roListExpectations" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /roListExpectations/ parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class roListExpectations(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:

        roExpectationsList = Ro_OpExpectationsList().opExpectationsListGet()

        print(roExpectationsList)

        @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
        def roExpectationsListProc(roExpectationsList):
            """Process List of Remote Operations Expectations"""
            @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
            def roExpectationProc(thisRoExpecation):
                """Process One Remote Operation"""

                thisRo = thisRoExpecation.roOp

                for thisPreInvokeCallable in thisRoExpecation.preInvokeCallables:
                    thisPreInvokeCallable(thisRoExpecation)

                invokedOp = wsInvokerIcm.ro_opInvokeCapture(thisRo)

                for thisPostInvokeCallable in thisRoExpecation.postInvokeCallables:
                    thisPostInvokeCallable(thisRoExpecation)

                return invokedOp

            for thisRoExpecation in roExpectationsList:
                invokedOp = roExpectationProc(thisRoExpecation)

            return invokedOp

        roExpectationsListProc(roExpectationsList)

        return( cmndOutcome )


    
    def cmndDocStr(self): return """
** Place holder for ICM's experimental or test code.  [[elisp:(org-cycle)][| ]]
 You can use this Cmnd for rapid prototyping and testing of newly developed functions.
"""

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
        ***** Cmnd Args Specification
        """
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="actionPars",
            argDefault=None,
            argChoices='any',
            argDescription="Rest of args for use by action"
            )

        return cmndArgsSpecDict
        
    
    
####+BEGIN: bx:icm:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:class :className "Ro_Params" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Class-basic    :: /Ro_Params/ object  [[elisp:(org-cycle)][| ]]
"""
class Ro_Params(object):
####+END:

     def __init__(
             self,
             headerParams,
             urlParams,
             bodyParams,
             svcSpec=None,
             resource=None,
             opName=None,
             ):

         # Instance Variables Enumeration
         
         self.headerParams = headerParams
         self.urlParams = urlParams
         self.bodyParams = bodyParams
         self.svcSpec = svcSpec
         self.resource = resource
         self.opName = opName


####+BEGIN: bx:dblock:python:class :className "Ro_Results" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Class-basic    :: /Ro_Results/ object  [[elisp:(org-cycle)][| ]]
"""
class Ro_Results(object):
####+END:

     def __init__(
             self,
             httpResultCode,
             httpResultText,
             opResults=None,
             opResultHeaders=None,
             ):
         
         # Instance Variables Enumeration
         
         self.httpResultCode = httpResultCode
         self.httpResultText = httpResultText
         self.opResults = opResults
         self.opResultHeaders = opResultHeaders
         

####+BEGIN: bx:dblock:python:class :className "Ro_Op" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Class-basic    :: /Ro_Op/ object  [[elisp:(org-cycle)][| ]]
"""
class Ro_Op(object):
####+END:

    # No Class Variables Enumeration

     def __init__(
             self,
             svcSpec,
             perfSap,
             resource,
             opName,
             roParams,
             roResults=None,
             ):

         # Instance Variables Enumeration
         self.svcSpec = svcSpec
         self.perfSap = perfSap
         self.resource = resource
         self.opName = opName         
         self.roParams = roParams
         self.roResults = roResults

         self.invokeStartTime = None
         self.invokeEndTime = None

         return


         
####+BEGIN: bx:dblock:python:class :className "Ro_OpsList" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Class-basic    :: /Ro_OpsList/ object  [[elisp:(org-cycle)][| ]]
"""
class Ro_OpsList(object):
####+END:
    """Maintain a list of Ro_Op. """

    # Class Variables Enumeration
    opsList = []  # Typically set in loaded files and used in ICM-Libs

    
    def __init__(self,):
        pass

    def opAppend(self,
                  op,
        ):
        """
        """
        self.__class__.opsList.append(op)

    def opAdd(self,
              svcSpec,
              perfSap,
              resource,
              opName,
              roParams,
              roResults=None,
        ):
        """
        """
        op = Ro_Op(
            svcSpec=svcSpec,
            perfSap=perfSap,
            resource=resource,
            opName=opName,
            roParams=roParams,
            roResults=roResults,
        )

        self.__class__.opsList.append(op)

    def opsListGet(self):
         """
         """
         return self.__class__.opsList



####+BEGIN: bx:dblock:python:class :className "Ro_OpExpectation" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Class-basic    :: /Ro_OpExpectation/ object  [[elisp:(org-cycle)][| ]]
"""
class Ro_OpExpectation(object):
####+END:

     def __init__(
             self,
             roOp,
             postInvokeCallables,
             preInvokeCallables=[],
             expectedResults=None,
             ):
         
         # Instance Variables Enumeration
         self.roOp = roOp
         self.preInvokeCallables = preInvokeCallables
         self.postInvokeCallables = postInvokeCallables         
         self.expectedResults = expectedResults

####+BEGIN: bx:dblock:python:class :className "Ro_OpExpectationsList" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Class-basic    :: /Ro_OpExpectationsList/ object  [[elisp:(org-cycle)][| ]]
"""
class Ro_OpExpectationsList(object):
####+END:
    """Maintain a list of Ro_OpExpctation.
    """

    # Class Variables Enumeration
    opExpectationsList = []  # Typically set in loaded files and used in ICM-Libs
        
    def __init__(self,):
        pass

    def opExpectationAppend(self,
                  opExpectation,
        ):
        """
        """
        self.__class__.opExpectationsList.append(opExpectation)
        

    def opExpectationAdd(self,
              svcSpec,
              perfSap,
              resource,
              opName,
              roParams,
              roResults,
              postInvokeCallables,
              preInvokeCallables=None,
              expectedResults=None,
        ):
        """
        """
        op = Ro_Op(
            svcSpec=svcSpec,
            perfSap=perfSap,
            resource=resource,
            opName=opName,
            roParams=roParams,
            roResults=roResults,
        )

        opExpectation = Ro_OpExpectation(
            roOp=op,
            preInvokeCallables=preInvokeCallables,            
            postInvokeCallables=postInvokeCallables,
            expectedResults=expectedResults,
        )

        self.__class__.opExpectationsList.append(opExpectation)

    def opExpectationsListGet(self):
         """
         """
         return self.__class__.opExpectationsList

    
             
        
####+BEGIN: bx:icm:python:section :title "Supporting Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "opReport" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "op"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /opReport/ retType=bool argsList=(op)  [[elisp:(org-cycle)][| ]]
"""
def opReport(
    op,
):
####+END:
    pp = pprint.PrettyPrinter(indent=4)

    icm.ANN_write("""* ->:: @{perfSap}@{resource}@{opName} with {params}""".format(
        perfSap=op.perfSap,
        resource=op.resource,
        opName=op.opName,
        params="bodyParams",
    ))

    params = op.roParams    

    icm.ANN_write("""** ->:: svcSpec={svcSpec}""".format(
        svcSpec=op.svcSpec,
    ))

    icm.ANN_write("** <-:: Body Params: \n{bodyParams}".format(
        bodyParams=pp.pformat(params.bodyParams)))
        
    results = op.roResults        
        
    icm.ANN_write("""* <-:: {httpResultCode} -- {httpResultText} -- {resultType}""".format(
        httpResultCode=results.httpResultCode,
        httpResultText=results.httpResultText,
        resultType="json",
    ))

    icm.ANN_write("** <-:: Operation Result: \n{result}".format(
        result=pp.pformat(results.opResults)))
    

    icm.ANN_write("""* ==:: basicPass or failed or Verified""")
        
        
             
    
####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
