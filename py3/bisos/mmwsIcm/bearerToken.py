# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* ::  A /library/ for generating, validating  and decoding bearer tokens.
"""


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "bearerToken"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "202502124022"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Beta"
__status__ = "Beta"
####+END:

__credits__ = [""]

####+BEGINNOT: bx:dblock:global:file-insert-cond :cond "./blee.el" :file ""
csInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
}
####+END:

####+BEGIN: bx:cs:python:topControls 
""" #+begin_org
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:


####+BEGIN: bx:cs:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:


####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Imports=  [[elisp:(outline-show-subtree+toggle)][||]] *IMPORTS*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGINNOT: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] *Imports* =Based on Classification=cs-u=
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

import os
import collections
import enum

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
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:cs:python:subSection :title "Common Arguments Specification"

####+END:

####+BEGIN: bx:cs:python:func :funcName "commonParamsSpecify" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "csParams"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/ retType=bool argsList=(csParams)  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
    csParams,
):
####+END:

    csParams.parDictAdd(
        parName='userName',
        parDescription="Name Of The User",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--userName',
    )

    csParams.parDictAdd(
        parName='role',
        parDescription="User Role",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--role',
    )

    csParams.parDictAdd(
        parName='acGroups',
        parDescription="Resource Group IDs",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--acGroups',
    )

    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]        *Common Examples Sections*
"""

####+BEGIN: bx:cs:python:func :funcName "examples_tokenGenerator" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "userName role acGroups"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_tokenGenerator/ retType=bool argsList=(userName role acGroups)  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_tokenGenerator(
    userName,
    role,
    acGroups,
):
####+END:
    """."""
    
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    cs.examples.menuChapter('*= bearerToken CmndsLib: Token Manager -- Output / Input =*')

    cs.examples.menuSection('* -i jwtPlain*')

    cmndName = "jwtPlainOutStr"

    cps = cpsInit();
    cps['userName'] = userName
    cps['role'] = role
    cps['acGroups'] = acGroups       
    cmndArgs = "";
    menuItem(verbosity='none')
    #cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='full')

    cmndName = "jwtPlainOutFile"

    cps = cpsInit();
    cps['userName'] = userName
    cps['role'] = role
    cps['acGroups'] = acGroups       
    cmndArgs = "/tmp/bearerPlain.json";
    menuItem(verbosity='none')

    cs.examples.menuSection('* -i jwtSigned*')

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


    cs.examples.menuSection('* -i jwtPlainInput*')

    cmndName = "jwtPlainInFiles"

    cps = cpsInit();
    cmndArgs = "/tmp/bearerPlain.json";
    menuItem(verbosity='none')
    
    


####+BEGIN: bx:cs:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:
    

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "tokenOutput" :comment "OBSOLETED" :parsMand "" :parsOpt "userName role acGroups" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<tokenOutput>>  *OBSOLETED*  =verify= parsOpt=userName role acGroups ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class tokenOutput(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'userName', 'role', 'acGroups', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             userName: typing.Optional[str]=None,  # Cs Optional Param
             role: typing.Optional[str]=None,  # Cs Optional Param
             acGroups: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:
        """OBSOLETED"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'userName': userName, 'role': role, 'acGroups': acGroups, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        userName = csParam.mappedValue('userName', userName)
        role = csParam.mappedValue('role', role)
        acGroups = csParam.mappedValue('acGroups', acGroups)
