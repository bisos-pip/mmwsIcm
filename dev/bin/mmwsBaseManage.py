#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""\
*    *[Summary]* :: A =mmwsBaseManage=: Based on specified parameters manage a WebService Base.
"""

####+BEGIN: bx:icm:python:top-of-file :partof "cible" :copyleft "none"
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/unisos/mmwsIcm/dev/bin/mmwsBaseManage.py :: [[elisp:(org-cycle)][| ]]

 A Python Interactively Command Module (PyICM). Part Of ByStar.
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 Warning: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:python:name :style "fileName"
__icmName__ = "mmwsBaseManage"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201809102516"
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

####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

####+BEGIN: bx:icm:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import sys
import os

import collections

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__

####+END:

from blee.icmPlayer import bleep

#import bearerToken

g_importedCmnds = {        # Enumerate modules from which CMNDs become invokable
    'bleep': bleep.__file__,
    #'bearerToken': bearerToken.__file__,
}

#import pprint    

####+BEGIN: bx:icm:python:section :title "= =Framework::= ICM  Description (Overview) ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM  Description (Overview) =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "icmOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /icmOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class icmOverview(icm.Cmnd):
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


####+BEGIN: bx:icm:python:section :title "= =Framework::= ICM Hooks ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM Hooks =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "g_icmChars" :comment "ICM Characteristics Spec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmChars/ =ICM Characteristics Spec= retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def g_icmChars():
####+END:
    icmInfo['panel'] = "{}-Panel.org".format(__icmName__)
    icmInfo['groupingType'] = "IcmGroupingType-pkged"
    icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"
    
g_icmChars()


####+BEGIN: bx:icm:python:func :funcName "g_icmPreCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmPreCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPreCmnds():
####+END:
    """ PreHook """
    pass


####+BEGIN: bx:icm:python:func :funcName "g_icmPostCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmPostCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPostCmnds():
####+END:
    """ PostHook """
    pass


####+BEGIN: bx:icm:python:section :title "= =Framework::= Options, Arguments and Examples Specifications ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= Options, Arguments and Examples Specifications =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "g_argsExtraSpecify" :comment "FrameWrk: ArgsSpec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_argsExtraSpecify/ =FrameWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
"""
def g_argsExtraSpecify(
    parser,
):
####+END:
    """Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = icm.IcmGlobalContext()
    icmParams = icm.ICM_ParamDict()

    icmParams.parDictAdd(
        parName='moduleVersion',
        parDescription="Module Version",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--version',
    )

    
    bleep.commonParamsSpecify(icmParams)

    #bearerToken.commonParamsSpecify(icmParams)
       
    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)
    
    return


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "examples" :cmndType "ICM-Cmnd-FWrk" :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd-FWrk  :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(icm.Cmnd):
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
        def cpsInit(): return collections.OrderedDict()
        def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        ##### IMPORTANT PARAMS SPECIFICATIONS BEGIN

        svcSpecUrl="http://localhost:8080/swagger.json"
        svcSpecFile="./swagger.json"        
        perfSap="http://localhost:8080"
        headersFileName = "./bearerToken.headers"
        includeOpsListInExamples = False
        
        ##### IMPORTANT PARAMS SPECIFICATIONS END        
        

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)
        
        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())
        
        icm.G_commonBriefExamples()

        bleep.examples_icmBasic()

        #bearerToken.examples_tokenGenerator("NAME", "ROLES", "GROUPS")

            
        return(cmndOutcome)

    def cmndDocStr(self): return """
** ICM Examples -- List of commonly used lines for this ICM [[elisp:(org-cycle)][| ]]
"""
    
   
    
####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/G_examples.bottom.py"
    # Intentionally Left Blank -- previously: lhip.G_devExamples(G_myName)

####+END:


####+BEGIN: bx:icm:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

    
####+BEGIN: bx:icm:python:section :title "Common/Generic Facilities -- Library Candidates"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common/Generic Facilities -- Library Candidates*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

    
####+BEGIN: bx:icm:python:section :title "= =Framework::=   G_main -- Instead Of ICM Dispatcher ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::=   G_main -- Instead Of ICM Dispatcher =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "G_main" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /G_main/ retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def G_main():
####+END:
    """ 
** Replaces ICM dispatcher for other command line args parsings.
"""
    pass

####+BEGIN: bx:icm:python:icmItem :itemType "Configuration" :itemTitle "= =Framework::= g_ Settings -- ICMs Imports ="
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Configuration  :: = =Framework::= g_ Settings -- ICMs Imports =  [[elisp:(org-cycle)][| ]]
"""
####+END:

g_examples = examples  # or None
g_mainEntry = None  # or G_main

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icm2.G_main.py"
"""
*  [[elisp:(beginning-of-buffer)][Top]] # /Dblk-Begin/ # [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

def classedCmndsDict():
    """
** Should be done here, can not be done in icm library because of the evals.
"""
    callDict = dict()
    for eachCmnd in icm.cmndList_mainsMethods().cmnd(
            interactive=False,
            importedCmnds=g_importedCmnds,
            mainFileName=__file__,
    ):
        try:
            callDict[eachCmnd] = eval("{}".format(eachCmnd))
            continue
        except NameError:
            pass

        for mod in g_importedCmnds:
            try:
                eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
            except AttributeError:
                continue
            try:                
                callDict[eachCmnd] = eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
                break
            except NameError:
                pass
    return callDict

icmInfo['icmName'] = __icmName__
icmInfo['version'] = __version__
icmInfo['status'] = __status__
icmInfo['credits'] = __credits__

G = icm.IcmGlobalContext()
G.icmInfo = icmInfo

def g_icmMain():
    """This ICM's specific information is passed to G_mainWithClass"""
    sys.exit(
        icm.G_mainWithClass(
            inArgv=sys.argv[1:],                 # Mandatory
            extraArgs=g_argsExtraSpecify,        # Mandatory
            G_examples=g_examples,               # Mandatory            
            classedCmndsDict=classedCmndsDict(),   # Mandatory
            mainEntry=g_mainEntry,
            g_icmPreCmnds=g_icmPreCmnds,
            g_icmPostCmnds=g_icmPostCmnds,
        )
    )

g_icmMain()

"""
*  [[elisp:(beginning-of-buffer)][Top]] ## /Dblk-End/ ## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

####+END:

####+BEGIN: bx:icm:python:section :title "Unused Facilities -- Temporary Junk Yard"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Unused Facilities -- Temporary Junk Yard*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
