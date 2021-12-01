# -*- coding: utf-8 -*-

# self.form implementation generated from reading ui file 'uis/user_page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_Form(object):
    def __init__(self,Form):
        self.form = Form
        self.setupUi()

    def buttonStyle(self):
        return """
        QPushButton {
            color: black;
            border: 1px solid rgb(236, 236, 236);
            border-radius: 3px;
            width: 30px;
            height: 20px;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(236, 236, 236), stop: 1 rgb(236, 236, 236));
        }
        QPushButton:hover {
            color: #fff;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(179, 176, 176), stop: 1 rgb(179, 176, 176));
        }
        QPushButton:pressed {
            color: #fff;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E09825, stop: 1 #E09825);
        }
        """
    
    def buttonNavStyle(self):
        return """
        QPushButton{
        background-color: #241a16;
        color: #fff;
        }
        QPushButton:hover {
            color: #fff;
            background-color: #0c0807;
        }
        QPushButton:pressed {
            color: #fff;
            background-color: #E09825;
        }"""
    
    def ButtonImageStyle(self):
        return """
        QPushButton{
            border-image: url(:/images/mojito.jpg);
            background-repeat: no-repeat;
        }
        QPushButton:hover {
            opacity:0.3;
        }
        QPushButton:pressed {
            background-color: #E09825;
        }"""
    
    def setupUi(self):
        self.form.setObjectName("self.form")
        self.form.resize(800, 380)
        self.form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.form.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "")
        self.label = QtWidgets.QLabel(self.form)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 74))
        self.label.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: bold;\n"
        "font-size: 36px;\n"
        "line-height: 42px;\n"
        "\n"
        "color: #FFFFFF;\n"
        "background-color: #E09825;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.form)
        self.pushButton.setGeometry(QtCore.QRect(735, 10, 50, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QIcon('assets/settings.png'))
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2 = QtWidgets.QPushButton(self.form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 310, 65, 65))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QIcon('assets/queue.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 340, 500, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #region button menu
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet(self.buttonStyle())
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet(self.buttonStyle())
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet(self.buttonStyle())
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setStyleSheet(self.buttonStyle())
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setStyleSheet(self.buttonStyle())
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setStyleSheet(self.buttonStyle())
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setStyleSheet(self.buttonStyle())
        self.horizontalLayout.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setStyleSheet(self.buttonStyle())
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setStyleSheet(self.buttonStyle())
        self.horizontalLayout.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setStyleSheet(self.buttonStyle())
        self.horizontalLayout.addWidget(self.pushButton_15)
        #endregion button menu
        
        self.label_2 = QtWidgets.QLabel(self.form)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 150, 30))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("border-top-left-radius: 5px;"
                                   "border-top-right-radius: 20px;"
                                   "border: 1px solid black;")

        self.label_3 = QtWidgets.QLabel(self.form)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 150, 130))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("border-bottom-left-radius: 20px;"
                                   "border-bottom-right-radius: 5px;"
                                   "border: 1px solid black;")

        self.label_4 = QtWidgets.QLabel(self.form)
        self.label_4.setGeometry(QtCore.QRect(641, 110, 150, 30))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("border-top-left-radius: 5px;"
                                   "border-top-right-radius: 20px;"
                                   "border: 1px solid black;")

        self.label_5 = QtWidgets.QLabel(self.form)
        self.label_5.setGeometry(QtCore.QRect(641, 140, 150, 130))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("border-bottom-left-radius: 20px;"
                                   "border-bottom-right-radius: 5px;"
                                   "border: 1px solid black;")

        self.pushButton_3 = QtWidgets.QPushButton(self.form)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 310, 65, 65))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-image: url(:/check/assets/check2.png);\n"
        "border-radius:30px\n"
        "")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("crt_pushButton_2")
        self.pushButton_3.setIcon(QIcon('assets/check2.png'))
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setStyleSheet("border-radius:30px\noverflow:hidden;")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.form)
        self.pushButton_4.setGeometry(QtCore.QRect(165, 90, 30, 230))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(self.buttonNavStyle())
        
        self.pushButton_5 = QtWidgets.QPushButton(self.form)
        self.pushButton_5.setGeometry(QtCore.QRect(605, 90, 30, 230))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(self.buttonNavStyle())
        
        
        self.label_6 = QtWidgets.QLabel(self.form)
        self.label_6.setGeometry(QtCore.QRect(195, 290, 205, 30))
        self.label_6.setStyleSheet("background-color: rgba(0,0,0,0.5);"
                                   "color: #fff;"
                                   "padding-left: 15px;"
                                   "border-top-right-radius: 20px;")
        self.label_6.setObjectName("label_6")
        self.pushButton_16 = QtWidgets.QPushButton(self.form)
        self.pushButton_16.setGeometry(QtCore.QRect(195, 90, 410, 230))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_6.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle(_translate("self.form", "Mixology"))
        self.label.setText(_translate("self.form", "    MIXOLOGY"))
        self.pushButton_6.setText(_translate("self.form", "1"))
        self.pushButton_7.setText(_translate("self.form", "2"))
        self.pushButton_8.setText(_translate("self.form", "3"))
        self.pushButton_9.setText(_translate("self.form", "4"))
        self.pushButton_10.setText(_translate("self.form", "5"))
        self.pushButton_11.setText(_translate("self.form", "6"))
        self.pushButton_12.setText(_translate("self.form", "7"))
        self.pushButton_13.setText(_translate("self.form", "8"))
        self.pushButton_14.setText(_translate("self.form", "9"))
        self.pushButton_15.setText(_translate("self.form", "10"))
        self.label_2.setText(_translate("self.form", "Líquidos"))
        self.label_3.setText(_translate("self.form", "- item 1\n"
        "- item 2\n"
        "- item 3\n"
        "- item 4\n"
        "- item 5\n"
        "- item 6"))
        self.label_4.setText(_translate("self.form", "Sólidos"))
        self.label_5.setText(_translate("self.form", "- item 1\n"
        "- item 2\n"
        "- item 3\n"
        "- item 4\n"
        "- item 5\n"
        "- item 6"))
        self.pushButton_4.setText(_translate("self.form", "<"))
        self.pushButton_5.setText(_translate("self.form", ">"))
        self.label_6.setText(_translate("self.form", "Nombre"))
        self.pushButton_16.setIcon(QIcon('images/mojito.jpg'))
        self.pushButton_16.setIconSize(QtCore.QSize(410, 230))
        self.pushButton_16.setStyleSheet(self.ButtonImageStyle())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())

