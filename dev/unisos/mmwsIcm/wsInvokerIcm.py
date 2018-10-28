# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* ::  A /library/ for Web Services Invoker ICMs (wsInvokerIcm) -- make all operations invokable from command line based on swagger sepc input.
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/unisos/mmwsIcm/dev/unisos/mmwsIcm/wsInvokerIcm.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM). Part Of ByStar.
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 Warning: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "wsInvokerIcm"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201810164344"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icmInfo-mbNedaGpl.py"
icmInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'copyright':       "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]",
    'licenses':        ["[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
    'partOf':          ["[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]",]
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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
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

from unisos.mmwsIcm import ro

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
import httplib

from urlparse import urlparse

import ast


####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "icmBegin_libOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || ICM-Cmnd       :: /icmBegin_libOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Func-anyOrNone :: /commonParamsSpecify/ retType=bool argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:

    icmParams.parDictAdd(
        parName='svcSpec',
        parDescription="URI for OpenApi/Swagger Specification",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--svcSpec',
    )

    icmParams.parDictAdd(
        parName='perfSap',
        parDescription="Performer SAP For Constructing Full URLs with end-points",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--perfSap',
    )

    icmParams.parDictAdd(
        parName='resource',
        parDescription="Resource Name (end-point)",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--resource',
    )

    icmParams.parDictAdd(
        parName='opName',
        parDescription="Operation Name",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--opName',
    )

    icmParams.parDictAdd(
        parName='headers',
        parDescription="Headers File",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--headers',
    )
    
    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Common Examples Sections*
"""

####+BEGIN: bx:icm:python:func :funcName "examples_commonInvoker" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "svcSpecUrl svcSpecFile perfSap headers"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Func-anyOrNone :: /examples_commonInvoker/ retType=bool argsList=(svcSpecUrl svcSpecFile perfSap headers)  [[elisp:(org-cycle)][| ]]
"""
def examples_commonInvoker(
    svcSpecUrl,
    svcSpecFile,
    perfSap,
    headers,
):
####+END:
    """."""
    
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    def headersParam(cps, headers):
        if headers:
            cps['headers'] = headers

    icm.cmndExampleMenuChapter('*Service Specification Digestion*')

    cmndName = "svcOpsList"

    if svcSpecUrl:

        icm.cmndExampleMenuSection('* -i svcOpsList  svcSpecUrl*')        
        
        cps = cpsInit();
        cps['svcSpec'] = svcSpecUrl
        headersParam(cps, headers)        
        cmndArgs = "";
        menuItem(verbosity='none')
        #icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')

        cps = cpsInit();
        cps['svcSpec'] = svcSpecUrl
        cps['perfSap'] = perfSap
        headersParam(cps, headers)                
        cmndArgs = "";
        menuItem(verbosity='none')    

    if svcSpecFile:

        icm.cmndExampleMenuSection('* -i svcOpsList  svcSpecFile*')        
        
        # cps = cpsInit();
        # cps['svcSpec'] = svcSpecFile
        # headersParam(cps, headers)                        
        # cmndArgs = "";
        # menuItem(verbosity='none')
        # #icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')

        cps = cpsInit();
        cps['svcSpec'] = svcSpecFile

        cps['perfSap'] = perfSap
        headersParam(cps, headers)                        
        cmndArgs = "";
        menuItem(verbosity='none')    
        


####+BEGIN: bx:icm:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
    

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "svcOpsList" :parsMand "svcSpec" :parsOpt "perfSap headers" :argsMin "0" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || ICM-Cmnd       :: /svcOpsList/ parsMand=svcSpec parsOpt=perfSap headers argsMin=0 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class svcOpsList(icm.Cmnd):
    cmndParamsMandatory = [ 'svcSpec', ]
    cmndParamsOptional = [ 'perfSap', 'headers', ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        svcSpec=None,         # or Cmnd-Input
        perfSap=None,         # or Cmnd-Input
        headers=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'svcSpec': svcSpec, 'perfSap': perfSap, 'headers': headers, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        svcSpec = callParamsDict['svcSpec']
        perfSap = callParamsDict['perfSap']
        headers = callParamsDict['headers']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        icm.TM_here("svcSpec={svcSpec} -- perfSap={perfSap}".format(svcSpec=svcSpec, perfSap=perfSap))

        try:         
            loadedSvcSpec, origin_url = loadSvcSpec(svcSpec, perfSap)
        except Exception as e:            
            icm.EH_problem_usageError("wsInvokerIcm.svcOpsList Failed -- svcSpec={svcSpec}".format(
                svcSpec=svcSpec,
            ))
            icm.EH_critical_exception(e)
            return

        pp = pprint.PrettyPrinter(indent=4)
        icm.TM_here("{}".format(pp.pformat(loadedSvcSpec)))
        

        processSvcSpec(loadedSvcSpec, origin_url, perfSap, headers, svcSpec)



    
    def cmndDocStr(self): return """
** List as ICM invokavles, based on svcSpc. [[elisp:(org-cycle)][| ]]
   Loads svcSpec into python core and passes that to processSvcSpec. 
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "rinvoke" :parsMand "svcSpec resource opName" :parsOpt "perfSap headers" :argsMin "0" :argsMax "999" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || ICM-Cmnd       :: /rinvoke/ parsMand=svcSpec resource opName parsOpt=perfSap headers argsMin=0 argsMax=999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class rinvoke(icm.Cmnd):
    cmndParamsMandatory = [ 'svcSpec', 'resource', 'opName', ]
    cmndParamsOptional = [ 'perfSap', 'headers', ]
    cmndArgsLen = {'Min': 0, 'Max': 999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        svcSpec=None,         # or Cmnd-Input
        resource=None,         # or Cmnd-Input
        opName=None,         # or Cmnd-Input
        perfSap=None,         # or Cmnd-Input
        headers=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'svcSpec': svcSpec, 'resource': resource, 'opName': opName, 'perfSap': perfSap, 'headers': headers, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        svcSpec = callParamsDict['svcSpec']
        resource = callParamsDict['resource']
        opName = callParamsDict['opName']
        perfSap = callParamsDict['perfSap']
        headers = callParamsDict['headers']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        opParsList = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        icm.TM_here("svcSpec={svcSpec} -- perfSap={perfSap}".format(svcSpec=svcSpec, perfSap=perfSap))

        #generateSvcInfo("http://localhost:8080/swagger.json")
        loadedSvcSpec, origin_url = loadSvcSpec(svcSpec, perfSap)

        if perfSap:
            #origin_url = "http://localhost:8080"
            origin_url = perfSap

        pp = pprint.PrettyPrinter(indent=4)
        icm.TM_here("{}".format(pp.pformat(loadedSvcSpec)))

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
                icm.EH_problem_usageError("Expected 2: {parValLen}".format(parValLen=parValLen) )               
                continue
            
            opInvokeEvalStr = opInvokeEvalStr + """{parName}="{parValue}", """.format(
                parName=parName, parValue=parValue
                )
            
        opInvokeEvalStr = opInvokeEvalStr + ")"
        icm.TM_here("Invoking With Eval: str={opInvokeEvalStr}".format(opInvokeEvalStr=opInvokeEvalStr,))

        eval(opInvokeEvalStr)
        
        return

    
    def cmndDocStr(self): return """
** Creates the opInvoke string and evals opInvoke.  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "loggingSetup" :funcType "void" :retType "bool" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Func-void      :: /loggingSetup/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def loggingSetup():
####+END:
    # Debug logging
    logControler = icm.LOG_Control()
    icmLogger = logControler.loggerGet()
    
    icmLogLevel = logControler.level
    #icmLogLevel = logControler.loggerGetLevel()  # Use This After ICM has been updated

    def requestsDebugLog():
        httplib.HTTPConnection.debuglevel = 1
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

    
####+BEGIN: bx:icm:python:func :funcName "loadSvcSpec" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "spec perfSapUrl"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Func-anyOrNone :: /loadSvcSpec/ retType=bool argsList=(spec perfSapUrl) deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
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
            r = requests.get(spec)
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
        # icm.LOG_here("perfSap: host={host} port={port} path={path}".format(
        #     host = perfSapUrlObj.hostname,
        #     port = perfSapUrlObj.port,
        #     path = perfSapUrlObj.path,
        # ))
    
        spec['host'] = '{}:{}'.format(perfSapUrlObj.hostname, perfSapUrlObj.port)

        if perfSapUrlObj.path:
            spec['basePath'] = perfSapUrlObj.path

    spec = sanitize_spec(spec)
    return spec, origin_url


####+BEGIN: bx:icm:python:func :funcName "processSvcSpec" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "spec origin_url perfSap headers svcSpec"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Func-anyOrNone :: /processSvcSpec/ retType=bool argsList=(spec origin_url perfSap headers svcSpec) deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
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
    #icm.TM_here(pp.pformat(spec))

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
        
    for res_name, res in spec.resources.items():
        for op_name, op in res.operations.items():
            name = get_command_name(op)

            paramsListStr = ""
            optionalOrRequired = ""
            for param_name, param in op.params.items():
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
            print("{thisIcm} --svcSpec={svcSpec} {perfSapStr} {headersStr} --resource={res_name} --opName={op_name} -i rinvoke {paramsListStr}".format(            
                thisIcm=thisIcm,
                svcSpec=svcSpecStr,
                perfSapStr=perfSapStr,
                headersStr=headersStr,                                                                      
                res_name=res_name,
                op_name=op_name,
                paramsListStr=paramsListStr,
                )
            )
                
                
####+BEGIN: bx:icm:python:func :funcName "getOperationWithResourceAndOpName" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "spec origin_url resource opName"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Func-anyOrNone :: /getOperationWithResourceAndOpName/ retType=bool argsList=(spec origin_url resource opName) deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
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
    
    for res_name, res in spec.resources.items():
        if res_name != resource:
            continue

        for op_name, op in res.operations.items():
            if op_name != opName:
                continue
            
            name = get_command_name(op)

            icm.LOG_here("Invoking: resource={resource}  opName={opName}".format(
                resource=resource, opName=op_name))

            return op


####+BEGIN: bx:icm:python:func :funcName "get_command_name" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "op"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Func-anyOrNone :: /get_command_name/ retType=bool argsList=(op)  [[elisp:(org-cycle)][| ]]
"""
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


####+BEGINNOT: bx:icm:python:func :funcName "opInvoke" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "headers op *args **kwargs"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /opInvoke/ retType=bool argsList=(headers op *args **kwargs)  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)    
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
            icm.EH_problem_usageError("Expected 2: {}".format(headerLineAsListLen))
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
            icm.TM_here("bodyAny={}".format(pp.pformat(bodyAny)))
            
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
            icm.TM_here("bodyFile={}".format(pp.pformat(bodyFile)))
            
            if bodyFile == "":
                return ""
            
            if os.path.isfile(bodyAny):
                return bodyFileAsDict(bodyFile)
            else:
                return {}

        elif bodyFunc != None:
            icm.TM_here("bodyFunc={}".format(pp.pformat(bodyFunc)))
            
            if bodyFunc == "":
                return ""

            if bodyFunc == "NOTYET-valid func":
                return bodyFuncAsDict(bodyFunc)
            else:
                return {}
            

        elif bodyStr != None:
            icm.TM_here("bodyStr={}".format(pp.pformat(bodyStr)))
            
            if bodyStr == "":
                return ""
            
            bodyValue = bodyStrAsDict(bodyStr)
            return bodyValue

        else:
            # So they were all None, meaning that no form of "body" was specified.
            return None

    # icm.TM_here("Args: {}".format(args))
    # for key in kwargs:
    #      icm.TM_here("another keyword arg: %s: %s" % (key, kwargs[key]))
        

    bodyAny = kwargs.pop('body', None)
    bodyFile = kwargs.pop('bodyFile', None)
    bodyStr = kwargs.pop('bodyStr', None)
    bodyFunc = kwargs.pop('bodyFunc', None)

    bodyValue = bodyArgToDict(bodyAny, bodyFile, bodyStr, bodyFunc)

    icm.TM_here(pp.pformat(requestOptions))
    
    if bodyValue == None:
        request = construct_request(op, requestOptions, **kwargs)
    elif bodyValue == "":
        # Causes An Exception That Describes Expected Dictionary
        request = construct_request(op, requestOptions, body=None, **kwargs)
    else:
        request = construct_request(op, requestOptions, body=bodyValue, **kwargs)

        
    icm.LOG_here("request={request}".format(request=pp.pformat(request)))

    c = RequestsClient()

    future = c.request(request)
    
    result = future.result()

    icm.LOG_here("responseHeaders: {headers}".format(
        headers=pp.pformat(result._delegate.headers)))

    icm.ANN_write("Operation Status: {result}".format(result=result))

    icm.ANN_write("Operation Result: {result}".format(
        result=pp.pformat(result.json()))
    )
    


####+BEGIN: bx:icm:python:func :funcName "ro_opInvokeCapture" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "roOp"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Func-anyOrNone :: /ro_opInvokeCapture/ retType=bool argsList=(roOp) deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def ro_opInvokeCapture(
    roOp,
):
####+END:


    pp = pprint.PrettyPrinter(indent=4)    

    #icm.TM_here("svcSpec={svcSpec} -- perfSap={perfSap}".format(svcSpec=roOp.svcSpec, perfSap=roOp.perfSap))

    loadedSvcSpec, origin_url = loadSvcSpec(roOp.svcSpec, roOp.perfSap)

    if roOp.perfSap:
        #origin_url = "http://localhost:8080"
        origin_url = roOp.perfSap

    #
    # NOTYET LOG level changes here
    #
    #icm.TM_here("{}".format(pp.pformat(loadedSvcSpec)))

    opBravadoObj = getOperationWithResourceAndOpName(
        loadedSvcSpec,
        origin_url,
        roOp.resource,
        roOp.opName,
        )

    
    requestOptions = dict()

    params = roOp.roParams

    headerParams = params.headerParams
    if headerParams:
        requestOptions["headers"] = headerParams

    urlParams = params.urlParams
    if urlParams == None:
        urlParams = dict()

    bodyParams = params.bodyParams
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
        
    icm.LOG_here("request={request}".format(request=pp.pformat(request)))

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
        icm.EH_critical_exception(e)
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
                icm.EH_critical_exception(e)
                opResults=None

        roResults = ro.Ro_Results(
            httpResultCode=result._delegate.status_code,    # type=int
            httpResultText=result._delegate.reason,         # type=str
            opResults=opResults,
            opResultHeaders=result._delegate.headers,
            )

        icm.LOG_here("RESPONSE: status_code={status_code} -- reason={reason} -- text={text}".format(
            status_code=result._delegate.status_code,
            reason=result._delegate.reason,        
            text=result._delegate.text,
            ))

        icm.LOG_here("RESPONSE: responseHeaders: {headers}".format(
            headers=pp.pformat(result._delegate.headers)))

    roOp.roResults = roResults
    
    return roOp


####+BEGIN: bx:icm:python:func :funcName "invokeCapture" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "op"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Func-anyOrNone :: /invokeCapture/ retType=bool argsList=(op) deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def invokeCapture(
    op,
):
####+END:
    print(op)
    
    print(op.svcSpec)

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
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))
    
    
    
####+BEGIN: bx:icm:python:func :funcName "sanitize_spec" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "spec"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]] || Func-anyOrNone :: /sanitize_spec/ retType=bool argsList=(spec)  [[elisp:(org-cycle)][| ]]
"""
def sanitize_spec(
    spec,
):
####+END:
    for path, path_obj in list(spec['paths'].items()):
        # remove root paths as no resource name can be found for it
        if path == '/':
            del spec['paths'][path]
    return spec

    

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
