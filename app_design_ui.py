# Form implementation generated from reading ui file 'd:\флешка\pet-projects\yandex_lyceum_project\app_design.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 666)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_longitude = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_longitude.setGeometry(QtCore.QRect(350, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_longitude.setFont(font)
        self.label_longitude.setObjectName("label_longitude")
        self.lineEdit_longitude = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_longitude.setGeometry(QtCore.QRect(350, 50, 281, 31))
        self.lineEdit_longitude.setObjectName("lineEdit_longitude")
        self.label_scale = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_scale.setGeometry(QtCore.QRect(10, 80, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_scale.setFont(font)
        self.label_scale.setObjectName("label_scale")
        self.lineEdit_scale = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_scale.setGeometry(QtCore.QRect(10, 120, 621, 31))
        self.lineEdit_scale.setObjectName("lineEdit_scale")
        self.pushButton_search = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(290, 160, 75, 23))
        self.pushButton_search.setObjectName("pushButton_search")
        self.label_latitude = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_latitude.setGeometry(QtCore.QRect(10, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_latitude.setFont(font)
        self.label_latitude.setObjectName("label_latitude")
        self.lineEdit_latitude = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_latitude.setGeometry(QtCore.QRect(10, 50, 281, 31))
        self.lineEdit_latitude.setObjectName("lineEdit_latitude")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_longitude.setText(_translate("MainWindow", "Введите долготу"))
        self.label_scale.setText(_translate("MainWindow", "Введите масштаб"))
        self.pushButton_search.setText(_translate("MainWindow", "Найти"))
        self.label_latitude.setText(_translate("MainWindow", "Введите широту"))
