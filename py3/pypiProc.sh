#!/bin/bash

####+BEGIN: bx:bsip:bash:seed-spec :types "seedPypiProc.sh"
SEED="
*  /[dblock]/ /Seed/ :: [[file:/bisos/core/bsip/bin/seedPypiProc.sh]] |
"
FILE="
*  /This File/ :: /bisos/git/bxRepos/bisos-pip/capability/py3/pypiProc.sh
"
if [ "${loadFiles}" == "" ] ; then
    /bisos/core/bsip/bin/seedPypiProc.sh -l $0 "$@"
    exit $?
fi
####+END:

function examplesHookPost {
    cat  << _EOF_
--- EXTRAs ---
$( examplesSeperatorChapter "pypiProc.sh Maintenance" )
${G_myName} -i artifactsList   # Copy better artifacts when available
_EOF_
    return
}
