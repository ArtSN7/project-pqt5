import sys
import sqlite3
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import imges

GLOBAL = None


class Ui_MainWindowView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1000)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 1181, 51))
        self.label_2.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/pink home.png);\n"
"font: 75 36pt \"Arial\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(110, 70, 1081, 681))
        self.widget.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/home or main.png);")
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 311, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_2.setGeometry(QtCore.QRect(580, 110, 311, 361))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 111, 41))
        self.label_3.setStyleSheet("font: italic 16pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(580, 60, 111, 41))
        self.label_4.setStyleSheet("font: italic 16pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(70, 520, 311, 61))
        self.pushButton.setStyleSheet("font: 63 11pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 520, 311, 61))
        self.pushButton_5.setStyleSheet("font: 63 11pt \"Arial\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 70, 91, 681))
        self.widget_2.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/home or left.png);")
        self.widget_2.setObjectName("widget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 90, 40))
        self.pushButton_4.setStyleSheet("border-image: url(:/ad/project pqt5/materials for the proj/grey.png);")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ad/project pqt5/materials for the proj/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 80, 90, 40))
        self.pushButton_2.setStyleSheet("border-image: url(:/ad/project pqt5/materials for the proj/grey.png);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ad/project pqt5/materials for the proj/wishlist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 760, 1181, 241))
        self.widget_3.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/home or down.png);")
        self.widget_3.setObjectName("widget_3")
        self.label_15 = QtWidgets.QLabel(self.widget_3)
        self.label_15.setGeometry(QtCore.QRect(680, 60, 491, 71))
        self.label_15.setStyleSheet("font: 12pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 421, 71))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "CashCheck"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Новый столбец"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Новый столбец"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Новый столбец"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Новый столбец"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Новый столбец"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Новый столбец"))
        self.label_3.setText(_translate("MainWindow", "Покупки:"))
        self.label_4.setText(_translate("MainWindow", "Желания:"))
        self.pushButton.setText(_translate("MainWindow", "Поиск в покупках"))
        self.pushButton_5.setText(_translate("MainWindow", "Поиск в желаниях"))
        self.label_15.setText(_translate("MainWindow", "Приложение работает без сбоев. Все прекрасно - робот доволен!"))
        self.label.setText(_translate("MainWindow", "Подсказка:"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">Тут Вы можете просматривать текущую информацию по базам данным и искать нужную информацию, используя поиск</span></p></body></html>"))


class Ui_MainWindowStart(object):
    def setupUi(self, MainWindowStart):
        MainWindowStart.setObjectName("MainWindowStart")
        MainWindowStart.resize(1200, 1000)
        MainWindowStart.setMinimumSize(QtCore.QSize(1200, 1000))
        MainWindowStart.setMaximumSize(QtCore.QSize(1200, 1000))
        MainWindowStart.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/startluna.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindowStart)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 680, 351, 61))
        self.pushButton.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/grey start.png);\n"
"font: 36pt \"Arial\";")
        self.pushButton.setText("  GO MAIN")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ad/project pqt5/materials for the proj/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(52, 64))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 531, 121))
        self.label.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/pink start.png);\n"
"font: 75 72pt \"Arial\";")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 780, 351, 61))
        self.pushButton_2.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/grey start.png);\n"
"font: 36pt \"Arial\";\n"
"")
        self.pushButton_2.setText(" INFORM")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ad/project pqt5/materials for the proj/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(52, 64))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindowStart.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowStart)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindowStart.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowStart)
        self.statusbar.setObjectName("statusbar")
        MainWindowStart.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowStart)
        QtCore.QMetaObject.connectSlotsByName(MainWindowStart)

    def retranslateUi(self, MainWindowStart):
        _translate = QtCore.QCoreApplication.translate
        MainWindowStart.setWindowTitle(_translate("MainWindowStart", "MainWindow"))
        self.label.setText(_translate("MainWindowStart", "CachCheck"))


