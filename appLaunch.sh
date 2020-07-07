#!/bin/bash

# Launch programs and get their wmctrl window title
# kill the programs


# cmd to launch program
CMD2LAUNCH=${1}
# time to sleep
WAITTIME=${2}

# lauch as background process
# need to learn about subshells in order to make this properly work using ${!}
# doesn't work right
${CMD2LAUNCH} & PID2KILL=$$
# get the PID to kill later
echo "PID2KILL: ${PID2KILL}"

wait $WAITTIME

# get the window header info
WINHEADER=$(wmctrl -l | tail -n 1 )
echo "${WINHEADER}"

# kill the program
pkill -9 -P ${PID2KILL}

exit 0
