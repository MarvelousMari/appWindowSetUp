# get the appplications to launch
# get the desired desktop config
# create script to have launch on start

import subprocess
import time

# wait time that can be set if needed cause of programs launching to slowly
waitTime = 2

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
    appSubProc = subprocess.run([app,' &', 'sleep', waitTime ])
    # TODO: get PID to kill later
    # sleep to allow for program to launch GUI
    time.sleep(waitTime)
    # get most recently opened window
    windowsOpen = subprocess.run(['wmctrl -l | tail -n 1'], shell=True, capture_output=True, text=True, check=True)
    # check to see if the terminal launch command(app) is already a part of the window descriptor
    # if it is add it to the dictionary
    if app.lower() in windowsOpen.stdout.lower():
        windowNames[app] = app
    # else ask for what part of the app window header is always there
    else:
        print("what part of this line: ")
        print(windowsOpen.stdout.lower())
        print("is always in the header of the %s window: " % (app))
        windowNames[app] = input().lower()

print("windowNames dict contains: ")
print(windowNames)

# windowName : desktopNum
windowLocations = {}
print("desktops start at 0, you can not create an empty desktop inbetween")
currentDesktop = 0
while len(windowNames) > 0:
    print("add an application to desktop %s " % (currentDesktop))
    appInput = input("OR input NEXT to move to the next desktop: ")
    if appInput in windowNames:
        windowLocations[windowNames[appInput]] = currentDesktop
        del windowNames[appInput]
    elif appInput == "NEXT":
        currentDesktop = currentDesktop + 1
    else:
        print("'%s' is not a valid appName")

print(windowLocations)