####+END:

        writeToken(userName, role, acGroups)

    
    def cmndDocStr(self): return """
** Place holder for ICM's experimental or test code.  [[elisp:(org-cycle)][| ]]
 You can use this Cmnd for rapid prototyping and testing of newly developed functions.
"""



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "jwtPlainOutStr" :parsMand "" :parsOpt "userName role acGroups" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<jwtPlainOutStr>>  =verify= parsOpt=userName role acGroups ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class jwtPlainOutStr(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'userName', 'role', 'acGroups', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             userName: typing.Optional[str]=None,  # Cs Optional Param
             role: typing.Optional[str]=None,  # Cs Optional Param
             acGroups: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'userName': userName, 'role': role, 'acGroups': acGroups, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        userName = csParam.mappedValue('userName', userName)
        role = csParam.mappedValue('role', role)
        acGroups = csParam.mappedValue('acGroups', acGroups)
####+END:

        outBearerToken = BearerToken()
        outUserInfo = BearerTokenUserInfo()

        if userName: outUserInfo.setUserName(userName)
        if role: outUserInfo.setRole(role)
        if acGroups: outUserInfo.setResGroupIds(acGroups)

        outBearerToken.setUserInfo(outUserInfo)

        bearerTokenStr = outBearerToken.encodeAsJsonStr()

        b_io.tm.here(bearerTokenStr)
        
        base64Str = base64.standard_b64encode(bearerTokenStr)
        
        if rtInv.outs:
            print(base64Str)
        else:
            b_io.tm.here(base64Str)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=base64Str,
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "jwtPlainOutFile" :parsMand "" :parsOpt "userName role acGroups" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<jwtPlainOutFile>>  =verify= parsOpt=userName role acGroups argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class jwtPlainOutFile(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'userName', 'role', 'acGroups', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             userName: typing.Optional[str]=None,  # Cs Optional Param
             role: typing.Optional[str]=None,  # Cs Optional Param
             acGroups: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'userName': userName, 'role': role, 'acGroups': acGroups, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        userName = csParam.mappedValue('userName', userName)
        role = csParam.mappedValue('role', role)
        acGroups = csParam.mappedValue('acGroups', acGroups)
####+END:

        outBearerToken = BearerToken()
        outUserInfo = BearerTokenUserInfo()

        if userName: outUserInfo.setUserName(userName)
        if role: outUserInfo.setRole(role)
        if acGroups: outUserInfo.setResGroupIds(acGroups)

        outBearerToken.setUserInfo(outUserInfo)

        bearerTokenStr = outBearerToken.encodeAsJsonStr()

        b_io.tm.here(bearerTokenStr)
        
        base64Str = base64.standard_b64encode(bearerTokenStr)
        
        b_io.tm.here(base64Str)

        outFilePath = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)

        b_io.tm.here("Writing BearerToken to {outFilePath}".
                     format(outFilePath=outFilePath,))
        
        with open(outFilePath, 'w') as outfile:  
            outfile.write(base64Str)
    
        outfile.close()    

        

####+BEGIN: b:py3:cs:method/typing :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="outFile",
            argChoices=[],
            argDescription="Name of file to output."
        )

        return cmndArgsSpecDict

####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndDocStr/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(
####+END:
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""
        


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "jwtSignedOutStr" :parsMand "" :parsOpt "userName role acGroups" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<jwtSignedOutStr>>  =verify= parsOpt=userName role acGroups ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class jwtSignedOutStr(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'userName', 'role', 'acGroups', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             userName: typing.Optional[str]=None,  # Cs Optional Param
             role: typing.Optional[str]=None,  # Cs Optional Param
             acGroups: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'userName': userName, 'role': role, 'acGroups': acGroups, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        userName = csParam.mappedValue('userName', userName)
        role = csParam.mappedValue('role', role)
        acGroups = csParam.mappedValue('acGroups', acGroups)
####+END:

        outBearerToken = BearerToken()
        outUserInfo = BearerTokenUserInfo()

        if userName: outUserInfo.setUserName(userName)
        if role: outUserInfo.setRole(role)
        if acGroups: outUserInfo.setResGroupIds(acGroups)

        outBearerToken.setUserInfo(outUserInfo)

        bearerTokenStr = outBearerToken.encodeAsJsonStr()

        b_io.tm.here(bearerTokenStr)

        bearerTokenDict = outBearerToken.selfAsDict()

        encoded = jwt.encode(bearerTokenDict, 'secret', algorithm='HS256')

        if rtInv.outs:
            print(encoded)
        else:
            b_io.tm.here(encoded)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=encoded,
        )



