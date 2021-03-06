#!/bin/bash
 
# this is a script generated to launch apps in diffrent desktops on start up

firefox &> /dev/null & sleep 5
wmctrl -r firefox -t 0

flatpak run com.google.AndroidStudio &> /dev/null & sleep 5
wmctrl -r android -t 1

flatpak run com.google.AndroidStudio &> /dev/null & sleep 5
wmctrl -r android -t 1

flatpak run com.spotify.Client &> /dev/null & sleep 5
wmctrl -r spotify -t 2

exit 0