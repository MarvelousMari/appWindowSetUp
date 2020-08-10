#!/bin/bash
usage() {
  echo "-d for desktop connnected"
}

DESKTOPCONNECTED=false

while getopts vl:s OPTION
do
  case ${OPTION} in
    d)
      DESKTOPCONNECTED=true
      ;;
    ?)
      usage
      ;;
  esac
done
# this is a script generated to launch apps in diffrent desktops on start up

if DESKTOPCONNECTED
then
  flatpak run com.github.debauchee.barrier &> /dev/null &
  flatpak run com.google.AndroidStudio &> /dev/null &
  firefox github.com/login mariellapage.com/wp-admin &> /dev/null &
else
  firefox udemy.com github.com/login mariellapage.com/wp-admin &> /dev/null & sleep 2
  wmctrl -r firefox -t 0

  flatpak run com.google.AndroidStudio &> /dev/null & sleep 10
  wmctrl -r android -t 1

  github &> /dev/null & sleep 3
  wmctrl -r github -t 2

  flatpak run com.spotify.Client &> /dev/null & sleep 2
  wmctrl -r spotify -t 3

  exit 0
fi
