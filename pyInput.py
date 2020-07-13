# get the appplications to launch
# get the desired desktop config
# create script to have launch on start

import subprocess
import time
import os

# wait time that can be set if needed cause of programs launching to slowly
waitTime = 3

# get applications to launch
print("please enter the applications you would like to launch one at a time")
print("when you're done entering applications input 'DONE'")
print("use the format for launching the application in terminal including any arguments you use:")
print("")

# list of launch cmds
appList = []
while True:
    # make sure it's in proper terminal format
    app = input("cmd:  ")
    print("")
    # TODO: add while catch correct input to prevent mistakes
    # moving this # TODO: to appLaunch.sh
    if app == 'DONE':
        break
    else:
        appList.append(app)

print("applist: %s" % (appList))

# dict for {window name : app launch cmd}
windowNames = {}

# get the window names of all of the apps
for app in appList:
    # launch the apps
    appSubProc = subprocess.run(['./appLaunch.sh', app , str(waitTime)], capture_output=True, text=True)
    # check to see if the terminal launch command(app) is already a part of the window descriptor
    # firefox is the command and the name of the window
    # if it is add it to the dictionary
    if app.lower() in appSubProc.stdout.lower():
        windowNames[app] = app
    # else ask for what part of the app window header is always there
    else:
        print("what part of this line: ")
        # stdout of ./appLaunch
        print(appSubProc.stdout.lower())
        print("is always in the header of the %s window: " % (app))
        windowNames[input().lower()] = app

print("")

print("windowNames: %s" % (windowNames))

print("")

# {desktopNum : [(windowName, launch cmd)]}
# {0: [(firefox, firefox),(atom, flatpak run io.atom.Atom)]}
windowLocations = {}
print("desktops start at 0, you can not create an empty desktop inbetween")
# desktop apps are being added to
currentDesktop = 0
# how many desktops are available
desktopsAvailable = 0
print("add an application to desktop OR input NEXT to move to the next desktop")
# windowNames.keys() is the name of the windows that the user provided
print("application to choose from:", (windowNames.keys()))
# while there are still launch cmds that havent't been added
# in the format of the window name desktop num
while len(appList) > 0 :
    # get the name of the window that belongs on that desktop
    InputedWindowName = input("desktop %s:   " % (currentDesktop))
    # if the input is a valid windowName
    if InputedWindowName in windowNames:
        # prevents issues with dictionary not having an array value and trying to use append
        windowLocations[currentDesktop] = windowLocations[currentDesktop] if currentDesktop in windowLocations else []
        # append to the value
        windowLocations[currentDesktop].append( (InputedWindowName, windowNames[InputedWindowName]) )
        # remove from appList so that when there are none left the while loop ends
        appList.remove(windowNames[InputedWindowName])
        # if currentDesktop is the highest available
        if currentDesktop == desktopsAvailable:
            # make another desktop available
            desktopsAvailable = desktopsAvailable + 1
    # move to next desktop if available
    elif InputedWindowName == "NEXT":
        # if desktopsAvailable is only 1 higher than the current desktop
        if desktopsAvailable == (currentDesktop + 1):
            # move to the next desktop
            currentDesktop = currentDesktop + 1
        # so if the desktop can't be empty or skip a number
        else:
            print("can't have an empty desktop")
    # if not valid input
    else:
        print("'%s' is not a valid input" % (InputedWindowName))
    print("")

print("")

# {0: [(firefox, firefox),(atom, flatpak run io.atom.Atom)]}
print("windowLocations: %s" % (windowLocations))
# dict for {window name : app launch cmd}
print("windowNames: %s" % (windowNames))
# list of launch cmds SHOULD BE EMPTY AT THIS POINT
print("appList: %s" % (appList))

# EX. of possible info at this point
# windowLocations: {0: [('firefox', 'firefox'), ('atom', 'flatpak run io.atom.Atom')], 1: [('gedit', 'gedit')], 2: [('spotify', 'flatpak run com.spotify.Client')]}
# windowNames: {'firefox': 'firefox', 'atom': 'flatpak run io.atom.Atom', 'gedit': 'gedit', 'spotify': 'flatpak run com.spotify.Client'}
# appList: []


# generate code

# get current directory then add the file to generate
# appGenWindowSetUp.sh
gen_path = os.path.dirname(os.path.realpath(__file__)) + "/appGenWindowSetUp.sh"

gen_file = open(gen_path, 'w')

# add shabang
gen_file.write("#!/bin/bash")
gen_file.write("\n \n")
gen_file.write("# this is a script generated to launch apps in diffrent desktops on start up")
gen_file.write("\n")
gen_file.write("\n")

# desktop num in window windowLocations
for desktop in windowLocations:
    # for each tuple in the array that is the value of the windowLocations current desktop from loop above
    # {0: [(windowName, launchCmd),(windowName, launchCmd)}
    for winTupleToPlace in windowLocations[desktop]:
        # /dev/null/ the output to keep things clean # launch cmd # sleep time
        gen_file.write("%s &> /dev/null & sleep %s" % (winTupleToPlace[1], str(waitTime)))
        gen_file.write("\n")
        # move window from this tuple in array of tuples given to the current desktop
        gen_file.write("wmctrl -r %s -t %s" % (winTupleToPlace[0] , desktop))
        gen_file.write("\n")
        gen_file.write("\n")

gen_file.write("exit 0")
gen_file.close()

# TODO: chmod the written file
