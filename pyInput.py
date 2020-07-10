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

# print("applist: %s" % (appList))

# dict for window name : app launch cmd
windowNames = {}

# get the window names of all of the apps
for app in appList:
    # launch the apps
    appSubProc = subprocess.run(['./appLaunch.sh', app , str(waitTime)], capture_output=True, text=True)
    # check to see if the terminal launch command(app) is already a part of the window descriptor
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

# desktopNum : [(windowName, launch cmd)]
# {0: [(firefox, firefox),(atom, flatpak run io.atom.Atom)]}
windowLocations = {}
print("desktops start at 0, you can not create an empty desktop inbetween")
# desktop apps are being added to
currentDesktop = 0
# how many desktops are available
desktopsAvailable = 0
# while there are windows that haven't been assigned
print("add an application to desktop OR input NEXT to move to the next desktop")
# windowNames.keys() is the name of the windows that the user provided
print("application to choose from:", (windowNames.keys()))
# like a for loop through the whole appList but can be out of order for easier use
numberOfApps = len(appList)
while numberOfApps > 0 :
    # adsaf@asdf $"desktop 0:" ## should be a window name
    InputedWindowName = input("desktop %s:   " % (currentDesktop))
    # if the input is a valid windowName
    if InputedWindowName in windowNames:
        try:
            # add to windowLocations [desktopnum] = Val array of tuples [].append(windowName, launch command)
            windowLocations[currentDesktop].append( (InputedWindowName, windowNames[InputedWindowName]) )
            # remove from the possible options to prevent double placing
            numberOfApps = numberOfApps - 1
        # catch the exception that there is no value for that in the dictionary already and so you can't use "".append"
        except :
            # add to windowLocations [desktopnum] = Array of tuples[(append(windowName, launch command)]
            windowLocations[currentDesktop] = [ ( InputedWindowName, windowNames[InputedWindowName] ) ]
            numberOfApps = numberOfApps - 1
        # TODO: CHECK TO SEE IF MULTIPLE OF THE SAME WINDOW WORKS
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
        # else if desktopsAvailable is 2 higher(empty desktop)
        else:
            print("can't have an empty desktop")
    # if not valid input
    else:
        print("'%s' is not a valid input" % (InputedWindowName))
    print("")

print("")

# desktopNum : [(windowName, launch cmd)]
# {0: [(firefox, firefox),(atom, flatpak run io.atom.Atom)]}
print("windowLocations: %s" % (windowLocations))
# dict for window name : app launch cmd
print("windowNames: %s" % (windowNames))
# list of launch cmds
print("appList: %s" % (appList))


# windowLocations: {0: [('firefox', 'firefox'), ('atom', 'flatpak run io.atom.Atom')], 1: [('gedit', 'gedit')], 2: [('spotify', 'flatpak run com.spotify.Client')]}
# windowNames: {'firefox': 'firefox', 'atom': 'flatpak run io.atom.Atom', 'gedit': 'gedit', 'spotify': 'flatpak run com.spotify.Client'}
# appList: ['firefox', 'flatpak run io.atom.Atom', 'gedit', 'flatpak run com.spotify.Client']


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

for desktop in windowLocations:
    # for each tuple in the array that is the value of the windowLocations current desktop from loop above
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
