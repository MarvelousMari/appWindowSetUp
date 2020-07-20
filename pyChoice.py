import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

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

        self.show()

    @pyqtSlot()
    def android_on_click(self):
        print('android_on_click')
        androidSubProc = subprocess.run(["./androidDesktopLauncher.sh"])
        sys.exit()

    @pyqtSlot()
    def bash_on_click(self):
        print('bash_on_click')
        bashSubProc = subprocess.run(['./bashDesktopLauncher.sh'])
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
