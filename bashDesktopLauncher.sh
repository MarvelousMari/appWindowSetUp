#!/bin/bash

# open firefox and atom on desktop 0
# open terminal on desktop 1
# open spotify on desktop 2
# using wmctrl
# can't use wmctrl -n to generate desktops, must fill a desktop to create
# an additional desktops
# use the below to figure out errors with odd named windows
# :ACTIVE:
# :SELECT:
# -m manager
# -d desktops
# -l list windows

# applications for dekstop 0 are handled at the end
# this is to allow for tile windows to be on and not mess up
# from too fast window and desktop movement
# also allows for shorter sleep times

# open the applications for desktop 1
gnome-terminal & sleep 2
if [[ "${?}" == 1 ]]
then
  echo "couldn't open gnome-terminal"
  exit 1
fi

# move applications to desktop 1
# wmctrl window argument is usually a string
# and the first window containing that string is acted on
# gnome-terminal windows all contain @pop-os
wmctrl -r @Mtop -t 1
if [[ "${?}" == 1 ]]
then
  echo "couldn't move window named '@Mtop'"
  exit 1
fi

# launch desktop 2 applications
flatpak run com.spotify.Client &> /dev/null & sleep 2
if [[ "${?}" == 1 ]]
then
  echo "couldn't open spotify"
  exit 1
fi

# move applications to desktop 2
wmctrl -r spotify -t 2
if [[ "${?}" == 1 ]]
then
  echo "couldn't move spotify"
  exit 1
fi

# open the application for desktop 0
firefox udemy.com github.com/login mariellapage.com/wp-admin & sleep 2
if [[ "${?}" == 1 ]]
then
  echo "couldn't open firefox"
  exit 1
fi

# split so atom opens on the right with tile windows on
flatpak run io.atom.Atom & sleep 2
if [[ "${?}" == 1 ]]
then
  echo "couldn't open atom"
  exit 1
fi

exit 0
