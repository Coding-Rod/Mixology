# -*- coding: utf-8 -*-

# self.form implementation generated from reading ui file 'uis/scroll_test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
# TODO: Index
# TODO: Change labels

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QMessageBox
from apis.data import Data

class Ui_Form(object):
    def __init__(self, Form):
        self.dat = Data()
        self.form = Form
    def create(self):
        self.form.setObjectName("Form")
        self.form.resize(800, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form.sizePolicy().hasHeightForWidth())
        self.form.setSizePolicy(sizePolicy)
        self.form.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.label_2 = QtWidgets.QLabel(self.form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 74))
        self.label_2.setStyleSheet("font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 36px;\n"
"line-height: 42px;\n"
"\n"
"color: #FFFFFF;\n"
"background-color: #E09825;")
        self.label_2.setObjectName("label_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.form)
        self.pushButton_7.setGeometry(QtCore.QRect(730, 20, 41, 31))
        self.pushButton_7.setStyleSheet("background: #AA0000;\n"
"border: 0.5px solid rgba(255, 255, 255, 0.48);\n"
"border-radius: 10px;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"\n"
"color: #FFFFFF;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: sys.exit(0))
        self.label_12 = QtWidgets.QLabel(self.form)
        self.label_12.setGeometry(QtCore.QRect(320, 330, 67, 17))
        self.label_12.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.form)
        self.pushButton.setGeometry(QtCore.QRect(10, 310, 65, 65))
        self.pushButton.setStyleSheet("border-image: url(:/back/assets/back.png);\n"
"border-radius:30px\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QIcon('assets/back.png'))
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.pushButton_2 = QtWidgets.QPushButton(self.form)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 310, 65, 65))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-image: url(:/check/assets/check2.png);\n"
"border-radius:30px\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QIcon('assets/check2.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.pushButton_2.clicked.connect(self.save)
        self.lineEdit = QtWidgets.QLineEdit(self.form)
        self.lineEdit.setGeometry(QtCore.QRect(360, 30, 170, 25))
        self.lineEdit.setStyleSheet("border-radius: 10px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.form)
        self.textEdit.setGeometry(QtCore.QRect(300, 30, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: #E09825;\n"
"color: #FFFFFF;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setLineWidth(1)
        self.textEdit.setObjectName("textEdit")
        self.horizontalSlider_11 = QtWidgets.QSlider(self.form)
        self.horizontalSlider_11.setGeometry(QtCore.QRect(400, 330, 80, 16))
        self.horizontalSlider_11.setMaximum(1)
        self.horizontalSlider_11.setSliderPosition(0)
        self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_11.setObjectName("horizontalSlider_11")
        self.scrollArea = QtWidgets.QScrollArea(self.form)
        self.scrollArea.setGeometry(QtCore.QRect(30, 110, 350, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 334, 442))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)

        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_2)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_3.setSizePolicy(sizePolicy)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_3)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_4.setSizePolicy(sizePolicy)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_4)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_5.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_5.setSizePolicy(sizePolicy)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_5)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_6.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_6.setSizePolicy(sizePolicy)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_6)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.horizontalSlider_7 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_7.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_7.setSizePolicy(sizePolicy)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_7)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.horizontalSlider_8 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_8.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_8.setSizePolicy(sizePolicy)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_8)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalSlider_9 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_9.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_9.setSizePolicy(sizePolicy)
        self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_9.setObjectName("horizontalSlider_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_9)
        self.horizontalSlider_10 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_10.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_10.setSizePolicy(sizePolicy)
        self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_10.setObjectName("horizontalSlider_10")
        self.horizontalSlider_10.setValue(0)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_10)

        #region Slider formatter

        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.valueChanged.connect(self.update_val)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(100)


        self.horizontalSlider_2.setMaximum(1000)
        self.horizontalSlider_2.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_2.valueChanged.connect(self.update_val)
        self.horizontalSlider_2.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_2.setTickInterval(100)


        self.horizontalSlider_3.setMaximum(1000)
        self.horizontalSlider_3.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_3.valueChanged.connect(self.update_val)
        self.horizontalSlider_3.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_3.setTickInterval(100)


        self.horizontalSlider_4.setMaximum(1000)
        self.horizontalSlider_4.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_4.valueChanged.connect(self.update_val)
        self.horizontalSlider_4.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_4.setTickInterval(100)


        self.horizontalSlider_5.setMaximum(1000)
        self.horizontalSlider_5.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_5.valueChanged.connect(self.update_val)
        self.horizontalSlider_5.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_5.setTickInterval(100)


        self.horizontalSlider_6.setMaximum(1000)
        self.horizontalSlider_6.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_6.valueChanged.connect(self.update_val)
        self.horizontalSlider_6.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_6.setTickInterval(100)


        self.horizontalSlider_7.setMaximum(1000)
        self.horizontalSlider_7.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_7.valueChanged.connect(self.update_val)
        self.horizontalSlider_7.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_7.setTickInterval(100)


        self.horizontalSlider_8.setMaximum(1000)
        self.horizontalSlider_8.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_8.valueChanged.connect(self.update_val)
        self.horizontalSlider_8.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_8.setTickInterval(100)


        self.horizontalSlider_9.setMaximum(1000)
        self.horizontalSlider_9.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_9.valueChanged.connect(self.update_val)
        self.horizontalSlider_9.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_9.setTickInterval(100)


        self.horizontalSlider_10.setMaximum(1000)
        self.horizontalSlider_10.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_10.valueChanged.connect(self.update_val)
        self.horizontalSlider_10.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_10.setTickInterval(100)
        #endregion Slider formatter

        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_9)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.form)
        self.scrollArea_2.setGeometry(QtCore.QRect(390, 110, 350, 200))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 348, 198))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_2.raise_()
        self.scrollArea.raise_()
        self.label_2.raise_()
        self.pushButton_7.raise_()
        self.label_12.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.textEdit.raise_()
        self.lineEdit.raise_()
        self.horizontalSlider_11.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle(_translate("self.form", "self.form"))
        self.label_2.setText(_translate("self.form", "    CREATE"))
        self.pushButton_7.setText(_translate("self.form", "X"))
        self.label_12.setText(_translate("self.form", "MIX"))
        self.textEdit.setHtml(_translate("self.form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Name</span></p></body></html>"))
        self.label.setText(_translate("self.form", self.dat.bottles['1'][0])+("\t\t"if len(self.dat.bottles['1'][0])<7 else "\t")+"\n"+str(self.horizontalSlider.value())+" ml")
        self.label_3.setText(_translate("self.form", self.dat.bottles['2'][0])+("\t\t"if len(self.dat.bottles['2'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_2.value())+" ml")
        self.label_4.setText(_translate("self.form", self.dat.bottles['3'][0])+("\t\t"if len(self.dat.bottles['3'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_3.value())+" ml")
        self.label_5.setText(_translate("self.form", self.dat.bottles['4'][0])+("\t\t"if len(self.dat.bottles['4'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_4.value())+" ml")
        self.label_6.setText(_translate("self.form", self.dat.bottles['5'][0])+("\t\t"if len(self.dat.bottles['5'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_5.value())+" ml")
        self.label_7.setText(_translate("self.form", self.dat.bottles['6'][0])+("\t\t"if len(self.dat.bottles['6'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_6.value())+" ml")
        self.label_8.setText(_translate("self.form", self.dat.bottles['7'][0])+("\t\t"if len(self.dat.bottles['7'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_7.value())+" ml")
        self.label_9.setText(_translate("self.form", self.dat.bottles['8'][0])+("\t\t"if len(self.dat.bottles['8'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_8.value())+" ml")
        self.label_10.setText(_translate("self.form", self.dat.bottles['9'][0])+("\t\t"if len(self.dat.bottles['9'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_9.value())+" ml")
        self.label_11.setText(_translate("self.form", self.dat.bottles['10'][0])+("\t\t"if len(self.dat.bottles['10'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_10.value())+" ml")
        self.checkBox.setText(_translate("self.form", self.dat.boxes["1"]))
        self.checkBox_2.setText(_translate("self.form", self.dat.boxes["2"]))
        self.checkBox_3.setText(_translate("self.form", self.dat.boxes["3"]))
        self.checkBox_4.setText(_translate("self.form", self.dat.boxes["4"]))
        self.checkBox_5.setText(_translate("self.form", self.dat.boxes["5"]))
        self.checkBox_6.setText(_translate("self.form", self.dat.boxes["6"]))
    
    def update_val(self):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle("Mixology")                
        self.horizontalSlider.setValue(int(self.horizontalSlider.value()/100)*100)
        self.horizontalSlider_2.setValue(int(self.horizontalSlider_2.value()/100)*100)
        self.horizontalSlider_3.setValue(int(self.horizontalSlider_3.value()/100)*100)
        self.horizontalSlider_4.setValue(int(self.horizontalSlider_4.value()/100)*100)
        self.horizontalSlider_5.setValue(int(self.horizontalSlider_5.value()/100)*100)
        self.horizontalSlider_6.setValue(int(self.horizontalSlider_6.value()/100)*100)
        self.horizontalSlider_7.setValue(int(self.horizontalSlider_7.value()/100)*100)
        self.horizontalSlider_8.setValue(int(self.horizontalSlider_8.value()/100)*100)
        self.horizontalSlider_9.setValue(int(self.horizontalSlider_9.value()/100)*100)
        self.horizontalSlider_10.setValue(int(self.horizontalSlider_10.value()/100)*100)
        self.lineEdit.setText("")
        self.label.setText(_translate("self.form", self.dat.bottles['1'][0])+("\t\t"if len(self.dat.bottles['1'][0])<7 else "\t")+"\n"+str(self.horizontalSlider.value())+" ml")
        self.label_3.setText(_translate("self.form", self.dat.bottles['2'][0])+("\t\t"if len(self.dat.bottles['2'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_2.value())+" ml")
        self.label_4.setText(_translate("self.form", self.dat.bottles['3'][0])+("\t\t"if len(self.dat.bottles['3'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_3.value())+" ml")
        self.label_5.setText(_translate("self.form", self.dat.bottles['4'][0])+("\t\t"if len(self.dat.bottles['4'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_4.value())+" ml")
        self.label_6.setText(_translate("self.form", self.dat.bottles['5'][0])+("\t\t"if len(self.dat.bottles['5'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_5.value())+" ml")
        self.label_7.setText(_translate("self.form", self.dat.bottles['6'][0])+("\t\t"if len(self.dat.bottles['6'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_6.value())+" ml")
        self.label_8.setText(_translate("self.form", self.dat.bottles['7'][0])+("\t\t"if len(self.dat.bottles['7'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_7.value())+" ml")
        self.label_9.setText(_translate("self.form", self.dat.bottles['8'][0])+("\t\t"if len(self.dat.bottles['8'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_8.value())+" ml")
        self.label_10.setText(_translate("self.form", self.dat.bottles['9'][0])+("\t\t"if len(self.dat.bottles['9'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_9.value())+" ml")
        self.label_11.setText(_translate("self.form", self.dat.bottles['10'][0])+("\t\t"if len(self.dat.bottles['10'][0])<7 else "\t")+"\n"+str(self.horizontalSlider_10.value())+" ml")


    def save(self):
        name = (self.lineEdit.text())
        ingredients = ((
              (str(self.dat.bottles['1'][0])+"," if self.horizontalSlider.value() > 0 else "")+
              (str(self.dat.bottles['2'][0])+"," if self.horizontalSlider_2.value() > 0 else "")+
              (str(self.dat.bottles['3'][0])+"," if self.horizontalSlider_3.value() > 0 else "")+
              (str(self.dat.bottles['4'][0])+"," if self.horizontalSlider_4.value() > 0 else "")+
              (str(self.dat.bottles['5'][0])+"," if self.horizontalSlider_5.value() > 0 else "")+
              (str(self.dat.bottles['6'][0])+"," if self.horizontalSlider_6.value() > 0 else "")+
              (str(self.dat.bottles['7'][0])+"," if self.horizontalSlider_7.value() > 0 else "")+
              (str(self.dat.bottles['8'][0])+"," if self.horizontalSlider_8.value() > 0 else "")+
              (str(self.dat.bottles['9'][0])+"," if self.horizontalSlider_9.value() > 0 else "")+
              (str(self.dat.bottles['10'][0])+"," if self.horizontalSlider_10.value() > 0 else "")
        )[:-1])
        volume = ((
              (str(self.horizontalSlider.value())+"," if self.horizontalSlider.value() > 0 else "")+
              (str(self.horizontalSlider_2.value())+"," if self.horizontalSlider_2.value() > 0 else "")+
              (str(self.horizontalSlider_3.value())+"," if self.horizontalSlider_3.value() > 0 else "")+
              (str(self.horizontalSlider_4.value())+"," if self.horizontalSlider_4.value() > 0 else "")+
              (str(self.horizontalSlider_5.value())+"," if self.horizontalSlider_5.value() > 0 else "")+
              (str(self.horizontalSlider_6.value())+"," if self.horizontalSlider_6.value() > 0 else "")+
              (str(self.horizontalSlider_7.value())+"," if self.horizontalSlider_7.value() > 0 else "")+
              (str(self.horizontalSlider_8.value())+"," if self.horizontalSlider_8.value() > 0 else "")+
              (str(self.horizontalSlider_9.value())+"," if self.horizontalSlider_9.value() > 0 else "")+
              (str(self.horizontalSlider_10.value())+"," if self.horizontalSlider_10.value() > 0 else "")
        )[:-1])
        boxes = ((
              (str(self.dat.boxes['1'])+"," if self.checkBox.isChecked() else "")+
              (str(self.dat.boxes['2'])+"," if self.checkBox_2.isChecked() else "")+
              (str(self.dat.boxes['3'])+"," if self.checkBox_3.isChecked() else "")+
              (str(self.dat.boxes['4'])+"," if self.checkBox_4.isChecked() else "")+
              (str(self.dat.boxes['5'])+"," if self.checkBox_5.isChecked() else "")+
              (str(self.dat.boxes['6'])+"," if self.checkBox_6.isChecked() else "")
        )[:-1])
        mix = ([False, True][self.horizontalSlider_11.value()])
        self.dat.add_recipe(name,ingredients,volume,boxes,mix)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Your recipe is saved")
        # msg.setInformativeText('More information')
        msg.setWindowTitle("Saved")
        msg.exec_()
        self.label.setText(self.dat.bottles['1'][0]+("\t\t"if len(self.dat.bottles['1'][0])<7 else "\t")+"\n"+"0 ml")
        self.label_3.setText(self.dat.bottles['2'][0]+("\t\t"if len(self.dat.bottles['2'][0])<7 else "\t")+"\n"+"0 ml")
        self.label_4.setText(self.dat.bottles['3'][0]+("\t\t"if len(self.dat.bottles['3'][0])<7 else "\t")+"\n"+"0 ml")
        self.label_5.setText(self.dat.bottles['10'][0]+("\t\t"if len(self.dat.bottles['4'][0])<7 else "\t")+"\n"+"0 ml")
        self.label_6.setText(self.dat.bottles['4'][0]+("\t\t"if len(self.dat.bottles['5'][0])<7 else "\t")+"\n"+"0 ml")
        self.label_7.setText(self.dat.bottles['5'][0]+("\t\t"if len(self.dat.bottles['6'][0])<7 else "\t")+"\n"+"0 ml")
        self.label_8.setText(self.dat.bottles['6'][0]+("\t\t"if len(self.dat.bottles['7'][0])<7 else "\t")+"\n"+"0 ml")
        self.label_9.setText(self.dat.bottles['7'][0]+("\t\t"if len(self.dat.bottles['8'][0])<7 else "\t")+"\n"+"0 ml")
        self.label_11.setText(self.dat.bottles['8'][0]+("\t\t"if len(self.dat.bottles['9'][0])<7 else "\t")+"\n"+"0 ml")
        self.label_10.setText(self.dat.bottles['9'][0]+("\t\t"if len(self.dat.bottles['10'][0])<7 else "\t")+"\n"+"0 ml")
        self.horizontalSlider.setValue(0)
        self.horizontalSlider_2.setValue(0)
        self.horizontalSlider_3.setValue(0)
        self.horizontalSlider_4.setValue(0)
        self.horizontalSlider_5.setValue(0)
        self.horizontalSlider_6.setValue(0)
        self.horizontalSlider_7.setValue(0)
        self.horizontalSlider_8.setValue(0)
        self.horizontalSlider_9.setValue(0)
        self.horizontalSlider_10.setValue(0)
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    ui.create()
    Form.show()
    sys.exit(app.exec_())

