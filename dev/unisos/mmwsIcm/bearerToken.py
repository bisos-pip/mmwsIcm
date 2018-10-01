# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* ::  A /library/ for generating, validating  and decoding bearer tokens.
"""


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "bearerTokenGen"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201808014304"
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
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import os
import collections
import enum

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__

####+END:


import pprint
import datetime
import random
import struct
import sys
import json
import base64

import jwt

####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "icmBegin_libOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /icmBegin_libOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Common Arguments Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "commonParamsSpecify" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "icmParams"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /commonParamsSpecify/ retType=bool argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:

    icmParams.parDictAdd(
        parName='userName',
        parDescription="Name Of The User",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--userName',
    )

    icmParams.parDictAdd(
        parName='role',
        parDescription="User Role",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--role',
    )

    icmParams.parDictAdd(
        parName='acGroups',
        parDescription="Resource Group IDs",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--acGroups',
    )

    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]        *Common Examples Sections*
"""

####+BEGIN: bx:icm:python:func :funcName "examples_tokenGenerator" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "userName role acGroups"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /examples_tokenGenerator/ retType=bool argsList=(userName role acGroups)  [[elisp:(org-cycle)][| ]]
"""
def examples_tokenGenerator(
    userName,
    role,
    acGroups,
):
####+END:
    """."""
    
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    icm.cmndExampleMenuChapter('*= bearerToken CmndsLib: Token Manager -- Output / Input =*')

    icm.cmndExampleMenuSection('* -i jwtPlain*')

    cmndName = "jwtPlainOutStr"

    cps = cpsInit();
    cps['userName'] = userName
    cps['role'] = role
    cps['acGroups'] = acGroups       
    cmndArgs = "";
    menuItem(verbosity='none')
    #icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')

    cmndName = "jwtPlainOutFile"

    cps = cpsInit();
    cps['userName'] = userName
    cps['role'] = role
    cps['acGroups'] = acGroups       
    cmndArgs = "/tmp/bearerPlain.json";
    menuItem(verbosity='none')

    icm.cmndExampleMenuSection('* -i jwtSigned*')

    cmndName = "jwtSignedOutStr"

    cps = cpsInit();
    cps['userName'] = userName
    cps['role'] = role
    cps['acGroups'] = acGroups       
    cmndArgs = "";
    menuItem(verbosity='none')

    cmndName = "jwtSignedOutFile"

    cps = cpsInit();
    cps['userName'] = userName
    cps['role'] = role
    cps['acGroups'] = acGroups       
    cmndArgs = "/tmp/bearerSigned.jwt";
    menuItem(verbosity='none')


    icm.cmndExampleMenuSection('* -i jwtPlainInput*')

    cmndName = "jwtPlainInFiles"

    cps = cpsInit();
    cmndArgs = "/tmp/bearerPlain.json";
    menuItem(verbosity='none')
    
    


####+BEGIN: bx:icm:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
    

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "tokenOutput" :comment "OBSOLETED" :parsMand "" :parsOpt "userName role acGroups" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /tokenOutput/ =OBSOLETED= parsMand= parsOpt=userName role acGroups argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class tokenOutput(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'userName', 'role', 'acGroups', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        userName=None,         # or Cmnd-Input
        role=None,         # or Cmnd-Input
        acGroups=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'userName': userName, 'role': role, 'acGroups': acGroups, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        userName = callParamsDict['userName']
        role = callParamsDict['role']
        acGroups = callParamsDict['acGroups']

####+END:

        writeToken(userName, role, acGroups)

    
    def cmndDocStr(self): return """
** Place holder for ICM's experimental or test code.  [[elisp:(org-cycle)][| ]]
 You can use this Cmnd for rapid prototyping and testing of newly developed functions.
