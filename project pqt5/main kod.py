import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from start import Ui_MainWindowStart
from home import Ui_MainWindowHome
from info import Ui_MainWindowInfo
import imges


class InfoW(QMainWindow, Ui_MainWindowInfo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.window = StartW()
        self.window.show()
        self.close()




class StartW(QMainWindow, Ui_MainWindowStart):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run1)

    def run(self):
        self.window = HomeW()
        self.window.show()
        self.close()

    def run1(self):
        self.window = InfoW()
        self.window.show()
        self.close()


class HomeW(QMainWindow, Ui_MainWindowHome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.run)

    def run(self):
        self.window = StartW()
        self.window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartW()
    ex.show()
    sys.exit(app.exec_())