class Ui_MainWindowInfo(object):
    def setupUi(self, MainWindowInfo):
        MainWindowInfo.setObjectName("MainWindowInfo")
        MainWindowInfo.resize(1200, 1000)
        MainWindowInfo.setMinimumSize(QtCore.QSize(1200, 1000))
        MainWindowInfo.setMaximumSize(QtCore.QSize(1200, 1000))
        MainWindowInfo.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/info or.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindowInfo)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 150, 511, 181))
        self.textBrowser.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/pink info.png);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 450, 231, 91))
        self.pushButton.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/grey info.png);\n"
"font: 87 14pt \"Arial\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ad/project pqt5/materials for the proj/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        MainWindowInfo.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindowInfo)
        self.statusbar.setObjectName("statusbar")
        MainWindowInfo.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowInfo)
        QtCore.QMetaObject.connectSlotsByName(MainWindowInfo)

    def retranslateUi(self, MainWindowInfo):
        _translate = QtCore.QCoreApplication.translate
        MainWindowInfo.setWindowTitle(_translate("MainWindowInfo", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindowInfo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Добрый день, вечер или утро! Я рад сообщить, что это проект для ЯЛицея по PyQT5 и Вы сейчас в маленьком описании данного проекта. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">На это приложение я потратил много времени и буду рад, если Вы оцените его по заслугам, ведь оно способно помочь Вам с вашей, видимо, финансовой проблемкой :)</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindowInfo", " ОБРАТНО"))