"""



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "jwtPlainOutStr" :parsMand "" :parsOpt "userName role acGroups" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /jwtPlainOutStr/ parsMand= parsOpt=userName role acGroups argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class jwtPlainOutStr(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'userName', 'role', 'acGroups', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        userName=None,         # or Cmnd-Input
        role=None,         # or Cmnd-Input
        acGroups=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'userName': userName, 'role': role, 'acGroups': acGroups, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        userName = callParamsDict['userName']
        role = callParamsDict['role']
        acGroups = callParamsDict['acGroups']

####+END:

        outBearerToken = BearerToken()
        outUserInfo = BearerTokenUserInfo()

        if userName: outUserInfo.setUserName(userName)
        if role: outUserInfo.setRole(role)
        if acGroups: outUserInfo.setResGroupIds(acGroups)

        outBearerToken.setUserInfo(outUserInfo)

        bearerTokenStr = outBearerToken.encodeAsJsonStr()

        icm.LOG_here(bearerTokenStr)
        
        base64Str = base64.standard_b64encode(bearerTokenStr)
        
        if interactive:
            print(base64Str)
        else:
            icm.LOG_here(base64Str)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=base64Str,
        )


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "jwtPlainOutFile" :parsMand "" :parsOpt "userName role acGroups" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /jwtPlainOutFile/ parsMand= parsOpt=userName role acGroups argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class jwtPlainOutFile(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'userName', 'role', 'acGroups', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        userName=None,         # or Cmnd-Input
        role=None,         # or Cmnd-Input
        acGroups=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'userName': userName, 'role': role, 'acGroups': acGroups, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        userName = callParamsDict['userName']
        role = callParamsDict['role']
        acGroups = callParamsDict['acGroups']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        outBearerToken = BearerToken()
        outUserInfo = BearerTokenUserInfo()

        if userName: outUserInfo.setUserName(userName)
        if role: outUserInfo.setRole(role)
        if acGroups: outUserInfo.setResGroupIds(acGroups)

        outBearerToken.setUserInfo(outUserInfo)

        bearerTokenStr = outBearerToken.encodeAsJsonStr()

        icm.LOG_here(bearerTokenStr)
        
        base64Str = base64.standard_b64encode(bearerTokenStr)
        
        icm.LOG_here(base64Str)

        outFilePath = self.cmndArgsGet("0", cmndArgsSpecDict, effectiveArgsList)

        icm.LOG_here("Writing BearerToken to {outFilePath}".
                     format(outFilePath=outFilePath,))
        
        with open(outFilePath, 'w') as outfile:  
            outfile.write(base64Str)
    
        outfile.close()    

        

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="outFile",
            argChoices=[],
            argDescription="Name of file to output."
        )

        return cmndArgsSpecDict

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""
        


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "jwtSignedOutStr" :parsMand "" :parsOpt "userName role acGroups" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /jwtSignedOutStr/ parsMand= parsOpt=userName role acGroups argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class jwtSignedOutStr(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'userName', 'role', 'acGroups', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        userName=None,         # or Cmnd-Input
        role=None,         # or Cmnd-Input
        acGroups=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'userName': userName, 'role': role, 'acGroups': acGroups, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        userName = callParamsDict['userName']
        role = callParamsDict['role']
        acGroups = callParamsDict['acGroups']

####+END:

        outBearerToken = BearerToken()
        outUserInfo = BearerTokenUserInfo()

        if userName: outUserInfo.setUserName(userName)
        if role: outUserInfo.setRole(role)
        if acGroups: outUserInfo.setResGroupIds(acGroups)

        outBearerToken.setUserInfo(outUserInfo)

        bearerTokenStr = outBearerToken.encodeAsJsonStr()

        icm.LOG_here(bearerTokenStr)

        bearerTokenDict = outBearerToken.selfAsDict()

        encoded = jwt.encode(bearerTokenDict, 'secret', algorithm='HS256')

        if interactive:
            print(encoded)
        else:
            icm.LOG_here(encoded)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=encoded,
        )



####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "jwtSignedOutFile" :parsMand "" :parsOpt "userName role acGroups" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /jwtSignedOutFile/ parsMand= parsOpt=userName role acGroups argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class jwtSignedOutFile(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'userName', 'role', 'acGroups', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        userName=None,         # or Cmnd-Input
        role=None,         # or Cmnd-Input
        acGroups=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'userName': userName, 'role': role, 'acGroups': acGroups, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        userName = callParamsDict['userName']
        role = callParamsDict['role']
        acGroups = callParamsDict['acGroups']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        outBearerToken = BearerToken()
        outUserInfo = BearerTokenUserInfo()

        if userName: outUserInfo.setUserName(userName)
        if role: outUserInfo.setRole(role)
        if acGroups: outUserInfo.setResGroupIds(acGroups)

        outBearerToken.setUserInfo(outUserInfo)

        bearerTokenStr = outBearerToken.encodeAsJsonStr()

        icm.LOG_here(bearerTokenStr)

        bearerTokenDict = outBearerToken.selfAsDict()

        encoded = jwt.encode(bearerTokenDict, 'secret', algorithm='HS256')

        icm.LOG_here(encoded)        
        
        base64Str = base64.standard_b64encode(bearerTokenStr)
        
        icm.LOG_here(base64Str)

        outFilePath = self.cmndArgsGet("0", cmndArgsSpecDict, effectiveArgsList)

        icm.LOG_here("Writing BearerToken to {outFilePath}".
                     format(outFilePath=outFilePath,))
        
        with open(outFilePath, 'w') as outfile:  
            outfile.write(base64Str)
    
        outfile.close()    



####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="outFile",
            argChoices=[],
            argDescription="Name of file to output."
        )

        return cmndArgsSpecDict

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""
    


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "jwtPlainInFiles" :comment "" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /jwtPlainInFiles/ parsMand= parsOpt= argsMin=1 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class jwtPlainInFiles(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

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

        for each in effectiveArgsList:
            readTokenFromFile(each)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="actionPars",
            argChoices=[],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""
    
        
####+BEGIN: bx:icm:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        
    
####+BEGIN: bx:icm:python:func :funcName "createToken" :funcType "anyOrNone" :retType "any" :deco "default" :argsList "name role group"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /createToken/ retType=any argsList=(name role group) deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def createToken(
    name,
    role,
    group,
):
####+END:
    token = {}
    userInfo={}
    userInfo['userName'] = str(name)
    userInfo['role'] = role.split(',')
    userInfo['acGroups'] = group.split(',')
    token['userInfo'] = userInfo
    return token



####+BEGIN: bx:icm:python:func :funcName "writeToken" :funcType "anyOrNone" :retType "any" :deco "default" :argsList "name role group"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /writeToken/ retType=any argsList=(name role group) deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def writeToken(
    name,
    role,
    group,
):
####+END:
    filePath = 'token.json'
    print(filePath)
    
    token = createToken(name, role, group)
    tokenStr = json.dumps(token)
    print(tokenStr)
    base64Str = base64.standard_b64encode(tokenStr)
    print(base64Str)
    with open(filePath, 'w') as outfile:  
	  outfile.write(base64Str)
    
    outfile.close()    


####+BEGIN: bx:icm:python:func :funcName "readTokenFromFile" :funcType "anyOrNone" :retType "any" :deco "default" :argsList "fileName"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /readTokenFromFile/ retType=any argsList=(fileName) deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def readTokenFromFile(
   fileName,
):
####+END:
    """
