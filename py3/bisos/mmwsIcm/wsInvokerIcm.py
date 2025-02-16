# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* ::  A /library/ for Web Services Invoker ICMs (wsInvokerIcm) -- make all operations invokable from command line based on swagger sepc input.
"""

####+BEGIN: bx:cs:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
""" #+begin_org
*  This file:/bisos/git/bxRepos/bisos-pip/mmwsIcm/py3/bisos/mmwsIcm/wsInvokerIcm.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
#+end_org """
####+END:


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "wsInvokerIcm"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "202502125349"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

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


from bisos.mmwsIcm import ro

import pprint    
from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient

import re
import requests
import sys
import yaml

from functools import partial
from bravado_core.spec import Spec
from bravado.client import construct_request
from bravado.requests_client import RequestsClient

REPLACEABLE_COMMAND_CHARS = re.compile('[^a-z0-9]+')

#import requests
import logging
import http.client

from urllib.parse import urlparse

import ast


moduleDescription="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

    Given a Service-Specification (svcSpec) as an Open-Api/Swagger URL or FILE,
    digest the svcSpec and map the svcSpec to command-lines of an ICM.

    SvcSpec for invoker should not have a host and a base param. 
    If these exist, they overwrite perfSap which is not desired.

    swagger.yaml does not work with invoker. swagger.json should be used with invoker.
**      [End-Of-Description]
"""
        
moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]
        perfSap: Overwrites host and base in the swagger file.
**      [End-Of-Usage]
"""
        
moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: SvcSpec needs a SvcSpecAdmin.py to strip the base and host for Invoker. [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: origin_url is not same as perfSap. PerfSap should not overwrite it  [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  ICM Common       :: Add -p var=value  -i cmndFpUpdate .  (Where var becomes persitent) and -i cmndFpShow . [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: Add -p headers=fileName  [[elisp:(org-cycle)][| ]]
** DONE [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: Auto generate cmndsList with no args  [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: Instead of parName=parNameVALUE do parName=partType (int64) [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  rinvokerXxxx     :: Create a thin template for using wsIcmInvoker [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: implement body=xx [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: figure if for each body= the json info is known [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: convert all prints to icmLogs [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: change wsInvokerIcm name to wsIcm -- import from unisos.wsIcm wsInvokerIcm wsCommonIcm [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  wsIcmInvoker     :: Add load modules and use loaded options instead of bodyFile  [[elisp:(org-cycle)][| ]]

**      [End-Of-Status]
"""

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
        parName='svcSpec',
        parDescription="URI for OpenApi/Swagger Specification",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--svcSpec',
    )

    csParams.parDictAdd(
        parName='perfSap',
        parDescription="Performer SAP For Constructing Full URLs with end-points",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--perfSap',
    )

    csParams.parDictAdd(
        parName='resource',
        parDescription="Resource Name (end-point)",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--resource',
    )

    csParams.parDictAdd(
        parName='opName',
        parDescription="Operation Name",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--opName',
    )

    csParams.parDictAdd(
        parName='headers',
        parDescription="Headers File",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--headers',
    )
    
    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Common Examples Sections*
"""

####+BEGIN: bx:cs:python:func :funcName "examples_commonInvoker" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "svcSpecUrl svcSpecFile perfSap headers"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_commonInvoker/ retType=bool argsList=(svcSpecUrl svcSpecFile perfSap headers)  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_commonInvoker(
    svcSpecUrl,
    svcSpecFile,
    perfSap,
    headers,
):
####+END:
    """."""
    
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    def headersParam(cps, headers):
        if headers:
            cps['headers'] = headers

    cs.examples.menuChapter('*Service Specification Digestion*')

    cmndName = "svcOpsList"

    if svcSpecUrl:

        cs.examples.menuSection('* -i svcOpsList  svcSpecUrl*')        
        
        cps = cpsInit();
        cps['svcSpec'] = svcSpecUrl
        headersParam(cps, headers)        
        cmndArgs = "";
        menuItem(verbosity='none')
        #cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='full')

        cps = cpsInit();
        cps['svcSpec'] = svcSpecUrl
        cps['perfSap'] = perfSap
        headersParam(cps, headers)                
        cmndArgs = "";
        menuItem(verbosity='none')    

    if svcSpecFile:

        cs.examples.menuSection('* -i svcOpsList  svcSpecFile*')        
        
        # cps = cpsInit();
        # cps['svcSpec'] = svcSpecFile
        # headersParam(cps, headers)                        
        # cmndArgs = "";
        # menuItem(verbosity='none')
        # #cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='full')

        cps = cpsInit();
        cps['svcSpec'] = svcSpecFile

        cps['perfSap'] = perfSap
        headersParam(cps, headers)                        
        cmndArgs = "";
        menuItem(verbosity='none')    
        


####+BEGIN: bx:cs:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:
    

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "svcOpsList" :parsMand "svcSpec" :parsOpt "perfSap headers" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<svcOpsList>>  =verify= parsMand=svcSpec parsOpt=perfSap headers argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class svcOpsList(cs.Cmnd):
    cmndParamsMandatory = [ 'svcSpec', ]
    cmndParamsOptional = [ 'perfSap', 'headers', ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             svcSpec: typing.Optional[str]=None,  # Cs Mandatory Param
             perfSap: typing.Optional[str]=None,  # Cs Optional Param
             headers: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'svcSpec': svcSpec, 'perfSap': perfSap, 'headers': headers, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        svcSpec = csParam.mappedValue('svcSpec', svcSpec)
        perfSap = csParam.mappedValue('perfSap', perfSap)
        headers = csParam.mappedValue('headers', headers)
####+END:

        b_io.tm.here("svcSpec={svcSpec} -- perfSap={perfSap}".format(svcSpec=svcSpec, perfSap=perfSap))

        try:         
            loadedSvcSpec, origin_url = loadSvcSpec(svcSpec, perfSap)
        except Exception as e:            
            b_io.eh.problem_usageError("wsInvokerIcm.svcOpsList Failed -- svcSpec={svcSpec}".format(
                svcSpec=svcSpec,
            ))
            b_io.eh.critical_exception(e)
            return

        pp = pprint.PrettyPrinter(indent=4)
        b_io.tm.here("{}".format(pp.pformat(loadedSvcSpec)))
        

        processSvcSpec(loadedSvcSpec, origin_url, perfSap, headers, svcSpec)



    
    def cmndDocStr(self): return """
** List as ICM invokavles, based on svcSpc. [[elisp:(org-cycle)][| ]]
   Loads svcSpec into python core and passes that to processSvcSpec. 
"""


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "rinvoke" :parsMand "svcSpec resource opName" :parsOpt "perfSap headers" :argsMin 0 :argsMax 999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<rinvoke>>  =verify= parsMand=svcSpec resource opName parsOpt=perfSap headers argsMax=999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class rinvoke(cs.Cmnd):
    cmndParamsMandatory = [ 'svcSpec', 'resource', 'opName', ]
    cmndParamsOptional = [ 'perfSap', 'headers', ]
    cmndArgsLen = {'Min': 0, 'Max': 999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             svcSpec: typing.Optional[str]=None,  # Cs Mandatory Param
             resource: typing.Optional[str]=None,  # Cs Mandatory Param
             opName: typing.Optional[str]=None,  # Cs Mandatory Param
             perfSap: typing.Optional[str]=None,  # Cs Optional Param
             headers: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'svcSpec': svcSpec, 'resource': resource, 'opName': opName, 'perfSap': perfSap, 'headers': headers, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        svcSpec = csParam.mappedValue('svcSpec', svcSpec)
        resource = csParam.mappedValue('resource', resource)
        opName = csParam.mappedValue('opName', opName)
        perfSap = csParam.mappedValue('perfSap', perfSap)
        headers = csParam.mappedValue('headers', headers)
####+END:

        opParsList = self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList)

        b_io.tm.here("svcSpec={svcSpec} -- perfSap={perfSap}".format(svcSpec=svcSpec, perfSap=perfSap))

        #generateSvcInfo("http://localhost:8080/swagger.json")
        loadedSvcSpec, origin_url = loadSvcSpec(svcSpec, perfSap)

        if perfSap:
            #origin_url = "http://localhost:8080"
            origin_url = perfSap

        pp = pprint.PrettyPrinter(indent=4)
        b_io.tm.here("{}".format(pp.pformat(loadedSvcSpec)))

        op = getOperationWithResourceAndOpName(
            loadedSvcSpec,
            origin_url,
            resource,
            opName
            )

        
        opInvokeEvalStr="opInvoke(headers, op, "
        for each in opParsList:
            parVal = each.split("=")
            parValLen = len(parVal)

            if parValLen == 2:
                parName=parVal[0]
                parValue=parVal[1]
            else:
                b_io.eh.problem_usageError("Expected 2: {parValLen}".format(parValLen=parValLen) )               
                continue
            
            opInvokeEvalStr = opInvokeEvalStr + """{parName}="{parValue}", """.format(
                parName=parName, parValue=parValue
                )
            
        opInvokeEvalStr = opInvokeEvalStr + ")"
        b_io.tm.here("Invoking With Eval: str={opInvokeEvalStr}".format(opInvokeEvalStr=opInvokeEvalStr,))

        eval(opInvokeEvalStr)
        
        return

    
    def cmndDocStr(self): return """
** Creates the opInvoke string and evals opInvoke.  [[elisp:(org-cycle)][| ]]
"""

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
            argPosition="0&-1",
            argName="actionPars",
            argDefault=None,
            argChoices='any',
            argDescription="Rest of args for use by action"
            )

        return cmndArgsSpecDict
        
    
        
####+BEGIN: bx:cs:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:cs:python:func :funcName "loggingSetup" :funcType "void" :retType "bool" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-void     [[elisp:(outline-show-subtree+toggle)][||]] /loggingSetup/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def loggingSetup():
####+END:
    # Debug logging
    logControler = b_io.log.Control()
    icmLogger = logControler.loggerGet()
    
    icmLogLevel = logControler.level
    #icmLogLevel = logControler.loggerGetLevel()  # Use This After ICM has been updated

    def requestsDebugLog():
        http.client.HTTPConnection.debuglevel = 1
        #logging.basicConfig()
        if icmLogLevel:
            if icmLogLevel <= 10:
                logging.getLogger().setLevel(logging.DEBUG)
        req_log = logging.getLogger('requests.packages.urllib3')
        req_log.setLevel(logging.DEBUG)
        req_log.propagate = True

    if icmLogLevel:
        if icmLogLevel <= 15:
            requestsDebugLog()

    
####+BEGIN: bx:cs:python:func :funcName "loadSvcSpec" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "spec perfSapUrl"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /loadSvcSpec/ retType=bool argsList=(spec perfSapUrl) deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def loadSvcSpec(
    spec,
    perfSapUrl,
):
####+END:
    """Returns a dictionary -- perfSap is unused"""
    origin_url = None

    if isinstance(spec, str):
        if spec.startswith('https://') or spec.startswith('http://'):
            origin_url = spec
            r = requests.get(spec, verify=False)
            r.raise_for_status()
            spec = yaml.safe_load(r.text)
        else:
            with open(spec, 'rb') as fd:
                spec = yaml.safe_load(fd.read())

        #
        # NOTYET, perhaps this way of loading it would be more reliable
        #
        #from bravado.client import SwaggerClient
        #from bravado.swagger_model import load_file
        #spec_dict = load_file(spec_path)

    if perfSapUrl:
        perfSapUrlObj = urlparse(perfSapUrl)

        # NOTYET, levae as LOG
        # b_io.tm.here("perfSap: host={host} port={port} path={path}".format(
        #     host = perfSapUrlObj.hostname,
        #     port = perfSapUrlObj.port,
        #     path = perfSapUrlObj.path,
        # ))
    
        spec['host'] = '{}:{}'.format(perfSapUrlObj.hostname, perfSapUrlObj.port)

        if perfSapUrlObj.path:
            spec['basePath'] = perfSapUrlObj.path

    spec = sanitize_spec(spec)
    return spec, origin_url


####+BEGIN: bx:cs:python:func :funcName "processSvcSpec" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "spec origin_url perfSap headers svcSpec"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /processSvcSpec/ retType=bool argsList=(spec origin_url perfSap headers svcSpec) deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def processSvcSpec(
    spec,
    origin_url,
    perfSap,
    headers,
    svcSpec,
):
####+END:
    """ Prints a list of ICM invokable commands.
"""
    pp = pprint.PrettyPrinter(indent=4)

    spec = Spec.from_dict(spec, origin_url=origin_url)
    #b_io.tm.here(pp.pformat(spec))

    thisIcm = G.icmMyName()

    perfSapStr = ""
    if perfSap:
        perfSapStr = "--perfSap={perfSap} ".format(perfSap=perfSap)

    headersStr = ""
    if headers:
        headersStr = "--headers={headers} ".format(headers=headers)

    if origin_url:
        svcSpecStr = origin_url
    else:
        svcSpecStr = svcSpec
        
    for res_name, res in list(spec.resources.items()):
        for op_name, op in list(res.operations.items()):
            name = get_command_name(op)

            paramsListStr = ""
            optionalOrRequired = ""
            for param_name, param in list(op.params.items()):
                if param.required:
                    optionalOrRequired = "required_"
                else:
                    optionalOrRequired = "optional_"
                paramsListStr = paramsListStr + " {param_name}={optionalOrRequired}".format(
                    param_name=param_name, optionalOrRequired=optionalOrRequired,)
                    
                #print(param.required)
                #print(param.name)
                #print(param.type)                

            #icm.OUT_note("{thisIcm} --svcSpec={svcSpec} {perfSapStr} {headersStr} --resource={res_name} --opName={op_name} -i rinvoke {paramsListStr}".format(
            print(("{thisIcm} --svcSpec={svcSpec} {perfSapStr} {headersStr} --resource={res_name} --opName={op_name} -i rinvoke {paramsListStr}".format(            
                thisIcm=thisIcm,
                svcSpec=svcSpecStr,
                perfSapStr=perfSapStr,
                headersStr=headersStr,                                                                      
                res_name=res_name,
                op_name=op_name,
                paramsListStr=paramsListStr,
                )
            ))
                
                
####+BEGIN: bx:cs:python:func :funcName "getOperationWithResourceAndOpName" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "spec origin_url resource opName"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /getOperationWithResourceAndOpName/ retType=bool argsList=(spec origin_url resource opName) deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def getOperationWithResourceAndOpName(
    spec,
    origin_url,
    resource,
    opName,
):
####+END:
    """Returns op object."""

    pp = pprint.PrettyPrinter(indent=4)

    spec = Spec.from_dict(spec, origin_url=origin_url)        
    #pp.pprint(spec)
    
    for res_name, res in list(spec.resources.items()):
        if res_name != resource:
            continue

        for op_name, op in list(res.operations.items()):
            if op_name != opName:
                continue
            
            name = get_command_name(op)

            b_io.tm.here("Invoking: resource={resource}  opName={opName}".format(
                resource=resource, opName=op_name))

            return op


####+BEGIN: bx:cs:python:func :funcName "get_command_name" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "op"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /get_command_name/ retType=bool argsList=(op)  [[elisp:(org-cycle)][| ]]
#+end_org """
def get_command_name(
    op,
):
####+END:
    if op.http_method == 'get' and '{' not in op.path_name:
        return 'list'
    elif op.http_method == 'put':
        return 'update'
    else:
        return op.http_method


####+BEGINNOT: bx:cs:python:func :funcName "opInvoke" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "headers op *args **kwargs"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /opInvoke/ retType=bool argsList=(headers op *args **kwargs)  [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)    
def opInvoke(
    headers,
    op,
    *args,
    **kwargs
):
####+END:
    """ NOTYET, Important, opInvoke should be layered on  top of opInvokeCapture """

    pp = pprint.PrettyPrinter(indent=4)

    headerLines = list()
    if headers:
        with open(headers, 'rb') as file:
            headerLines = file.readlines()
        
    # else:
    #     print("Has No Headers")

    headerLinesAsDict = dict()
    for each in headerLines:
        headerLineAsList = each.split(":")
        headerLineAsListLen = len(headerLineAsList)
        
        if headerLineAsListLen == 2:
            headerLineTag = headerLineAsList[0]
            headerLineValue = headerLineAsList[1]
        else:
            b_io.eh.problem_usageError("Expected 2: {}".format(headerLineAsListLen))
            continue

        headerLinesAsDict[headerLineTag] = headerLineValue.lstrip(' ').rstrip()

    requestOptions = dict()

    if headerLinesAsDict:
        requestOptions["headers"] = headerLinesAsDict


    def bodyArgToDict(
        bodyAny,
        bodyFile,
        bodyStr,
        bodyFunc,        
    ):
        """ Returns None if all Args were None, and returns "" if one of the args was "", Otherwize a dict or {}."""
        
        def bodyStrAsDict(bodyStr):
            return ast.literal_eval(bodyStr)            

        def bodyFileAsDict(bodyFile):
            with open(bodyFile, 'r') as myfile:
                data=myfile.read().replace('\n', '')
            return ast.literal_eval(data)

        def bodyFuncAsDict(bodyFunc):
            resDict = eval(bodyFunc)
            # NOTYET, verify that we have a dict
            return resDict
        
        if bodyAny != None:
            b_io.tm.here("bodyAny={}".format(pp.pformat(bodyAny)))
            
            if bodyAny == "":
                return ""
            
            # Be it file, function or string
            if os.path.isfile(bodyAny):
                return bodyFileAsDict(bodyAny)
            elif bodyAny == "NOTYET-valid func":
                return bodyFuncAsDict(bodyAny)
            else:
                # We then take bodyAny to be a string
                return bodyStrAsDict(bodyAny)
            
        elif bodyFile != None:
            b_io.tm.here("bodyFile={}".format(pp.pformat(bodyFile)))
            
            if bodyFile == "":
                return ""
            
            if os.path.isfile(bodyAny):
                return bodyFileAsDict(bodyFile)
            else:
                return {}

        elif bodyFunc != None:
            b_io.tm.here("bodyFunc={}".format(pp.pformat(bodyFunc)))
            
            if bodyFunc == "":
                return ""

            if bodyFunc == "NOTYET-valid func":
                return bodyFuncAsDict(bodyFunc)
            else:
                return {}
            

        elif bodyStr != None:
            b_io.tm.here("bodyStr={}".format(pp.pformat(bodyStr)))
            
            if bodyStr == "":
                return ""
            
            bodyValue = bodyStrAsDict(bodyStr)
            return bodyValue

        else:
            # So they were all None, meaning that no form of "body" was specified.
            return None

    # b_io.tm.here("Args: {}".format(args))
    # for key in kwargs:
    #      b_io.tm.here("another keyword arg: %s: %s" % (key, kwargs[key]))
        

    bodyAny = kwargs.pop('body', None)
    bodyFile = kwargs.pop('bodyFile', None)
    bodyStr = kwargs.pop('bodyStr', None)
    bodyFunc = kwargs.pop('bodyFunc', None)

    bodyValue = bodyArgToDict(bodyAny, bodyFile, bodyStr, bodyFunc)

    b_io.tm.here(pp.pformat(requestOptions))
    
    if bodyValue == None:
        request = construct_request(op, requestOptions, **kwargs)
    elif bodyValue == "":
        # Causes An Exception That Describes Expected Dictionary
        request = construct_request(op, requestOptions, body=None, **kwargs)
    else:
        request = construct_request(op, requestOptions, body=bodyValue, **kwargs)

        
    b_io.tm.here("request={request}".format(request=pp.pformat(request)))

    c = RequestsClient()

    future = c.request(request)

    try:
        result = future.result()
    except Exception as e:            
        #io.eh.critical_exception(e)
        result = None

    if result:
        b_io.tm.here("responseHeaders: {headers}".format(
            headers=pp.pformat(result._delegate.headers)))

        b_io.ann.write("Operation Status: {result}".format(result=result))

        b_io.ann.write("Operation Result: {result}".format(
            result=pp.pformat(result.json()))
        )
    


####+BEGIN: bx:cs:python:func :funcName "ro_opInvokeCapture" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "roOp"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /ro_opInvokeCapture/ retType=bool argsList=(roOp) deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def ro_opInvokeCapture(
    roOp,
):
####+END:


    pp = pprint.PrettyPrinter(indent=4)    

    #b_io.tm.here("svcSpec={svcSpec} -- perfSap={perfSap}".format(svcSpec=roOp.svcSpec, perfSap=roOp.perfSap))

    loadedSvcSpec, origin_url = loadSvcSpec(roOp.svcSpec, roOp.perfSap)

    if roOp.perfSap:
        #origin_url = "http://localhost:8080"
        origin_url = roOp.perfSap

    #
    # NOTYET LOG level changes here
    #
    #b_io.tm.here("{}".format(pp.pformat(loadedSvcSpec)))

    opBravadoObj = getOperationWithResourceAndOpName(
        loadedSvcSpec,
        origin_url,
        roOp.resource,
        roOp.opName,
        )

    if not opBravadoObj:
        b_io.eh.problem_usageError(
            """getOperationWithResourceAndOpName Failed: resource={resource} opName={opName}""".format(
                resource=roOp.resource,
                opName=roOp.opName,
            ))
        return None

    
    requestOptions = dict()

    params = roOp.roParams

    headerParams = params.headerParams
    if headerParams:
        requestOptions["headers"] = headerParams

    urlParams = params.urlParams
    if urlParams == None:
        urlParams = dict()

    bodyParams = params.bodyParams
    b_io.tm.here("{}".format(pp.pformat(bodyParams)))
    if bodyParams:
        #
        # With ** we achieve kwargs
        #
        #  func(**{'type':'Event'}) is equivalent to func(type='Event')
        #
        request = construct_request(
            opBravadoObj,
            requestOptions,
            body=bodyParams,
            **urlParams
            )
    else:
        request = construct_request(
            opBravadoObj,
            requestOptions,
            **urlParams           
            )
        
    b_io.tm.here("request={request}".format(request=pp.pformat(request)))

    c = RequestsClient()


    #
    # This is where the invoke request goes out
    #
    future = c.request(request)

    #
    # This where the invoke response comes in
    #

    opResults = {}
    try:
        result = future.result()
    except Exception as e:            
        #io.eh.critical_exception(e)
        opResults = None

        roResults = ro.Ro_Results(
            httpResultCode=500,    # type=int
            httpResultText="Internal Server Error",         # type=str
            opResults=opResults,
            opResultHeaders=None,
            )
        
    if opResults != None:

        #
        # result
        #
        # 2018-10-01 -- https://github.com/Yelp/bravado/blob/master/bravado/requests_client.py
        # class RequestsResponseAdapter(IncomingResponse):
        #
        # type(result._delegate.text) = unicode
        # type(result._delegate.content) = str
        #


        opResults=None    

        if result._delegate.content:
            try:
                opResults=result.json()
            except Exception as e:            
                b_io.eh.critical_exception(e)
                opResults=None

        roResults = ro.Ro_Results(
            httpResultCode=result._delegate.status_code,    # type=int
            httpResultText=result._delegate.reason,         # type=str
            opResults=opResults,
            opResultHeaders=result._delegate.headers,
            )

        b_io.tm.here("RESPONSE: status_code={status_code} -- reason={reason} -- text={text}".format(
            status_code=result._delegate.status_code,
            reason=result._delegate.reason,        
            text=result._delegate.text,
            ))

        b_io.tm.here("RESPONSE: responseHeaders: {headers}".format(
            headers=pp.pformat(result._delegate.headers)))

    roOp.roResults = roResults
    
    return roOp


####+BEGIN: bx:cs:python:func :funcName "invokeCapture" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "op"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /invokeCapture/ retType=bool argsList=(op) deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def invokeCapture(
    op,
):
####+END:
    print(op)
    
    print((op.svcSpec))

    cmndOutcome = wsInvokerIcm.rinvoke().cmnd(
        interactive=False,
        svcSpec=op.svcSpec,
        resource=op.resource,
        opName=op.opName,
        perfSap=op.perfSap,
        argsList="", 
        )
    
    return( cmndOutcome )
    
    

    
def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.


    Usage:
    req = requests.Request('POST','http://stackoverflow.com',headers={'X-Custom':'Test'},data='a=1&b=2')
    prepared = req.prepare()
    pretty_print_POST(prepared)
    """
    print(('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in list(req.headers.items())),
        req.body,
    )))
    
    
    
####+BEGIN: bx:cs:python:func :funcName "sanitize_spec" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "spec"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /sanitize_spec/ retType=bool argsList=(spec)  [[elisp:(org-cycle)][| ]]
#+end_org """
def sanitize_spec(
    spec,
):
####+END:
    for path, path_obj in list(spec['paths'].items()):
        # remove root paths as no resource name can be found for it
        if path == '/':
            del spec['paths'][path]
    return spec

    

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _ ~End Of Editable Text~ _: |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:
