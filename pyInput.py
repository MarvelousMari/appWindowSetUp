# get the appplications to launch
# get the desired desktop config
# create script to have launch on start

import subprocess
import time

# wait time that can be set if needed cause of programs launching to slowly
waitTime = 5

# get applications to launch
print("please enter the applications you would like to launch one at a time")
print("when you're done entering applications input 'DONE'")
appList = []
while True:
    # make sure it's in proper terminal format
    app = input("use the format for launching the application in terminal including any arguments you use:\
    ")
    # TODO: add while catch correct input to prevent mistakes
    if app == 'DONE':
        break
    else:
        appList.append(app)

# dict for launch app cmd : window name
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
        print(appSubProc.stdout.lower())
        print("is always in the header of the %s window: " % (app))
        windowNames[app] = input().lower()

print("windowNames dict contains: ")
print(windowNames)

# windowName : desktopNum
windowLocations = {}
print("desktops start at 0, you can not create an empty desktop inbetween")
# desktop apps are being added to
currentDesktop = 0
# how many desktops are available
desktopsAvailable = 0
# while there are windows that haven't been assigned
print("add an application to desktop %s OR input NEXT to move to the next desktop" % (currentDesktop))
while len(windowNames) > 0:
    appInput = input("desktop %s:   " % (currentDesktop))
    # if the input is a valid windowName
    if appInput in windowNames:
        # add to windowLocations ~windowName : desktopNum~
        windowLocations[windowNames[appInput]] = currentDesktop
        # remove from the possible options to prevent double placing
        del windowNames[appInput]
        # TODO: CHECK TO SEE IF MULTIPLE OF THE SAME WINDOW WORKS
        # if currentDesktop is the highest available
        if currentDesktop == desktopsAvailable:
            # make another desktop available
            desktopsAvailable = desktopsAvailable + 1
    elif appInput == "NEXT":
        # if desktopsAvailable is only 1 higher than the current desktop
        if desktopsAvailable == (currentDesktop + 1):
            # move to the next desktop
            currentDesktop = currentDesktop + 1
        # else if desktopsAvailable is 2 higher(empty desktop)
        else:
            print("can't have an empty desktop")
    # if not valid input
    else:
        print("'%s' is not a valid input" % (appInput))

print(windowLocations)
