#!/bin/bash

# Launch programs and get their wmctrl window title
# kill the programs

# TODO: Learn how subshells and background process works
# TODO: Kill by PID for all types, this workaround works for now

# cmd to launch program
CMD2LAUNCH=${1}
# time to sleep
WAITTIME=${2}

# check if flatpak package
if [[ ${CMD2LAUNCH} == *"flatpak"* ]]
then
  FLATPAKPKG=True
else
  FLATPAKPKG=False
fi

# lauch as background process ignore all output
${CMD2LAUNCH} &> /dev/null &
# TODO: check to make sure the command ran successfully

# give the app time to load gui
sleep $WAITTIME

# get the window header info
WINHEADER=$(wmctrl -l -p | tail -n 1 | awk '{$1=$2=$3=$4=""; print $0}')
# stdout the info so the pyInput script can handle it
echo "${WINHEADER}"

# kill the app we launched
if [[ ${FLATPAKPKG} == "True" ]]
then
  # get INSTANCEID
  INSTANCEID=$(flatpak ps | head -n1 | awk '{print $1}')
#  echo "${INSTANCEID}"
  # kill instance
  flatpak kill ${INSTANCEID}
else
  # get the pid of the window that was just opened
  CMDPID=$(wmctrl -l -p | tail -n 1 | awk '{print $3}')
#  echo "CMDPID: ${CMDPID}"
  # kill the new window
  kill ${CMDPID}
fi
exit 0
