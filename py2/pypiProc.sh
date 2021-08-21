#!/bin/bash

####+BEGIN: bx:dblock:bash:top-of-file :vc "cvs" partof: "bystar" :copyleft "halaal+minimal"

####+END:

####+BEGIN: bx:bsip:bash:seed-spec :types "seedPypiProc.sh"
SEED="
*  /[dblock]/ /Seed/ :: [[file:/bisos/core/bsip/bin/seedPypiProc.sh]] | 
"
FILE="
*  /This File/ :: /bisos/git/bxRepos/bisos-pip/mmwsIcm/dev/pypiProc.sh 
"
if [ "${loadFiles}" == "" ] ; then
    /bisos/core/bsip/bin/seedPypiProc.sh -l $0 "$@" 
    exit $?
fi
####+END:


_CommentBegin_
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  examplesHookPost    [[elisp:(org-cycle)][| ]]
_CommentEnd_

function examplesHookPost {

    #local startTemplate="/bisos/git/bxRepos/bisos/defaults/software/starts/pypiProc.sh"
    local startTemplate="/bisos/apps/defaults/software/starts/pypiProc.sh"
    
cat  << _EOF_
--- EXTRAs ---
$( examplesSeperatorChapter "pypiProc.sh Maintenance" )
FN_fileSafeCopy ./pypiProc.sh ./pypiProc.sh.$(DATE_getTag)
diff ./pypiProc.sh ${startTemplate} 
cp ./pypiProc.sh ${startTemplate}
cp ${startTemplate} ./pypiProc.sh 
_EOF_
 return
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
