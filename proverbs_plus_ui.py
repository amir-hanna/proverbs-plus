# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proverbs_plus_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 278)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit_page_0 = QtWidgets.QPlainTextEdit(self.page_0)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plainTextEdit_page_0.setFont(font)
        self.plainTextEdit_page_0.setStyleSheet("background-color: #ffffcc; padding: 5px 5px 5px 5px;")
        self.plainTextEdit_page_0.setReadOnly(True)
        self.plainTextEdit_page_0.setPlainText("")
        self.plainTextEdit_page_0.setObjectName("plainTextEdit_page_0")
        self.verticalLayout.addWidget(self.plainTextEdit_page_0)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_previous = QtWidgets.QPushButton(self.page_0)
        self.btn_previous.setObjectName("btn_previous")
        self.horizontalLayout.addWidget(self.btn_previous)
        self.btn_next = QtWidgets.QPushButton(self.page_0)
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout.addWidget(self.btn_next)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_screen_0 = QtWidgets.QPushButton(self.page_0)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_screen_0.setFont(font)
        self.btn_screen_0.setObjectName("btn_screen_0")
        self.horizontalLayout.addWidget(self.btn_screen_0)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plainTextEdit_page_1 = QtWidgets.QPlainTextEdit(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plainTextEdit_page_1.setFont(font)
        self.plainTextEdit_page_1.setStyleSheet("background-color: #EAFFF1; padding: 5px 5px 5px 5px;")
        self.plainTextEdit_page_1.setReadOnly(True)
        self.plainTextEdit_page_1.setObjectName("plainTextEdit_page_1")
        self.verticalLayout_3.addWidget(self.plainTextEdit_page_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_screen_1 = QtWidgets.QPushButton(self.page_1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_screen_1.setFont(font)
        self.btn_screen_1.setObjectName("btn_screen_1")
        self.horizontalLayout_2.addWidget(self.btn_screen_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page_1)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.plainTextEdit_page_0, self.btn_previous)
        MainWindow.setTabOrder(self.btn_previous, self.btn_next)
        MainWindow.setTabOrder(self.btn_next, self.btn_screen_0)
        MainWindow.setTabOrder(self.btn_screen_0, self.plainTextEdit_page_1)
        MainWindow.setTabOrder(self.plainTextEdit_page_1, self.btn_screen_1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proverbs"))
        self.btn_previous.setText(_translate("MainWindow", "Previous"))
        self.btn_next.setText(_translate("MainWindow", "Next"))
        self.btn_screen_0.setText(_translate("MainWindow", "-_-_-_-_-"))
        self.plainTextEdit_page_1.setPlainText(_translate("MainWindow", "Please Wait ..."))
        self.btn_screen_1.setText(_translate("MainWindow", "Go Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

