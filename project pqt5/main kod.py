import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow
from start import Ui_MainWindowStart
from home import Ui_MainWindowHome
from info import Ui_MainWindowInfo
import imges
import datetime


class WrongDate(Exception):
    pass


class WrongWage(Exception):
    pass


class InfoW(QMainWindow, Ui_MainWindowInfo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_perehod)

    def start_perehod(self):
        self.window = StartW()
        self.window.show()
        self.close()


class StartW(QMainWindow, Ui_MainWindowStart):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.home_perehod)
        self.pushButton_2.clicked.connect(self.info_perehod)

    def home_perehod(self):
        self.window = HomeW()
        self.window.show()
        self.close()

    def info_perehod(self):
        self.window = InfoW()
        self.window.show()
        self.close()


class HomeW(QMainWindow, Ui_MainWindowHome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.move_back)
        self.pushButton_5.clicked.connect(self.user_inf)

    def move_back(self):
        self.window = StartW()
        self.window.show()
        self.close()

    def sbor(self):
        spis = []
        if self.dateEdit.date() <= QDate.currentDate():
            raise WrongDate
        else:
            spis.append(self.dateEdit.date())
        if int(self.lineEdit.text()) <= 0:
            raise WrongWage
        else:
            spis.append(self.lineEdit.text())
        if len(spis) == 2:
            return spis


    def user_inf(self):
        try:
            a = self.sbor()
            data = a[0]
            zarplata = a[1]
        except WrongDate:
            self.label_15.setText('Робот не доволен, ошибка в дате')
        except WrongWage:
            self.label_15.setText('Робот не доволен, ошибка в деньгах')
        except ValueError:
            self.label_15.setText('Робот не доволен, ошибка в вводе')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartW()
    ex.show()
    sys.exit(app.exec_())