** TODO -- NOTEYET -- Needs to be cleaned-up 
"""

   
    data = None

    try: 
        with open (fileName, "r") as thisFile:
            data = thisFile.readlines()    

        print(data)
        
    except Exception as e:
        print("file open failed for {fileName} -- skipping it".format(fileName=fileName))
        return

    decodedStr = base64.standard_b64decode(data[0])
    print(decodedStr)

    return

    """ 
** TODO NOTYET Examples of what to do with the jsonString (decodedStr) 
"""


    json1_data = json.loads(decodedStr)

    pp = pprint.PrettyPrinter(indent=4)    
    pp.pprint(json1_data)
    print(json1_data['userInfo'])
    userInfo = json1_data['userInfo']
    pp.pprint(userInfo['userName'])

    inBearerToken = BearerToken()
    inBearerToken.initFromJsonStr(decodedStr)

    userName = inBearerToken.getUserInfo().getUserName()
    print(userName)

    tokenStr = inBearerToken.encodeAsJsonStr()
    print(tokenStr)


####+BEGIN: bx:dblock:python:class :className "BearerToken" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /BearerToken/ object  [[elisp:(org-cycle)][| ]]
"""
class BearerToken(object):
####+END:
     _expiredAt = None
     _issuedAt = None
     _userInfo = None  # BearerTokenUserInfo
     _userInfoDict = None

     def __init__(self):
         pass

     def initFromJsonStr(
             self,
             jsonStr,
             ):
         """
         """
         jsonData = json.loads(jsonStr)
         
         pp = pprint.PrettyPrinter(indent=4)    
         icm.LOG_here(pp.pformat(jsonData))
         
         self.__class__._userInfoDict = jsonData['userInfo']

         userInfo = BearerTokenUserInfo(jsonData['userInfo'])

         self.setUserInfo(userInfo)

     def encodeAsJsonStr(
             self,
             ):
         """
         """
         tokenDict = self.selfAsDict()

         pp = pprint.PrettyPrinter(indent=4)    
         #icm.LOG_here(pp.pformat(tokenDict))

         tokenStr = json.dumps(tokenDict)

         return( tokenStr )


     def selfAsDict(self):
         selfDict={}

         def setKeyVal(key, value):
             if value:
                 selfDict[key] = value
         
         thisValue = self.getExpiredAt()
         thisKey = 'expiredAt'
         setKeyVal(thisKey, thisValue)

         thisValue = self.getIssuedAt()
         thisKey = 'issuedAt'
         setKeyVal(thisKey, thisValue)

         thisValue = self.getUserInfo()
         if thisValue:
            thisKey = 'userInfo'
            thisValue = thisValue.selfAsDict()
            setKeyVal(thisKey, thisValue)

         return selfDict

         
     def getExpiredAt(self):
         return self.__class__._expiredAt

     def setExpiredAt(self, expiredAt):
         self.__class__._expiredAt = expiredAt

     def getIssuedAt(self):
         return self.__class__._issuedAt

     def setIssuedAt(self, issuedAt):
         self.__class__._issuedAt = issuedAt

     def getUserInfo(self):
         return self.__class__._userInfo

     def setUserInfo(self, userInfo):
         self.__class__._userInfo = userInfo
         


