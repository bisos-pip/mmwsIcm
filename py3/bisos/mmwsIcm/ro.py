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
__version__ = "202502125033"
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

#import os
import collections
#import enum


import pprint

from . import wsInvokerIcm

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
        parName='placeHolder',
        parDescription="Name Of The User",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--userName',
    )
    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################## [[elisp:(delete-other-windows)][(1)]]        *Common Examples Sections*
"""

####+BEGIN: bx:cs:python:func :funcName "examples_remoteOperations" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "roListLoadFile roExpectListLoadFile"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_remoteOperations/ retType=bool argsList=(roListLoadFile roExpectListLoadFile)  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_remoteOperations(
    roListLoadFile,
    roExpectListLoadFile,
):
####+END:
    """."""
    
    def cpsInit(): return collections.OrderedDict()
    #def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    cs.examples.menuChapter('/Remote Operation Scenario Files/ *roListInv*')
        
    if roListLoadFiles:
        loadOpScenariosArgs=""
        for each in roListLoadFiles: 
            loadOpScenariosArgs="""{loadOpScenariosArgs} --load {each}""".format(
                loadOpScenariosArgs=loadOpScenariosArgs,
                each=each,)
        thisCmndAction= " -i roListInv"
        icm.cmndExampleMenuItem(format(loadOpScenariosArgs + thisCmndAction),
                                verbosity='none')                            

    if roExpectListLoadFiles:
        loadOpScenariosArgs=""
        for each in roExpectListLoadFiles: 
            loadOpScenariosArgs="""{loadOpScenariosArgs} --load {each}""".format(
                loadOpScenariosArgs=loadOpScenariosArgs,
                each=each,)
        thisCmndAction= " -i roListExpectations"
        icm.cmndExampleMenuItem(format(loadOpScenariosArgs + thisCmndAction),
                                verbosity='none')                            


####+BEGIN: bx:cs:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "roListInv" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<roListInv>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class roListInv(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:

        rosList = Ro_OpsList().opsListGet()

        @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
        def rosListProc(rosList):
            """Process List of Remote Operations"""
            @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
            def roProc(thisRo):
                """Process One Remote Operation"""

                return ( wsInvokerIcm.ro_opInvokeCapture(thisRo) )

            for thisRo in rosList:
                invokedOp = roProc(thisRo)
                if invokedOp:
                    opReport(invokedOp)
                else:
                    b_io.eh.problem_usageError("ro_opInvokeCapture Failed")

            return

        rosListProc(rosList)

        return( cmndOutcome )

    
    def cmndDocStr(self): return """
** Place holder for ICM's experimental or test code.  [[elisp:(org-cycle)][| ]]
 You can use this Cmnd for rapid prototyping and testing of newly developed functions.
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
        


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "roListExpectations" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<roListExpectations>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class roListExpectations(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:

        roExpectationsList = Ro_OpExpectationsList().opExpectationsListGet()


        @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
        def roExpectationsListProc(roExpectationsList):
            """Process List of Remote Operations Expectations"""
            @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
            def roExpectationProc(thisRoExpecation):
                """Process One Remote Operation"""

                thisRo = thisRoExpecation.roOp

                for thisPreInvokeCallable in thisRoExpecation.preInvokeCallables:
                    thisPreInvokeCallable(thisRoExpecation)

                invokedOp = wsInvokerIcm.ro_opInvokeCapture(thisRo)
                opReport(invokedOp)                

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


####+BEGIN: b:py3:class/decl :className "Ro_Params" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /Ro_Params/  superClass=object  [[elisp:(org-cycle)][| ]]
#+end_org """
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


####+BEGIN: b:py3:class/decl :className "Ro_Results" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /Ro_Results/  superClass=object  [[elisp:(org-cycle)][| ]]
#+end_org """
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
         

####+BEGIN: b:py3:class/decl :className "Ro_Op" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /Ro_Op/  superClass=object  [[elisp:(org-cycle)][| ]]
#+end_org """
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


         
####+BEGIN: b:py3:class/decl :className "Ro_OpsList" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /Ro_OpsList/  superClass=object  [[elisp:(org-cycle)][| ]]
#+end_org """
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



####+BEGIN: b:py3:class/decl :className "Ro_OpExpectation" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /Ro_OpExpectation/  superClass=object  [[elisp:(org-cycle)][| ]]
#+end_org """
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

####+BEGIN: b:py3:class/decl :className "Ro_OpExpectationsList" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /Ro_OpExpectationsList/  superClass=object  [[elisp:(org-cycle)][| ]]
#+end_org """
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

    
             
        
####+BEGIN: bx:cs:python:section :title "Supporting Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:cs:python:func :funcName "opReport" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "op"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /opReport/ retType=bool argsList=(op)  [[elisp:(org-cycle)][| ]]
#+end_org """
def opReport(
    op,
):
####+END:
    pp = pprint.PrettyPrinter(indent=4)

    b_io.ann.write("""* ->:: @{perfSap}@{resource}@{opName}""".format(
        perfSap=op.perfSap,
        resource=op.resource,
        opName=op.opName,
    ))

    params = op.roParams    

    b_io.ann.write("""** ->:: svcSpec={svcSpec}""".format(
        svcSpec=op.svcSpec,
    ))

    newLine = "\n";
    if params.headerParams == None: newLine = "";
        
    b_io.ann.write("** ->:: Header Params: {newLine}{headerParams}".format(
        newLine=newLine, headerParams=pp.pformat(params.headerParams)))

    newLine = "\n";
    if params.urlParams == None: newLine = "";
        
    b_io.ann.write("** ->:: Url Params: {newLine}{urlParams}".format(
        newLine=newLine, urlParams=pp.pformat(params.urlParams)))

    newLine = "\n";
    if params.bodyParams == None: newLine = "";
        
    b_io.ann.write("** ->:: Body Params: {newLine}{bodyParams}".format(
        newLine=newLine, bodyParams=pp.pformat(params.bodyParams)))

    
    results = op.roResults

    if results.opResults:
        resultsFormat="json"
    else:
        resultsFormat="empty"
        
    b_io.ann.write("""* <-:: httpStatus={httpResultCode} -- httpText={httpResultText} -- resultsFormat={resultsFormat}""".format(
        httpResultCode=results.httpResultCode,
        httpResultText=results.httpResultText,
        resultsFormat=resultsFormat,
    ))

    newLine = "\n";
    if results.opResults == None: newLine = "";
        
    b_io.ann.write("** <-:: Operation Result: {newLine}{result}".format(
        newLine=newLine, result=pp.pformat(results.opResults)))
    
    #b_io.ann.write("""* ==:: basicPass or failed or Verified""")
        
        
             
    
####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _ ~End Of Editable Text~ _: |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:
