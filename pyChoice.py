import sys
import subprocess
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    pwd = os.path.dirname(os.path.realpath(__file__))

    launchWithDesktop = False

    def __init__(self):
        super().__init__()
        # need to alter the coordinates
        self.title = 'Launch Script'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Android', self)
        button.setToolTip('Launch android dev desktop configuration')
        # need to alter coordinates
        button.move(100,70)
        button.clicked.connect(self.android_on_click)

        # need to alter coordinates
        button = QPushButton('Bash', self)
        button.setToolTip('Launch bash dev desktop configuration')
        button.move(200,70)
        button.clicked.connect(self.bash_on_click)

        checkBox = QCheckBox("DesktopConnected", self)
        checkBox.stateChanged.connect(self.clickBox)
        checkBox.move(300,70)


        self.show()

    def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            launchWithDesktop = True
            print("LaunchWithDesktop = True")
        else:
            launchWithDesktop =False
            print("LaunchWithDesktop = False")

    @pyqtSlot()
    def android_on_click(self):
        print('android_on_click')
        androidCMD = os.path.dirname(os.path.realpath(__file__)) + "/androidDesktopLauncher.sh"
        androidSubProc = subprocess.run([androidCMD])
        sys.exit()

    @pyqtSlot()
    def bash_on_click(self):
        print('bash_on_click')
        bashCMD = os.path.dirname(os.path.realpath(__file__)) + "/bashDesktopLauncher.sh"
        bashSubProc = subprocess.run([bashCMD])
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
