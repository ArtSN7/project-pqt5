import sys

from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow
from start import Ui_MainWindowStart
from home import Ui_MainWindowHome
from info import Ui_MainWindowInfo
import imges


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

        self.user_inf(1)


        self.pushButton_4.clicked.connect(self.move_back)
        self.pushButton_5.clicked.connect(self.user_inf(0))


    def move_back(self):
        self.window = StartW()
        self.window.show()
        self.close()

    def sbor(self):
        spis = []
        firstDayText = self.dateEdit.dateTime().toString('yyyy-MM-dd')
        firstDay = QDateTime.fromString(firstDayText, "yyyy-MM-dd")
        now = QDateTime.currentDateTime()
        numDay = now.daysTo(firstDay)
        if numDay <= 0:
            raise WrongDate
        else:
            spis.append(numDay)
        if int(self.lineEdit.text()) <= 0:
            raise WrongWage
        else:
            spis.append(self.lineEdit.text())
        if len(spis) == 2:
            return spis


    def user_inf(self, flag):
        if flag == 0:
            try:
                a = self.sbor()
                data = a[0]
                zarplata = a[1]
                self.label_11.setText(str(data))
                self.label_9.setText(str(zarplata))
            except WrongDate:
                self.label_15.setText('Робот не доволен, ошибка в дате')
            except WrongWage:
                self.label_15.setText('Робот не доволен, ошибка в деньгах')
            except ValueError:
                self.label_15.setText('Робот не доволен, ошибка в вводе')
        else:
            firstDayText = self.dateEdit.dateTime().toString('yyyy-MM-dd')
            firstDay = QDateTime.fromString(firstDayText, "yyyy-MM-dd")
            now = QDateTime.currentDateTime()

            if #в базе данных лежит "now" или "firstDay":
                self.label_11.setText(str(0))
                self.label_15.setText('Робот загрузил последние данные')
                # очищаем 'label_9' и 'progressBar'
            else:
                #из базы данных берем день и считаем новую разницу, вставляем его в 'label_11' , также берем значение денег и обновляем 'progressBar'







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartW()
    ex.show()
    sys.exit(app.exec_())