####+BEGIN: bx:dblock:python:class :className "BearerTokenUserInfo" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /BearerTokenUserInfo/ object  [[elisp:(org-cycle)][| ]]
"""
class BearerTokenUserInfo(object):
####+END:
     _userId = None
     _userName = None
     _role = None
     _acGroups = []
     _serviceBlackList = []

     def __init__(
             self,
             userInfoDict=None,
             ):
         if not userInfoDict:
             return

         pp = pprint.PrettyPrinter(indent=4)    
         icm.LOG_here(pp.pformat(userInfoDict))


         if 'userId' in userInfoDict.keys():
             self.setUserId(userInfoDict['userId'])
                            
         if 'userName' in userInfoDict.keys():
             self.setUserName(userInfoDict['userName'])
                              
         if 'role' in userInfoDict.keys():
             self.setRole(userInfoDict['role'])
                          
         if 'acGroups' in userInfoDict.keys():
             self.setResGroupIds(userInfoDict['acGroups'])
                                 
         if 'serviceBlackList' in userInfoDict.keys():
             self.setServiceBlackList(userInfoDict['serviceBlackList'])

     def selfAsDict(self):
         thisDict={}

         def setKeyVal(key, value):
             if value:
                 thisDict[key] = value
         
         thisValue = self.getUserId()
         thisKey = 'userId'
         setKeyVal(thisKey, thisValue)

         thisValue = self.getUserName()
         thisKey = 'userName'
         setKeyVal(thisKey, thisValue)

         thisValue = self.getRole()
         thisKey = 'role'
         setKeyVal(thisKey, thisValue)

         thisValue = self.getResGroupIds()
         thisKey = 'acGroups'
         setKeyVal(thisKey, thisValue)

         thisValue = self.getServiceBlackList()
         thisKey = 'serviceBlackList'
         setKeyVal(thisKey, thisValue)
         
         
         return thisDict
         
         
     def getUserId(self):
         return self.__class__._userId

     def setUserId(self, value):
         self.__class__._userId = value

     def getUserName(self):
         return self.__class__._userName

     def setUserName(self, value):
         self.__class__._userName = value

     def getRole(self):
         return self.__class__._role

     def setRole(self, value):
         self.__class__._role = value

     def getResGroupIds(self):
         return self.__class__._acGroups

     def setResGroupIds(self, value):
         self.__class__._acGroups = value
         
     def getServiceBlackList(self):
         return self.__class__._serviceBlackList

     def setServiceBlackList(self, value):
         self.__class__._serviceBlackList = value
         
     

    
####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
