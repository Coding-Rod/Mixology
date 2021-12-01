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
from apis.data import Data
from glob import glob

class Ui_Form(object):
    def __init__(self,Form):
        self.form = Form
        self.user_screen = 1
        self.dat = Data()
        self.user_page()

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
            background-color: #333;
        }"""
    
    def ButtonImageStyle(self):
        return """
        QPushButton{
            border-image: url(:/images/mojito.jpg);
            background-repeat: no-repeat;
        }
        QPushButton:hover {
            background-color: #aaa;
        }
        QPushButton:pressed {
            background-color: #E09825;
        }"""
    
    def user_page(self):
        self.form.setObjectName("self.form")
        self.form.resize(800, 380)
        self.form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.form.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "")
        self.usr_label = QtWidgets.QLabel(self.form)
        self.usr_label.setGeometry(QtCore.QRect(0, 0, 800, 74))
        self.usr_label.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: bold;\n"
        "font-size: 36px;\n"
        "line-height: 42px;\n"
        "\n"
        "color: #FFFFFF;\n"
        "background-color: #E09825;")
        self.usr_label.setObjectName("usr_label")
        self.usr_pushButton = QtWidgets.QPushButton(self.form)
        self.usr_pushButton.setGeometry(QtCore.QRect(735, 10, 50, 50))
        self.usr_pushButton.setObjectName("usr_pushButton")
        self.usr_pushButton.setIcon(QIcon('assets/settings.png'))
        self.usr_pushButton.setIconSize(QtCore.QSize(40, 40))
        self.usr_pushButton_2 = QtWidgets.QPushButton(self.form)
        self.usr_pushButton_2.setGeometry(QtCore.QRect(10, 310, 65, 65))
        self.usr_pushButton_2.setObjectName("usr_pushButton_2")
        self.usr_pushButton_2.setIcon(QIcon('assets/queue.png'))
        self.usr_pushButton_2.setIconSize(QtCore.QSize(50, 50))
        
        self.usr_horizontalLayoutWidget = QtWidgets.QWidget(self.form)
        self.usr_horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 340, 500, 30))
        self.usr_horizontalLayoutWidget.setObjectName("usr_horizontalLayoutWidget")
        self.usr_horizontalLayout = QtWidgets.QHBoxLayout(self.usr_horizontalLayoutWidget)
        self.usr_horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.usr_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.usr_horizontalLayout.setSpacing(15)
        self.usr_horizontalLayout.setObjectName("usr_horizontalLayout")
        
        #region button menu
        self.usr_pushButton_6 = QtWidgets.QPushButton(self.usr_horizontalLayoutWidget)
        self.usr_pushButton_6.setObjectName("usr_pushButton_6")
        self.usr_pushButton_6.setStyleSheet(self.buttonStyle())
        self.usr_pushButton_6.clicked.connect(lambda: self.usr_change_recipe(1))
        self.usr_horizontalLayout.addWidget(self.usr_pushButton_6)
        self.usr_pushButton_7 = QtWidgets.QPushButton(self.usr_horizontalLayoutWidget)
        self.usr_pushButton_7.setObjectName("usr_pushButton_7")
        self.usr_pushButton_7.setStyleSheet(self.buttonStyle())
        self.usr_pushButton_7.clicked.connect(lambda: self.usr_change_recipe(2))
        self.usr_horizontalLayout.addWidget(self.usr_pushButton_7)
        self.usr_pushButton_8 = QtWidgets.QPushButton(self.usr_horizontalLayoutWidget)
        self.usr_pushButton_8.setObjectName("usr_pushButton_8")
        self.usr_pushButton_8.setStyleSheet(self.buttonStyle())
        self.usr_pushButton_8.clicked.connect(lambda: self.usr_change_recipe(3))
        self.usr_horizontalLayout.addWidget(self.usr_pushButton_8)
        self.usr_pushButton_9 = QtWidgets.QPushButton(self.usr_horizontalLayoutWidget)
        self.usr_pushButton_9.setObjectName("usr_pushButton_9")
        self.usr_pushButton_9.setStyleSheet(self.buttonStyle())
        self.usr_pushButton_9.clicked.connect(lambda: self.usr_change_recipe(4))
        self.usr_horizontalLayout.addWidget(self.usr_pushButton_9)
        self.usr_pushButton_10 = QtWidgets.QPushButton(self.usr_horizontalLayoutWidget)
        self.usr_pushButton_10.setObjectName("usr_pushButton_10")
        self.usr_pushButton_10.setStyleSheet(self.buttonStyle())
        self.usr_pushButton_10.clicked.connect(lambda: self.usr_change_recipe(5))
        self.usr_horizontalLayout.addWidget(self.usr_pushButton_10)
        self.usr_pushButton_11 = QtWidgets.QPushButton(self.usr_horizontalLayoutWidget)
        self.usr_pushButton_11.setObjectName("usr_pushButton_11")
        self.usr_pushButton_11.setStyleSheet(self.buttonStyle())
        self.usr_pushButton_11.clicked.connect(lambda: self.usr_change_recipe(6))
        self.usr_horizontalLayout.addWidget(self.usr_pushButton_11)
        self.usr_pushButton_12 = QtWidgets.QPushButton(self.usr_horizontalLayoutWidget)
        self.usr_pushButton_12.setObjectName("usr_pushButton_12")
        self.usr_pushButton_12.setStyleSheet(self.buttonStyle())
        self.usr_pushButton_12.clicked.connect(lambda: self.usr_change_recipe(7))
        self.usr_horizontalLayout.addWidget(self.usr_pushButton_12)
        self.usr_pushButton_13 = QtWidgets.QPushButton(self.usr_horizontalLayoutWidget)
        self.usr_pushButton_13.setObjectName("usr_pushButton_13")
        self.usr_pushButton_13.setStyleSheet(self.buttonStyle())
        self.usr_pushButton_13.clicked.connect(lambda: self.usr_change_recipe(8))
        self.usr_horizontalLayout.addWidget(self.usr_pushButton_13)
        self.usr_pushButton_14 = QtWidgets.QPushButton(self.usr_horizontalLayoutWidget)
        self.usr_pushButton_14.setObjectName("usr_pushButton_14")
        self.usr_pushButton_14.setStyleSheet(self.buttonStyle())
        self.usr_pushButton_14.clicked.connect(lambda: self.usr_change_recipe(9))
        self.usr_horizontalLayout.addWidget(self.usr_pushButton_14)
        self.usr_pushButton_15 = QtWidgets.QPushButton(self.usr_horizontalLayoutWidget)
        self.usr_pushButton_15.setObjectName("usr_pushButton_15")
        self.usr_pushButton_15.setStyleSheet(self.buttonStyle())
        self.usr_pushButton_15.clicked.connect(lambda: self.usr_change_recipe(10))
        self.usr_horizontalLayout.addWidget(self.usr_pushButton_15)
        #endregion button menu
        
        self.usr_label_2 = QtWidgets.QLabel(self.form)
        self.usr_label_2.setGeometry(QtCore.QRect(10, 110, 150, 30))
        self.usr_label_2.setObjectName("usr_label_2")
        self.usr_label_2.setStyleSheet("border-top-left-radius: 5px;"
                                   "border-top-right-radius: 20px;"
                                   "border: 1px solid black;")

        self.usr_label_3 = QtWidgets.QLabel(self.form)
        self.usr_label_3.setGeometry(QtCore.QRect(10, 140, 150, 130))
        self.usr_label_3.setObjectName("usr_label_3")
        self.usr_label_3.setStyleSheet("border-bottom-left-radius: 20px;"
                                   "border-bottom-right-radius: 5px;"
                                   "border: 1px solid black;")

        self.usr_label_4 = QtWidgets.QLabel(self.form)
        self.usr_label_4.setGeometry(QtCore.QRect(641, 110, 150, 30))
        self.usr_label_4.setObjectName("usr_label_4")
        self.usr_label_4.setStyleSheet("border-top-left-radius: 5px;"
                                   "border-top-right-radius: 20px;"
                                   "border: 1px solid black;")

        self.usr_label_5 = QtWidgets.QLabel(self.form)
        self.usr_label_5.setGeometry(QtCore.QRect(641, 140, 150, 130))
        self.usr_label_5.setObjectName("usr_label_5")
        self.usr_label_5.setStyleSheet("border-bottom-left-radius: 20px;"
                                   "border-bottom-right-radius: 5px;"
                                   "border: 1px solid black;")

        self.usr_pushButton_3 = QtWidgets.QPushButton(self.form)
        self.usr_pushButton_3.setGeometry(QtCore.QRect(720, 310, 65, 65))
        self.usr_pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-image: url(:/check/assets/check2.png);\n"
        "border-radius:30px\n"
        "")
        self.usr_pushButton_3.setText("")
        self.usr_pushButton_3.setObjectName("usr_pushButton_3")
        self.usr_pushButton_3.setIcon(QIcon('assets/check2.png'))
        self.usr_pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.usr_pushButton_3.setStyleSheet("border-radius:30px\noverflow:hidden;")
        
        self.usr_pushButton_4 = QtWidgets.QPushButton(self.form)
        self.usr_pushButton_4.setGeometry(QtCore.QRect(165, 90, 30, 230))
        self.usr_pushButton_4.setObjectName("usr_pushButton_4")
        self.usr_pushButton_4.setStyleSheet(self.buttonNavStyle())
        self.usr_pushButton_4.clicked.connect(lambda: self.usr_change_recipe("-"))
        
        self.usr_pushButton_5 = QtWidgets.QPushButton(self.form)
        self.usr_pushButton_5.setGeometry(QtCore.QRect(605, 90, 30, 230))
        self.usr_pushButton_5.setObjectName("usr_pushButton_5")
        self.usr_pushButton_5.setStyleSheet(self.buttonNavStyle())
        self.usr_pushButton_5.clicked.connect(lambda: self.usr_change_recipe("+"))
        
        
        self.usr_label_6 = QtWidgets.QLabel(self.form)
        self.usr_label_6.setGeometry(QtCore.QRect(195, 290, 205, 30))
        self.usr_label_6.setStyleSheet("background-color: rgba(0,0,0,0.5);"
                                   "color: #fff;"
                                   "padding-left: 15px;"
                                   "border-top-right-radius: 20px;")
        self.usr_label_6.setObjectName("usr_label_6")
        self.usr_pushButton_16 = QtWidgets.QPushButton(self.form)
        self.usr_pushButton_16.setGeometry(QtCore.QRect(195, 90, 410, 230))
        self.usr_pushButton_16.setObjectName("usr_pushButton_16")
        self.usr_pushButton_16.raise_()
        self.usr_label.raise_()
        self.usr_pushButton.raise_()
        self.usr_pushButton_2.raise_()
        self.usr_horizontalLayoutWidget.raise_()
        self.usr_label_2.raise_()
        self.usr_label_3.raise_()
        self.usr_label_4.raise_()
        self.usr_label_5.raise_()
        self.usr_pushButton_3.raise_()
        self.usr_pushButton_4.raise_()
        self.usr_pushButton_5.raise_()
        self.usr_label_6.raise_()

        self.usr_retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.form)

    def usr_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle(_translate("self.form", "Mixology"))
        self.usr_label.setText(_translate("self.form", "    MIXOLOGY"))
        self.usr_pushButton_6.setText(_translate("self.form", "1"))
        self.usr_pushButton_6.setVisible(len(self.dat.df.ID)>0)
        self.usr_pushButton_7.setText(_translate("self.form", "2"))
        self.usr_pushButton_7.setVisible(len(self.dat.df.ID)>1)
        self.usr_pushButton_8.setText(_translate("self.form", "3"))
        self.usr_pushButton_8.setVisible(len(self.dat.df.ID)>2)
        self.usr_pushButton_9.setText(_translate("self.form", "4"))
        self.usr_pushButton_9.setVisible(len(self.dat.df.ID)>3)
        self.usr_pushButton_10.setText(_translate("self.form", "5"))
        self.usr_pushButton_10.setVisible(len(self.dat.df.ID)>4)
        self.usr_pushButton_11.setText(_translate("self.form", "6"))
        self.usr_pushButton_11.setVisible(len(self.dat.df.ID)>5)
        self.usr_pushButton_12.setText(_translate("self.form", "7"))
        self.usr_pushButton_12.setVisible(len(self.dat.df.ID)>6)
        self.usr_pushButton_13.setText(_translate("self.form", "8"))
        self.usr_pushButton_13.setVisible(len(self.dat.df.ID)>7)
        self.usr_pushButton_14.setText(_translate("self.form", "9"))
        self.usr_pushButton_14.setVisible(len(self.dat.df.ID)>8)
        self.usr_pushButton_15.setText(_translate("self.form", "10"))
        self.usr_pushButton_15.setVisible(len(self.dat.df.ID)>9)
        self.usr_label_2.setText(_translate("self.form", "Líquidos"))
        self.usr_label_3.setText("-"+"\n-".join(self.dat.df.Ingredients[self.user_screen-1].split(',')))
        self.usr_label_4.setText(_translate("self.form", "Sólidos"))
        self.usr_label_5.setText("-"+"\n-".join(self.dat.df.Boxes[self.user_screen-1].split(',')))
        self.usr_pushButton_4.setText("<" if self.user_screen>1 else "")
        self.usr_pushButton_4.setEnabled(self.user_screen>1)
        self.usr_pushButton_5.setText(">" if self.user_screen<len(self.dat.df.ID) else "")
        self.usr_pushButton_5.setEnabled(self.user_screen<len(self.dat.df.ID))
        self.usr_label_6.setText(self.dat.df.Name[self.user_screen-1])
        if self.dat.df.Name[self.user_screen-1]+'.jpg' in [x.replace("images/","") for x in glob("images/*")]:
            self.usr_pushButton_16.setIcon(QIcon('images/'+self.dat.df.Name[self.user_screen-1]+'.jpg'))
        else:
            self.usr_pushButton_16.setIcon(QIcon('images/Logo.jpg'))
        self.usr_pushButton_16.setIconSize(QtCore.QSize(400, 220))
        self.usr_pushButton_16.setStyleSheet(self.ButtonImageStyle())

    def usr_change_recipe(self, sign):
        if sign == "+":
            self.user_screen +=1
        elif sign == "-":
            self.user_screen -=1
        else:
            self.user_screen = sign
        self.usr_retranslateUi()
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())

