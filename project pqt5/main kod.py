import sys
import sqlite3
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow

from start import Ui_MainWindowStart
from home import Ui_MainWindowHome
from info import Ui_MainWindowInfo
import changing_bd
import view_of_bd
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


class ChangingW(QMainWindow, changing_bd.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ViewW(QMainWindow, view_of_bd.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class HomeW(QMainWindow, Ui_MainWindowHome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.start_info()

        self.pushButton_4.clicked.connect(self.move_back)
        self.pushButton_5.clicked.connect(self.user_inf)

        self.pushButton_2.clicked.connect(self.changing_bd_win)
        self.pushButton_3.clicked.connect(self.view_of_bd_win)


    def move_back(self):
        self.window = StartW()
        self.window.show()
        self.close()

    def changing_bd_win(self):
        self.window = ChangingW()
        self.window.show()
        self.close()

    def view_of_bd_win(self):
        self.window = ViewW()
        self.window.show()
        self.close()

    def start_info(self):
        con = sqlite3.connect("basa.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM user""").fetchall()[0]

        cur.close()
        con.close()

        if len(str(result[4])) == 1:
            a = f'0{result[4]}'
        else:
            a = f'{result[4]}'
        if len(str(result[0])) == 1:
            b = f'0{result[0]}'
        else:
            b = f'{result[0]}'

        dayZP = "-".join([str(result[3]), a, b])
        firstDay = QDate.fromString(dayZP, "yyyy-MM-dd")
        a = QDate.currentDate().toString('yyyy-MM-dd')
        now = QDate.fromString(a, "yyyy-MM-dd")


        #добавление в таблицы информации из бд


        try:
            if firstDay == now:
                self.label_11.setText(str(0))
                self.label_15.setText('Робот загрузил последние данные')
                self.label_9.setText('0')
                self.progressBar.setValue(0)
            else:

                numDay = now.daysTo(firstDay)
                self.label_11.setText(str(numDay))

                ostatok = result[1]
                self.label_9.setText(str(ostatok))

                self.progressBar.setValue(int(result[1] / result[2] * 100))

                self.lineEdit.setText(str(result[2]))
                self.dateEdit.setDate(firstDay)
                self.label_15.setText('Робот загрузил последние данные')
        except Exception:
            self.label_11.setText(str(0))
            self.label_15.setText('Робот загрузил последние данные')
            self.label_9.setText('0')
            self.progressBar.setValue(0)



    def sbor(self):
        spis = []
        firstDayText = self.dateEdit.date().toString('yyyy-MM-dd')
        firstDay = QDate.fromString(firstDayText, "yyyy-MM-dd")
        now = QDate.currentDate()
        numDay = now.daysTo(firstDay)

        if numDay <= 0:
            raise WrongDate
        else:
            spis.append(numDay)
            if int(self.lineEdit.text()) <= 0:
                raise WrongWage
            else:
                spis.append(self.lineEdit.text())
                spis.append(firstDayText)
        if len(spis) == 3:
            return spis


    def user_inf(self):
        try:
            a = self.sbor()
            data = a[0]
            zarplata = a[1]
            self.label_11.setText(str(data))
            self.label_9.setText(str(zarplata))
            dayZP = str(a[2].split('-')[2])
            monthZP = str(a[2].split('-')[1])
            yearZP = str(a[2].split('-')[0])

            con = sqlite3.connect("basa.db")
            cur = con.cursor()

            cur.execute(f"""UPDATE user SET СуммаДенег = {int(zarplata)}""")
            cur.execute(f"""UPDATE user SET потрачено = {1}""") # сделать функцию которая будет считать все траты
            cur.execute(f"""UPDATE user SET ДеньЗП = {dayZP}""")
            cur.execute(f"""UPDATE user SET ГодЗП = {yearZP}""")
            cur.execute(f"""UPDATE user SET МесяцЗП = {monthZP}""")

            con.commit()
            cur.close()
            con.close()

            self.start_info()

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