####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndDocStr/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(
####+END:
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "jwtSignedOutFile" :parsMand "" :parsOpt "userName role acGroups" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<jwtSignedOutFile>>  =verify= parsOpt=userName role acGroups argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class jwtSignedOutFile(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'userName', 'role', 'acGroups', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             userName: typing.Optional[str]=None,  # Cs Optional Param
             role: typing.Optional[str]=None,  # Cs Optional Param
             acGroups: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'userName': userName, 'role': role, 'acGroups': acGroups, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        userName = csParam.mappedValue('userName', userName)
        role = csParam.mappedValue('role', role)
        acGroups = csParam.mappedValue('acGroups', acGroups)
####+END:

        outBearerToken = BearerToken()
        outUserInfo = BearerTokenUserInfo()

        if userName: outUserInfo.setUserName(userName)
        if role: outUserInfo.setRole(role)
        if acGroups: outUserInfo.setResGroupIds(acGroups)

        outBearerToken.setUserInfo(outUserInfo)

        bearerTokenStr = outBearerToken.encodeAsJsonStr()

        b_io.tm.here(bearerTokenStr)

        bearerTokenDict = outBearerToken.selfAsDict()

        encoded = jwt.encode(bearerTokenDict, 'secret', algorithm='HS256')

        b_io.tm.here(encoded)        
        
        base64Str = base64.standard_b64encode(bearerTokenStr)
        
        b_io.tm.here(base64Str)

        outFilePath = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)

        b_io.tm.here("Writing BearerToken to {outFilePath}".
                     format(outFilePath=outFilePath,))
        
        with open(outFilePath, 'w') as outfile:  
            outfile.write(base64Str)
    
        outfile.close()    



####+BEGIN: b:py3:cs:method/typing :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="outFile",
            argChoices=[],
            argDescription="Name of file to output."
        )

        return cmndArgsSpecDict

####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndDocStr/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(
####+END:
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""
    


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "jwtPlainInFiles" :comment "" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<jwtPlainInFiles>>  =verify= argsMin=1 argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class jwtPlainInFiles(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:

        for each in effectiveArgsList:
            readTokenFromFile(each)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/typing :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="actionPars",
            argChoices=[],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict

####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndDocStr/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(
####+END:
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""
    
        
####+BEGIN: bx:cs:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:
        
    
####+BEGIN: bx:cs:python:func :funcName "createToken" :funcType "anyOrNone" :retType "any" :deco "default" :argsList "name role group"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /createToken/ retType=any argsList=(name role group) deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
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



####+BEGIN: bx:cs:python:func :funcName "writeToken" :funcType "anyOrNone" :retType "any" :deco "default" :argsList "name role group"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /writeToken/ retType=any argsList=(name role group) deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
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


####+BEGIN: bx:cs:python:func :funcName "readTokenFromFile" :funcType "anyOrNone" :retType "any" :deco "default" :argsList "fileName"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /readTokenFromFile/ retType=any argsList=(fileName) deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
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
        print(("file open failed for {fileName} -- skipping it".format(fileName=fileName)))
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
    print((json1_data['userInfo']))
    userInfo = json1_data['userInfo']
    pp.pprint(userInfo['userName'])

    inBearerToken = BearerToken()
    inBearerToken.initFromJsonStr(decodedStr)

    userName = inBearerToken.getUserInfo().getUserName()
    print(userName)

    tokenStr = inBearerToken.encodeAsJsonStr()
    print(tokenStr)


####+BEGIN: b:py3:class/decl :className "BearerToken" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /BearerToken/  superClass=object  [[elisp:(org-cycle)][| ]]
#+end_org """
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
         b_io.tm.here(pp.pformat(jsonData))
         
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
         #b_io.tm.here(pp.pformat(tokenDict))

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
         


####+BEGIN: b:py3:class/decl :className "BearerTokenUserInfo" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /BearerTokenUserInfo/  superClass=object  [[elisp:(org-cycle)][| ]]
#+end_org """
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
         b_io.tm.here(pp.pformat(userInfoDict))


         if 'userId' in list(userInfoDict.keys()):
             self.setUserId(userInfoDict['userId'])
                            
         if 'userName' in list(userInfoDict.keys()):
             self.setUserName(userInfoDict['userName'])
                              
         if 'role' in list(userInfoDict.keys()):
             self.setRole(userInfoDict['role'])
                          
         if 'acGroups' in list(userInfoDict.keys()):
             self.setResGroupIds(userInfoDict['acGroups'])
                                 
         if 'serviceBlackList' in list(userInfoDict.keys()):
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
         
     

    
####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _ ~End Of Editable Text~ _: |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:
