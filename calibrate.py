# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/Calibrate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from apis.data import Data
from PyQt5.QtWidgets import QSlider

class Ui_Form(object):
    def calibrate(self, Form):
        self.dat = Data()
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(800, 380)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
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
        self.label_2 = QtWidgets.QLabel(Form)
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
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 300, 65, 65))
        self.pushButton_10.setStyleSheet("\n"
"border-image: url(:/back/assets/back.png);\n"
"border-radius:30px")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(720, 300, 65, 65))
        self.pushButton_11.setStyleSheet("\n"
"border-image: url(:/check/assets/check2.png);\n"
"border-radius:30px\n"
"")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        
        #region Scroll 1
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(30, 80, 550, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 534, 472))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setText(self.dat.bottles["1"][0])
        self.gridLayout.addWidget(self.lineEdit_12, 0, 2, 1, 1)

        
        self.lineEdit_15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.setText(self.dat.bottles["2"][0])
        self.gridLayout.addWidget(self.lineEdit_15, 1, 2, 1, 1)

        
        self.horizontalSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 0, 3, 1, 1)

        self.lineEdit_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setText(self.dat.bottles["3"][0])
        self.gridLayout.addWidget(self.lineEdit_10, 2, 2, 1, 1)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())

        self.horizontalSlider_2 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_2.setSizePolicy(sizePolicy)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout.addWidget(self.horizontalSlider_2, 1, 3, 1, 1)

        self.horizontalSlider_3 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout.addWidget(self.horizontalSlider_3, 2, 3, 1, 1)

        self.horizontalSlider_4 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout.addWidget(self.horizontalSlider_4, 3, 3, 1, 1)

        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setMinimumSize(QtCore.QSize(0, 40))
        self.label_22.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_22.setText("Item---1")
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 4, 1, 1)

        self.horizontalSlider_5 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.gridLayout.addWidget(self.horizontalSlider_5, 4, 3, 1, 1)

        self.lineEdit_13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setText(self.dat.bottles["4"][0])
        self.gridLayout.addWidget(self.lineEdit_13, 3, 2, 1, 1)
        
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setMinimumSize(QtCore.QSize(0, 40))
        self.label_26.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_26.setText("Item---2")
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 4, 1, 1)

        self.horizontalSlider_6 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.gridLayout.addWidget(self.horizontalSlider_6, 5, 3, 1, 1)

        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(0, 40))
        self.label_18.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_18.setText("Item---3")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 4, 1, 1)

        self.lineEdit_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setText(self.dat.bottles["5"][0])
        self.gridLayout.addWidget(self.lineEdit_11, 4, 2, 1, 1)

        
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setMinimumSize(QtCore.QSize(0, 40))
        self.label_19.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_19.setText("Item---4")
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 4, 1, 1)

        self.lineEdit_14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setText(self.dat.bottles["6"][0])
        self.gridLayout.addWidget(self.lineEdit_14, 5, 2, 1, 1)

        
        self.horizontalSlider_7 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.gridLayout.addWidget(self.horizontalSlider_7, 6, 3, 1, 1)

        self.horizontalSlider_8 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.gridLayout.addWidget(self.horizontalSlider_8, 7, 3, 1, 1)

        self.horizontalSlider_9 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_9.setObjectName("horizontalSlider_9")
        self.gridLayout.addWidget(self.horizontalSlider_9, 8, 3, 1, 1)

        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setMinimumSize(QtCore.QSize(0, 40))
        self.label_21.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_21.setText("Item---5")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 4, 4, 1, 1)

        self.lineEdit_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setText(self.dat.bottles["7"][0])
        self.gridLayout.addWidget(self.lineEdit_9, 6, 2, 1, 1)

        
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setMinimumSize(QtCore.QSize(0, 40))
        self.label_20.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_20.setText("Item---6")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 5, 4, 1, 1)

        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setMinimumSize(QtCore.QSize(0, 40))
        self.label_24.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_24.setText("Item---7")
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 6, 4, 1, 1)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(30, 40))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setText(self.dat.bottles["8"][0])
        self.gridLayout.addWidget(self.lineEdit_7, 7, 2, 1, 1)

        
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setMinimumSize(QtCore.QSize(0, 40))
        self.label_23.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_23.setText("Item---8")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 7, 4, 1, 1)

        self.lineEdit_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setText(self.dat.bottles["9"][0])
        self.gridLayout.addWidget(self.lineEdit_8, 8, 2, 1, 1)

        
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setMinimumSize(QtCore.QSize(0, 40))
        self.label_25.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_25.setText("Item---9")
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 8, 4, 1, 1)

        self.lineEdit_16 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_16.setText(self.dat.bottles["10"][0])
        self.gridLayout.addWidget(self.lineEdit_16, 9, 2, 1, 1)

        
        self.horizontalSlider_10 = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_10.setObjectName("horizontalSlider_10")
        self.gridLayout.addWidget(self.horizontalSlider_10, 9, 3, 1, 1)

        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setMinimumSize(QtCore.QSize(0, 40))
        self.label_27.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_27.setText("Item---10")
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 9, 4, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #endregion Scroll 1
        
        #region Slider formatter
        self.horizontalSlider.setMaximum(3000)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.valueChanged.connect(self.cal_update_val)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(100)


        self.horizontalSlider_2.setMaximum(3000)
        self.horizontalSlider_2.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_2.valueChanged.connect(self.cal_update_val)
        self.horizontalSlider_2.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_2.setTickInterval(100)


        self.horizontalSlider_3.setMaximum(3000)
        self.horizontalSlider_3.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_3.valueChanged.connect(self.cal_update_val)
        self.horizontalSlider_3.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_3.setTickInterval(100)


        self.horizontalSlider_4.setMaximum(3000)
        self.horizontalSlider_4.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_4.valueChanged.connect(self.cal_update_val)
        self.horizontalSlider_4.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_4.setTickInterval(100)


        self.horizontalSlider_5.setMaximum(3000)
        self.horizontalSlider_5.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_5.valueChanged.connect(self.cal_update_val)
        self.horizontalSlider_5.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_5.setTickInterval(100)


        self.horizontalSlider_6.setMaximum(3000)
        self.horizontalSlider_6.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_6.valueChanged.connect(self.cal_update_val)
        self.horizontalSlider_6.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_6.setTickInterval(100)


        self.horizontalSlider_7.setMaximum(3000)
        self.horizontalSlider_7.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_7.valueChanged.connect(self.cal_update_val)
        self.horizontalSlider_7.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_7.setTickInterval(100)


        self.horizontalSlider_8.setMaximum(3000)
        self.horizontalSlider_8.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_8.valueChanged.connect(self.cal_update_val)
        self.horizontalSlider_8.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_8.setTickInterval(100)


        self.horizontalSlider_9.setMaximum(3000)
        self.horizontalSlider_9.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_9.valueChanged.connect(self.cal_update_val)
        self.horizontalSlider_9.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_9.setTickInterval(100)


        self.horizontalSlider_10.setMaximum(3000)
        self.horizontalSlider_10.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_10.valueChanged.connect(self.cal_update_val)
        self.horizontalSlider_10.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_10.setTickInterval(100)
        #endregion Slider formatter

        #region Scroll 2
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(600, 80, 162, 200))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 146, 336))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(self.dat.boxes['1'])

        self.verticalLayout.addWidget(self.lineEdit)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(self.dat.boxes['2'])
        
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(self.dat.boxes['3'])
        
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText(self.dat.boxes['4'])
        
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText(self.dat.boxes['5'])
        
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText(self.dat.boxes['6'])
        
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_2.raise_()
        self.pushButton_7.raise_()
        self.pushButton_11.raise_()
        self.pushButton_10.raise_()
        self.scrollArea.raise_()
        self.scrollArea_2.raise_()
        #endregion Scroll 2

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def cal_update_val(self):
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

        self.label_22.setText(str(self.horizontalSlider.value()))
        self.label_26.setText(str(self.horizontalSlider_2.value()))
        self.label_18.setText(str(self.horizontalSlider_3.value()))
        self.label_19.setText(str(self.horizontalSlider_4.value()))
        self.label_21.setText(str(self.horizontalSlider_5.value()))
        self.label_20.setText(str(self.horizontalSlider_6.value()))
        self.label_24.setText(str(self.horizontalSlider_7.value()))
        self.label_23.setText(str(self.horizontalSlider_8.value()))
        self.label_25.setText(str(self.horizontalSlider_9.value()))
        self.label_27.setText(str(self.horizontalSlider_10.value()))
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_7.setText(_translate("Form", "X"))
        self.label_2.setText(_translate("Form", "    CALIBRATE"))
        self.label_12.setText(_translate("Form", "Box 1"))
        self.label_13.setText(_translate("Form", "Box 2"))
        self.label_14.setText(_translate("Form", "Box 3"))
        self.label_15.setText(_translate("Form", "Box 4"))
        self.label_16.setText(_translate("Form", "Box 5"))
        self.label_17.setText(_translate("Form", "Box 6"))
        self.label_22.setText(str(self.dat.bottles["1"][1]))
        self.label_26.setText(str(self.dat.bottles["2"][1]))
        self.label_18.setText(str(self.dat.bottles["3"][1]))
        self.label_19.setText(str(self.dat.bottles["4"][1]))
        self.label_21.setText(str(self.dat.bottles["5"][1]))
        self.label_20.setText(str(self.dat.bottles["6"][1]))
        self.label_24.setText(str(self.dat.bottles["7"][1]))
        self.label_23.setText(str(self.dat.bottles["8"][1]))
        self.label_25.setText(str(self.dat.bottles["9"][1]))
        self.label_27.setText(str(self.dat.bottles["10"][1]))
        self.horizontalSlider.setValue(self.dat.bottles["1"][1])
        self.horizontalSlider_2.setValue(self.dat.bottles["2"][1])
        self.horizontalSlider_3.setValue(self.dat.bottles["3"][1])
        self.horizontalSlider_4.setValue(self.dat.bottles["4"][1])
        self.horizontalSlider_5.setValue(self.dat.bottles["5"][1])
        self.horizontalSlider_6.setValue(self.dat.bottles["6"][1])
        self.horizontalSlider_7.setValue(self.dat.bottles["7"][1])
        self.horizontalSlider_8.setValue(self.dat.bottles["8"][1])
        self.horizontalSlider_9.setValue(self.dat.bottles["9"][1])
        self.horizontalSlider_10.setValue(self.dat.bottles["10"][1])
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.calibrate(Form)
    Form.show()
    sys.exit(app.exec_())