class Ui_MainWindowHome(object):
    def setupUi(self, MainWindowHome):
        MainWindowHome.setObjectName("MainWindowHome")
        MainWindowHome.setEnabled(True)
        MainWindowHome.resize(1200, 1000)
        MainWindowHome.setMinimumSize(QtCore.QSize(1200, 1000))
        MainWindowHome.setMaximumSize(QtCore.QSize(1200, 1000))
        MainWindowHome.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/startluna.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindowHome)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(110, 60, 1081, 681))
        self.widget.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/home or main.png);")
        self.widget.setObjectName("widget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 331, 191))
        self.calendarWidget.setObjectName("calendarWidget")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(490, 40, 561, 31))
        self.progressBar.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(350, 90, 481, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setEnabled(True)
        self.label_6.setStyleSheet("font: 16pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_9.setStyleSheet("font: 16pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setEnabled(True)
        self.label_10.setStyleSheet("font: 16pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(350, 140, 401, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_7.setStyleSheet("font: 16pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setStyleSheet("font: 16pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_8.setStyleSheet("font: 16pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(350, 40, 121, 31))
        self.label_12.setStyleSheet("font: 16pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(10, 230, 141, 31))
        self.label_13.setStyleSheet("font: 16pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(550, 230, 111, 31))
        self.label_14.setStyleSheet("font: 16pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 270, 321, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_2.setGeometry(QtCore.QRect(550, 270, 321, 341))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 91, 681))
        self.widget_2.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/home or left.png);")
        self.widget_2.setObjectName("widget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 90, 40))
        self.pushButton_4.setStyleSheet("border-image: url(:/ad/project pqt5/materials for the proj/grey.png);")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ad/project pqt5/materials for the proj/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 90, 90, 40))
        self.pushButton_3.setStyleSheet("border-image: url(:/ad/project pqt5/materials for the proj/grey.png);")
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ad/project pqt5/materials for the proj/give-money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 180, 90, 40))
        self.pushButton_2.setStyleSheet("border-image: url(:/ad/project pqt5/materials for the proj/grey.png);")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ad/project pqt5/materials for the proj/wishlist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 750, 1181, 241))
        self.widget_3.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/home or down.png);")
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 528, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setStyleSheet("font: 16pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 531, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setStyleSheet("font: 16pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setStyleSheet("font: 16pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(710, 30, 351, 61))
        self.pushButton_5.setStyleSheet("border-image: url(:/ad/project pqt5/materials for the proj/grey.png);\n"
"font: 26pt \"Arial\";")
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_15 = QtWidgets.QLabel(self.widget_3)
        self.label_15.setGeometry(QtCore.QRect(640, 100, 491, 71))
        self.label_15.setStyleSheet("font: 12pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 1181, 51))
        self.label_2.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/pink home.png);\n"
"font: 75 36pt \"Arial\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindowHome.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowHome)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindowHome.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowHome)
        self.statusbar.setObjectName("statusbar")
        MainWindowHome.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowHome)
        QtCore.QMetaObject.connectSlotsByName(MainWindowHome)

    def retranslateUi(self, MainWindowHome):
        _translate = QtCore.QCoreApplication.translate
        MainWindowHome.setWindowTitle(_translate("MainWindowHome", "MainWindow"))
        self.label_6.setText(_translate("MainWindowHome", "Остаток:"))
        self.label_9.setText(_translate("MainWindowHome", "0"))
        self.label_10.setText(_translate("MainWindowHome", "(руб)"))
        self.label_7.setText(_translate("MainWindowHome", "До нового пополнения:  "))
        self.label_11.setText(_translate("MainWindowHome", "0"))
        self.label_8.setText(_translate("MainWindowHome", "(дней)"))
        self.label_12.setText(_translate("MainWindowHome", "Потрачено:"))
        self.label_13.setText(_translate("MainWindowHome", "Топ покупок:"))
        self.label_14.setText(_translate("MainWindowHome", "Последнее:"))
        self.label.setText(_translate("MainWindowHome", "ВАШИ ДАННЫЕ:"))
        self.label_3.setText(_translate("MainWindowHome", "Дата зачисления денег:"))
        self.label_4.setText(_translate("MainWindowHome", "Сумма сейчас:"))
        self.label_5.setText(_translate("MainWindowHome", "(руб)"))
        self.pushButton_5.setText(_translate("MainWindowHome", "ОБНОВИТЬ ДАННЫЕ"))
        self.label_15.setText(_translate("MainWindowHome", "Приложение работает без сбоев. Все прекрасно - робот доволен!"))
        self.label_2.setText(_translate("MainWindowHome", "CashCheck"))


class Ui_MainWindowChoise2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 226)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 170, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 16))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 60, 69, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 191, 16))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 60, 191, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "поиск"))
        self.label.setText(_translate("MainWindow", "Выберите условие поиска:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "id"))
        self.comboBox.setItemText(1, _translate("MainWindow", "название"))
        self.comboBox.setItemText(2, _translate("MainWindow", "цена"))
        self.comboBox.setItemText(3, _translate("MainWindow", "магазин"))
        self.label_2.setText(_translate("MainWindow", "Введите информацию для поиска:"))


class Ui_MainWindowChoise(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 226)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 170, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 16))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 60, 69, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 191, 16))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 60, 191, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "поиск"))
        self.label.setText(_translate("MainWindow", "Выберите условие поиска:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "id"))
        self.comboBox.setItemText(1, _translate("MainWindow", "название"))
        self.comboBox.setItemText(2, _translate("MainWindow", "цена"))
        self.comboBox.setItemText(3, _translate("MainWindow", "магазин"))
        self.label_2.setText(_translate("MainWindow", "Введите информацию для поиска:"))


class Ui_MainWindowChanging(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1000)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 1181, 51))
        self.label_2.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/pink home.png);\n"
