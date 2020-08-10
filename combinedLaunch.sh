#!/bin/bash

usage() {
  echo "-d for desktop connnected"
  echo "-c what config either BASH or ANDROID"
}

top_connected_android(){

  barrierc --enable-crypto 192.168.1.15

  # launch desktop 2 applications
  flatpak run com.spotify.Client &> /dev/null & sleep 2
  if [[ "${?}" == 1 ]]
  then
    echo "couldn't open spotify"
    exit 1
  fi

  # move applications to desktop 2
  wmctrl -r spotify -t 1
  if [[ "${?}" == 1 ]]
  then
    echo "couldn't move spotify"
    exit 1
  fi

  # open the application for desktop 0
  firefox udemy.com mariellapage.com/wp-admin & sleep 2
  if [[ "${?}" == 1 ]]
  then
    echo "couldn't open firefox"
    exit 1
  fi

  exit 0
}

top_connected_bash(){

  barrierc --enable-crypto 192.168.1.15

  # launch desktop 2 applications
  flatpak run com.spotify.Client &> /dev/null & sleep 2
  if [[ "${?}" == 1 ]]
  then
    echo "couldn't open spotify"
    exit 1
  fi

  # move applications to desktop 2
  wmctrl -r spotify -t 1
  if [[ "${?}" == 1 ]]
  then
    echo "couldn't move spotify"
    exit 1
  fi

  # open the application for desktop 0
  firefox udemy.com mariellapage.com/wp-admin & sleep 2
  if [[ "${?}" == 1 ]]
  then
    echo "couldn't open firefox"
    exit 1
  fi

  exit 0
}

top_android(){
  firefox udemy.com github.com/login mariellapage.com/wp-admin &> /dev/null & sleep 2
  wmctrl -r firefox -t 0

  flatpak run com.google.AndroidStudio &> /dev/null & sleep 10
  wmctrl -r android -t 1

  github &> /dev/null & sleep 3
  wmctrl -r github -t 2

  flatpak run com.spotify.Client &> /dev/null & sleep 2
  wmctrl -r spotify -t 3

  exit 0
}

top_bash(){
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
}

tower_connected_android(){
  flatpak run com.github.debauchee.barrier &
  flatpak run com.google.AndroidStudio &> /dev/null &
  exit 0
}

tower_connected_bash(){
  flatpak run com.github.debauchee.barrier &
  gnome-terminal &
  flatpak run io.atom.Atom &> /dev/null &
  exit 0
}

tower_android(){
  firefox udemy.com github.com/login mariellapage.com/wp-admin &> /dev/null &
  flatpak run com.google.AndroidStudio &> /dev/null &
  flatpak run com.spotify.Client &> /dev/null & sleep 2
  wmctrl -r spotify -t 1
  exit 0
}

tower_bash(){
  flatpak run io.atom.Atom &> /dev/null &
  firefox udemy.com github.com/login mariellapage.com/wp-admin &> /dev/null &
  gnome-terminal & sleep 2
  wmctrl -r "@MTower" -t 1
  flatpak run com.spotify.Client &> /dev/null & sleep 2
  wmctrl -r spotify -t 1
  exit 0
}

$DESKTOP_CONNECTED=false
$CONFIG_TO_LAUNCH=""

while getopts dc: OPTION
do
  case ${OPTION} in
    d)
      $DESKTOP_CONNECTED=true
      ;;
    c)
      CONFIG_TO_LAUNCH="${OPTARG}"
      if [[ $CONFIG_TO_LAUNCH = "ANDROID" ]] || [[ $CONFIG_TO_LAUNCH = "BASH" ]]
      then
        echo "valid input"
      else
        echo "INVALID CONFIG_TO_LAUNCH:${CONFIG_TO_LAUNCH}"
        echo "OPTARG:${OPTARG}"
        echo "OPTION:${OPTION}"
        exit 1
      fi
      ;;
    ?)
      usage
      ;;
  esac
done

if [[ $HOSTNAME == "MTower" ]]
then
  if [[ $CONFIG_TO_LAUNCH == "BASH" ]]
  then
    if $DESKTOP_CONNECTED
    then
      tower_connected_bash
    else
      tower_bash
    fi
  elif [[ $CONFIG_TO_LAUNCH == "ANDROID" ]]
  then
    if $DESKTOP_CONNECTED
    then
      tower_connected_android
    else
      tower_android
    fi
  else
    echo "INVALID CONFIG"
    exit 1
  fi
elif [[ $HOSTNAME == "Mtop" ]]
then
  if [[ $CONFIG_TO_LAUNCH == "BASH" ]]
  then
    if $DESKTOP_CONNECTED
    then
      top_connected_bash
    else
      top_bash
    fi
  elif [[ $CONFIG_TO_LAUNCH == "ANDROID" ]]
  then
    if $DESKTOP_CONNECTED
    then
      top_connected_android
    else
      top_android
    fi
  else
    echo "invalid CONFIG_TO_LAUNCH"
  fi
else
  echo "INVALID HOSTNAME"
  exit 1
fi
