#!/bin/bash

####+BEGIN: bx:dblock:bash:top-of-file :vc "cvs" partof: "bystar" :copyleft "halaal+minimal"
typeset RcsId="$Id: ftoProc.sh,v 1.1 2018-09-08 00:13:09 lsipusr Exp $"
# *CopyLeft*
#  This is a Halaal Poly-Existential. See http://www.freeprotocols.org

####+END:

####+BEGIN: bx:dblock:lsip:bash:seed-spec :types "seedFtoCommon.sh"
SEED="
*  /[dblock]/ /Seed/ :: [[file:/opt/public/osmt/bin/seedFtoCommon.sh]] | 
"
FILE="
*  /This File/ :: /de/bx/nne/dev-py/pypi/pkgs/unisos/icm/ftoProc.sh 
"
if [ "${loadFiles}" == "" ] ; then
    /opt/public/osmt/bin/seedFtoCommon.sh -l $0 "$@" 
    exit $?
fi
####+END:


leavesExcludes=""

leavesOrdered=""

nodesExcludes=""

nodesOrdered=""


_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || List       ::  Leaves List    [[elisp:(org-cycle)][| ]]
_CommentEnd_

####+BEGIN: bx:dblock:ploneProc:bash:leavesList :types ""
# {{{ DBLOCK-leavesList
leavesList="
dev
"
# }}} DBLOCK-leavesList
####+END:


_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || List       ::  Nodes List    [[elisp:(org-cycle)][| ]]
_CommentEnd_

####+BEGIN: bx:dblock:ploneProc:bash:nodesList :types ""
# {{{ DBLOCK-nodesList
nodesList="
fptb
rel
"
# }}} DBLOCK-nodesList
####+END:


_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Cmnd       ::  examplesHookPostExample    [[elisp:(org-cycle)][| ]]
_CommentEnd_

function examplesHookPost {
    cat  << _EOF_
$( examplesSeperatorTopLabel "EXTENSION EXAMPLES" )
_EOF_

    pypiFtpWalks

    templatesEvolution
    
    return
}


function pypiFtpWalks {
    cat  << _EOF_
$( examplesSeperatorChapter "ftpWalks: Uninstall" )
ftoProc.sh -v -n showRun -i ftoWalkRunCmnd pypiProc.sh -i pkgUnInstall sys
$( examplesSeperatorChapter "PyPi AuxNode ftpWalks" )
ftoProc.sh -v -n showRun -i treeRecurse runFunc pypiProc.sh -i distClean
ftoProc.sh -v -n showRun -i ftoWalkRunCmnd pypiProc.sh -i distClean
ftoProc.sh -v -n showRun -i ftoWalkRunCmnd pypiProc.sh -i pkgInstall edit /bystar/dist/venv/dev-py2-bisos-3
ftoProc.sh -v -n showRun -i ftoWalkRunCmnd pypiProc.sh -i pkgInstall edit sys
ftoProc.sh -v -n showRun -i ftoWalkRunCmnd icmPlayer.sh -i clean ftoProc.sh pypiProc.sh
ftoProc.sh -v -n showRun -i ftoWalkRunCmnd icmPlayer.sh -i pkgedPrep ftoProc.sh pypiProc.sh
$( examplesSeperatorChapter "Under Files Update" )
ftoProc.sh -v -n showRun -i updateUnderFilesTo  /libre/ByStar/InitialTemplates/update/fto/start/commonProc/anyFtoItem/ftoProcNode.sh ftoProc.sh
ftoProc.sh -v -n showRun -i updateUnderFilesTo /libre/ByStar/InitialTemplates/software/starts/pypiProc.sh pypiProc.sh 
_EOF_
 return
}


function templatesEvolution {
    cat  << _EOF_
$( examplesSeperatorSection "ftoProc.sh -- Templates Evolution" )
diff ./ftoProc.sh  /libre/ByStar/InitialTemplates/update/fto/start/commonProc/anyFtoItem/ftoProcNode.sh
cp ./ftoProc.sh  /libre/ByStar/InitialTemplates/update/fto/start/commonProc/anyFtoItem/ftoProcNode.sh
cp /libre/ByStar/InitialTemplates/update/fto/start/commonProc/anyFtoItem/ftoProcNode.sh ./ftoProc.sh  
$( examplesSeperatorSection "commonPanel.org -- Templates Evolution" )
diff ./Panel.org  /libre/ByStar/InitialTemplates/start/fto/commonProc/anyFtoItem/mainPanel.org
cp ./Panel.org /libre/ByStar/InitialTemplates/start/fto/commonProc/anyFtoItem/mainPanel.org
cp /libre/ByStar/InitialTemplates/start/fto/commonProc/anyFtoItem/mainPanel.org ./Panel.org
_EOF_
 return
}


function vis_updateUnderFilesTo {
    G_funcEntry
    function describeF {  cat  << _EOF_
_EOF_
    }
    EH_assert [[ $# -eq 2 ]]

    local updateToFile="$1"        
    local underFilesName="$2"

    if [ ! -f "${updateToFile}" ] ; then
	EH_problem "Bad Usage Missing ${updateToFile}"
	lpReturn
    fi

    local underFilesList=$(find . -type f -print | egrep "/${underFilesName}"'$')

    for each in ${underFilesList} ; do
	opDo cp ${updateToFile} ${each} 
	opDo bx-dblock -i dblockUpdateFile ${each}
    done

    lpReturn
}



####+BEGIN: bx:dblock:bash:end-of-file :types ""
_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  Common        ::  /[dblock] -- End-Of-File Controls/ [[elisp:(org-cycle)][| ]]
_CommentEnd_
#+STARTUP: showall
#local variables:
#major-mode: sh-mode
#fill-column: 90
# end:
####+END:
