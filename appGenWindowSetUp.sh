#!/bin/bash
 
# this is a script generated to launch apps in diffrent desktops on start up
firefox &> /dev/null & sleep 3
wmctrl -r firefox -t 0
flatpak run io.atom.Atom &> /dev/null & sleep 3
wmctrl -r atom -t 0
gedit &> /dev/null & sleep 3
wmctrl -r gedit -t 1
flatpak run com.spotify.Client &> /dev/null & sleep 3
wmctrl -r spotify -t 2
exit 0