"font: 75 36pt \"Arial\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 70, 91, 681))
        self.widget_2.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/home or left.png);")
        self.widget_2.setObjectName("widget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 90, 40))
        self.pushButton_4.setStyleSheet("border-image: url(:/ad/project pqt5/materials for the proj/grey.png);")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ad/project pqt5/materials for the proj/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 90, 90, 40))
        self.pushButton_3.setStyleSheet("border-image: url(:/ad/project pqt5/materials for the proj/grey.png);")
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ad/project pqt5/materials for the proj/give-money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(110, 70, 1081, 681))
        self.widget.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/home or main.png);")
        self.widget.setObjectName("widget")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(10, 10, 381, 151))
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 141, 16))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 141, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 80, 141, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 120, 141, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(480, 10, 381, 151))
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_5)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 40, 141, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 80, 141, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 120, 141, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setGeometry(QtCore.QRect(10, 200, 381, 81))
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.label_11 = QtWidgets.QLabel(self.widget_6)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 141, 16))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_6)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 40, 141, 20))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 40, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setGeometry(QtCore.QRect(480, 200, 381, 81))
        self.widget_7.setStyleSheet("")
        self.widget_7.setObjectName("widget_7")
        self.label_13 = QtWidgets.QLabel(self.widget_7)
        self.label_13.setGeometry(QtCore.QRect(10, 0, 141, 16))
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget_7)
        self.label_14.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 40, 141, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 40, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setGeometry(QtCore.QRect(10, 330, 381, 151))
        self.widget_8.setStyleSheet("")
        self.widget_8.setObjectName("widget_8")
        self.label_16 = QtWidgets.QLabel(self.widget_8)
        self.label_16.setGeometry(QtCore.QRect(10, 40, 231, 16))
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_16.setObjectName("label_16")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_9.setGeometry(QtCore.QRect(240, 40, 141, 20))
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 120, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_19 = QtWidgets.QLabel(self.widget_8)
        self.label_19.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_19.setObjectName("label_19")
        self.comboBox = QtWidgets.QComboBox(self.widget_8)
        self.comboBox.setGeometry(QtCore.QRect(10, 70, 81, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_10.setGeometry(QtCore.QRect(240, 70, 141, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_17 = QtWidgets.QLabel(self.widget_8)
        self.label_17.setGeometry(QtCore.QRect(100, 70, 131, 16))
        self.label_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_17.setObjectName("label_17")
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setGeometry(QtCore.QRect(480, 330, 381, 151))
        self.widget_9.setStyleSheet("")
        self.widget_9.setObjectName("widget_9")
        self.label_20 = QtWidgets.QLabel(self.widget_9)
        self.label_20.setGeometry(QtCore.QRect(10, 40, 231, 16))
        self.label_20.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_20.setObjectName("label_20")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_12.setGeometry(QtCore.QRect(240, 40, 141, 20))
        self.lineEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 120, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_23 = QtWidgets.QLabel(self.widget_9)
        self.label_23.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_23.setObjectName("label_23")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_9)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 70, 81, 22))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_11.setGeometry(QtCore.QRect(240, 70, 141, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_18 = QtWidgets.QLabel(self.widget_9)
        self.label_18.setGeometry(QtCore.QRect(100, 70, 131, 16))
        self.label_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Arial\";")
        self.label_18.setObjectName("label_18")
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setGeometry(QtCore.QRect(290, 540, 311, 41))
        self.label_21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Arialpip\";")
        self.label_21.setObjectName("label_21")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 760, 1181, 241))
        self.widget_3.setStyleSheet("background-image: url(:/ad/project pqt5/materials for the proj/home or down.png);")
        self.widget_3.setObjectName("widget_3")
        self.label_15 = QtWidgets.QLabel(self.widget_3)
        self.label_15.setGeometry(QtCore.QRect(680, 60, 491, 71))
        self.label_15.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setStyleSheet("font: 75 12pt \"System\";")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 421, 71))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "CashCheck"))
        self.label_3.setText(_translate("MainWindow", "Добавить в покупки:"))
        self.label_4.setText(_translate("MainWindow", "Название:"))
        self.label_5.setText(_translate("MainWindow", "Цена:"))
        self.label_6.setText(_translate("MainWindow", "Магазин:"))
        self.pushButton.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        self.label_8.setText(_translate("MainWindow", "Название:"))
        self.label_9.setText(_translate("MainWindow", "Цена:"))
        self.label_10.setText(_translate("MainWindow", "Магазин:"))
        self.pushButton_2.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        self.label_7.setText(_translate("MainWindow", "Добавить в желания:"))
        self.label_11.setText(_translate("MainWindow", "Удалить из покупок:"))
        self.label_12.setText(_translate("MainWindow", "НАЗВАНИЕ:"))
        self.pushButton_5.setText(_translate("MainWindow", "УДАЛИТЬ"))
        self.label_13.setText(_translate("MainWindow", "Удалить из желаний:"))
        self.label_14.setText(_translate("MainWindow", "НАЗВАНИЕ:"))
        self.pushButton_6.setText(_translate("MainWindow", "УДАЛИТЬ"))
        self.label_16.setText(_translate("MainWindow", "Наз.  вещи , которую редактируем:"))
        self.pushButton_7.setText(_translate("MainWindow", "РЕДАКТ."))
        self.label_19.setText(_translate("MainWindow", "Редактировать в покупках:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "название"))
        self.comboBox.setItemText(1, _translate("MainWindow", "цена"))
        self.comboBox.setItemText(2, _translate("MainWindow", "магазин"))
        self.label_17.setText(_translate("MainWindow", "Новая информация:"))
        self.label_20.setText(_translate("MainWindow", "Наз. вещи , которую редактируем:"))
        self.pushButton_8.setText(_translate("MainWindow", "РЕДАКТ."))
        self.label_23.setText(_translate("MainWindow", "Редактировать в желаниях:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "название"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "цена"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "магазин"))
        self.label_18.setText(_translate("MainWindow", "Новая информация:"))
        self.label_21.setText(_translate("MainWindow", "РОБОТ ЖДЕТ ВАШИХ УКАЗАНИЙ!"))
        self.label_15.setText(_translate("MainWindow", "Приложение работает без сбоев. Все прекрасно - робот доволен!"))
        self.label.setText(_translate("MainWindow", "Подсказка:"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">Тут Вы можеет редактировать информацию из 2 баз данных: желания и совершенные покупки. Вам доступно удаление, добавление и редактирование.</span></p></body></html>"))


class WrongDate(Exception):
    pass


class WrongWage(Exception):
    pass


class ChoisePokW(QMainWindow, Ui_MainWindowChoise2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox.activated.connect(self.handleActivated)
        self.znach = 'id'

        self.pushButton.clicked.connect(self.run)

    def handleActivated(self, text):
        self.znach = ['id', 'название', 'цена', 'магазин'][int(text)]

    def run(self):
        text = self.lineEdit.text()
        try:
            buy = []
            con = sqlite3.connect("basa.db")
            cur = con.cursor()
            if self.znach == 'id':
                buy = cur.execute("""SELECT название, цена, магазин FROM buy WHERE id = ?""", (text,)).fetchall()
            if self.znach == 'цена':
                buy = cur.execute("""SELECT название, цена, магазин FROM buy WHERE цена = ?""", (text,)).fetchall()
            if self.znach == 'магазин':
                buy = cur.execute("""SELECT название, цена, магазин FROM buy WHERE магазин = ?""", (text,)).fetchall()
            if self.znach == 'название':
                buy = cur.execute("""SELECT название, цена, магазин FROM buy WHERE название = ?""", (text,)).fetchall()
            cur.close()
            con.close()

            if len(buy) == 0:
                raise ValueError
            else:
                ViewW.make_tabl_pok(GLOBAL, buy)
                self.close()
        except ValueError:
            self.lineEdit.setText("НЕТ ТАКОГО")
        except Exception:
            self.lineEdit.setText("ОШИБКА В ДАННЫХ, TRY AGAIN")


class ChoiseWantW(QMainWindow, Ui_MainWindowChoise):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox.activated.connect(self.handleActivated)
        self.znach = 'id'

        self.pushButton.clicked.connect(self.run)

    def handleActivated(self, text):
        self.znach = ['id', 'название', 'цена', 'магазин'][int(text)]

    def run(self):
        text = self.lineEdit.text()
        try:
            buy = []
            con = sqlite3.connect("basa.db")
            cur = con.cursor()
            if self.znach == 'id':
                buy = cur.execute("""SELECT название, цена, магазин FROM want WHERE id = ?""", (text,)).fetchall()
            if self.znach == 'цена':
                buy = cur.execute("""SELECT название, цена, магазин FROM want WHERE цена = ?""", (text,)).fetchall()
            if self.znach == 'магазин':
                buy = cur.execute("""SELECT название, цена, магазин FROM want WHERE магазин = ?""", (text,)).fetchall()
            if self.znach == 'название':
                buy = cur.execute("""SELECT название, цена, магазин FROM want WHERE название = ?""", (text,)).fetchall()
            cur.close()
            con.close()

            if len(buy) == 0:
                raise ValueError
            else:
                ViewW.make_tabl_want(GLOBAL, buy)
                self.close()
        except ValueError:
            self.lineEdit.setText("НЕТ ТАКОГО")
        except Exception:
            self.lineEdit.setText("ОШИБКА В ДАННЫХ, TRY AGAIN")


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


class ChangingW(QMainWindow, Ui_MainWindowChanging):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_21.setText("РОБОТ ЖДЕТ ВАШИХ УКАЗАНИЙ!")

        self.pushButton_4.clicked.connect(self.move_back)
        self.pushButton_3.clicked.connect(self.view_w)

        self.pushButton.clicked.connect(self.add_pok)
        self.pushButton_5.clicked.connect(self.del_pok)
        self.pushButton_7.clicked.connect(self.red_pok)

        self.pushButton_2.clicked.connect(self.add_want)
        self.pushButton_6.clicked.connect(self.del_want)
        self.pushButton_8.clicked.connect(self.red_want)

        self.comboBox.activated.connect(self.handleActivated)
        self.znach = 'название'

        self.comboBox_2.activated.connect(self.handleActivated_2)
        self.znach_2 = 'название'

    def check_spend(self):
        con = sqlite3.connect("basa.db")
        cur = con.cursor()
        result = cur.execute("""SELECT цена FROM buy""").fetchall()
        count = 0
        for i in result:
            count += int(i[0])

        cur.execute("""UPDATE user SET потрачено = ?""", (count,))
        con.commit()
        cur.close()
        con.close()

    def handleActivated(self, text):
        self.znach = ['название', 'цена', 'магазин'][int(text)]

    def handleActivated_2(self, text):
        self.znach_2 = ['название', 'цена', 'магазин'][int(text)]

    def add_pok(self):
        try:
            con = sqlite3.connect("basa.db")
            cur = con.cursor()

            iD = cur.execute("""SELECT * FROM buy""").fetchall()[::-1]
            money = cur.execute("""SELECT * FROM user""").fetchall()[0]
            summa = money[2]
            spend = int(money[1]) + int(self.lineEdit_2.text())
            if spend > summa:
                cur.close()
                con.close()
                raise WrongWage
            else:
                if len(iD) != 0:
                    cur.execute("""INSERT INTO buy(id, название, цена, магазин) VALUES(?, ?, ?, ?)""",
                                (int(iD[0][0]) + 1, str(self.lineEdit.text()), int(self.lineEdit_2.text()),
                                 str(self.lineEdit_3.text())))
                else:
                    cur.execute("""INSERT INTO buy(id, название, цена, магазин) VALUES(?, ?, ?, ?)""",
                                (1, str(self.lineEdit.text()), int(self.lineEdit_2.text()),
                                 str(self.lineEdit_3.text())))
                con.commit()
                self.label_21.setText("  РОБОТ ВЫПОЛНИЛ ЗАДАЧУ")
                self.check_spend()

                cur.close()
                con.close()
        except WrongWage:
            self.label_21.setText("НЕДОСТАТОЧНО СРЕДСТВ")
        except Exception:
            self.label_21.setText("ОШИБКА В ДАННЫХ, ПОВТОРИТЕ ПОПЫТКУ")


    def del_pok(self):
        try:
            con = sqlite3.connect("basa.db")
            cur = con.cursor()
            cur.execute("""DELETE from buy where название = ?""", (self.lineEdit_7.text(),))
            con.commit()
            self.label_21.setText("  РОБОТ ВЫПОЛНИЛ ЗАДАЧУ")
            self.check_spend()
            cur.close()
            con.close()
        except Exception:
            self.label_21.setText("ОШИБКА В ДАННЫХ, ПОВТОРИТЕ ПОПЫТКУ")

    def red_pok(self):
        try:
            con = sqlite3.connect('basa.db')
            cur = con.cursor()
            if self.znach == 'цена':
                money = cur.execute("""SELECT * FROM user""").fetchall()[0]
                summa = money[2]
                spend = int(money[1]) + int(self.lineEdit_10.text())
                if spend > summa:
                    cur.close()
                    con.close()
                    raise WrongWage
                else:
                    cur.execute("""UPDATE buy SET цена = ? WHERE название = ?""", (int(self.lineEdit_10.text()), str(self.lineEdit_9.text())))
            if self.znach == 'магазин':
                cur.execute("""UPDATE buy SET магазин = ? WHERE название = ?""", (str(self.lineEdit_10.text()), str(self.lineEdit_9.text())))
            if self.znach == 'название':
                cur.execute("""UPDATE buy SET название = ? WHERE название = ?""", (str(self.lineEdit_10.text()), str(self.lineEdit_9.text())))
            con.commit()
            self.label_21.setText("  РОБОТ ВЫПОЛНИЛ ЗАДАЧУ")
            self.check_spend()

            cur.close()
            con.close()
        except WrongWage:
            self.label_21.setText("НЕДОСТАТОЧНО СРЕДСТВ")
        except Exception:
            self.label_21.setText("ОШИБКА В ДАННЫХ, ПОВТОРИТЕ ПОПЫТКУ")

    def add_want(self):
        try:
            con = sqlite3.connect("basa.db")
            cur = con.cursor()

            iD = cur.execute("""SELECT * FROM want""").fetchall()[::-1]

            if len(iD) != 0:
                cur.execute("""INSERT INTO want(id, название, цена, магазин) VALUES(?, ?, ?, ?)""",
                            (int(iD[0][0]) + 1, str(self.lineEdit_4.text()), int(self.lineEdit_5.text()),
                             str(self.lineEdit_6.text())))
            else:
                cur.execute("""INSERT INTO want(id, название, цена, магазин) VALUES(?, ?, ?, ?)""",
                            (1, str(self.lineEdit_4.text()), int(self.lineEdit_5.text()),
                             str(self.lineEdit_6.text())))
            con.commit()
            self.label_21.setText("  РОБОТ ВЫПОЛНИЛ ЗАДАЧУ")

            cur.close()
            con.close()
        except Exception:
            self.label_21.setText("ОШИБКА В ДАННЫХ, ПОВТОРИТЕ ПОПЫТКУ")

    def del_want(self):
        try:
            con = sqlite3.connect("basa.db")
            cur = con.cursor()
            cur.execute("""DELETE from want where название = ?""", (self.lineEdit_8.text(),))
            con.commit()
            self.label_21.setText("  РОБОТ ВЫПОЛНИЛ ЗАДАЧУ")
            cur.close()
            con.close()
        except Exception:
            self.label_21.setText("ОШИБКА В ДАННЫХ, ПОВТОРИТЕ ПОПЫТКУ")

    def red_want(self):
        try:
            con = sqlite3.connect('basa.db')
            cur = con.cursor()
            if self.znach_2 == 'цена':
                cur.execute("""UPDATE want SET цена = ? WHERE название = ?""",
                            (int(self.lineEdit_11.text()), str(self.lineEdit_12.text())))
            if self.znach_2 == 'магазин':
                cur.execute("""UPDATE want SET магазин = ? WHERE название = ?""",
                            (str(self.lineEdit_11.text()), str(self.lineEdit_12.text())))
            if self.znach_2 == 'название':
                cur.execute("""UPDATE want SET название = ? WHERE название = ?""",
                            (str(self.lineEdit_11.text()), str(self.lineEdit_12.text())))
            con.commit()
            self.label_21.setText("  РОБОТ ВЫПОЛНИЛ ЗАДАЧУ")

            cur.close()
            con.close()
        except Exception:
            self.label_21.setText("ОШИБКА В ДАННЫХ, ПОВТОРИТЕ ПОПЫТКУ")

    def move_back(self):
        self.window = HomeW()
        self.window.show()
        self.close()

    def view_w(self):
        self.window = ViewW()
        self.window.show()
        self.close()


class ViewW(QMainWindow, Ui_MainWindowView):
    def __init__(self):
        global GLOBAL
        super().__init__()
        self.setupUi(self)

        GLOBAL = self

        self.making_table()

        self.pushButton_4.clicked.connect(self.move_back)
        self.pushButton_2.clicked.connect(self.changing_bd_win)

        self.pushButton_5.clicked.connect(self.poisk_v_want)
        self.pushButton.clicked.connect(self.poisk_v_pok)

    def make_tabl_pok(self, res):
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['название', 'цена', 'магазин'])
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def make_tabl_want(self, res1):
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setHorizontalHeaderLabels(['название', 'цена', 'магазин'])
        # Заполняем таблицу элементами
        for i, row in enumerate(res1):
            self.tableWidget_2.setRowCount(
                self.tableWidget_2.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget_2.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def poisk_v_pok(self):
        self.window = ChoisePokW()
        self.window.show()

    def poisk_v_want(self):
        self.window = ChoiseWantW()
        self.window.show()


    def move_back(self):
        self.window = HomeW()
        self.window.show()
        self.close()

    def changing_bd_win(self):
        self.window = ChangingW()
        self.window.show()
        self.close()

    def making_table(self):
        #добавление в таблицы информации из бд о покупках
        con = sqlite3.connect("basa.db")
        cur = con.cursor()

        buy = cur.execute("""SELECT * FROM buy""").fetchall()
        res = [i[1:] for i in buy]

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['название', 'цена', 'магазин'])
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

        last = cur.execute("""SELECT * FROM want""").fetchall()
        res1 = [i[1:] for i in last]

        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setHorizontalHeaderLabels(['название', 'цена', 'магазин'])
        # Заполняем таблицу элементами
        for i, row in enumerate(res1):
            self.tableWidget_2.setRowCount(
                self.tableWidget_2.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget_2.setItem(
                    i, j, QTableWidgetItem(str(elem)))

        cur.close()
        con.close()


class HomeW(QMainWindow, Ui_MainWindowHome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.start_info()

        self.pushButton_4.clicked.connect(self.move_back)
        self.pushButton_5.clicked.connect(self.user_inf)

        self.pushButton_2.clicked.connect(self.changing_bd_win)
        self.pushButton_3.clicked.connect(self.view_of_bd_win)

# переход на окна
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

    def start_info(self): # отображение информации на виджетах окна home
        self.check_spend()
        con = sqlite3.connect("basa.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM user""").fetchall()[0]

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

        #добавление в таблицы информации из бд о покупках

        buy = cur.execute("""SELECT * FROM buy""").fetchall()
        buy.sort(key=lambda x: x[2], reverse=True)
        res = [i[1:] for i in buy]

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['название', 'цена', 'магазин'])
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

        last = cur.execute("""SELECT * FROM buy""").fetchall()[::-1]
        res1 = [i[1:] for i in last]

        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setHorizontalHeaderLabels(['название', 'цена', 'магазин'])
        # Заполняем таблицу элементами
        for i, row in enumerate(res1):
            self.tableWidget_2.setRowCount(
                self.tableWidget_2.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget_2.setItem(
                    i, j, QTableWidgetItem(str(elem)))

        cur.close()
        con.close()

        try:
            if firstDay == now:
                self.label_11.setText(str(0))
                self.label_15.setText('Робот загрузил последние данные')
                self.label_9.setText('0')
                self.progressBar.setValue(0)

                con = sqlite3.connect("basa.db")
                cur = con.cursor()
                cur.execute(f"""UPDATE user SET потрачено = {0}""")
            else:
                numDay = now.daysTo(firstDay)
                self.label_11.setText(str(numDay))

                ostatok = int(result[2]) - int(result[1])
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

    def check_spend(self):
        con = sqlite3.connect("basa.db")
        cur = con.cursor()
        result = cur.execute("""SELECT цена FROM buy""").fetchall()
        count = 0
        for i in result:
            count += int(i[0])

        cur.execute("""UPDATE user SET потрачено = ?""", (count,))
        con.commit()
        cur.close()
        con.close()

    def sbor(self): # собирает информацию из line_edits в графе (ваши данные)
        spis = []
        firstDayText = self.dateEdit.date().toString('yyyy-MM-dd')
        firstDay = QDate.fromString(firstDayText, "yyyy-MM-dd")
        now = QDate.currentDate()
        numDay = now.daysTo(firstDay)

        if numDay < 0:
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

    def user_inf(self): # обновление базы данных после нажатия кнопки в графе (ваши данные)
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