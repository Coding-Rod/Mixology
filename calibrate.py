# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/Calibrate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from apis.data import Data
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def __init__(self,Form):
        self.dat = Data()
        self.form = Form

    def calibrate_form(self):
        self.form.setObjectName("cal_form")
        self.form.resize(800, 380)
        self.cal_pushButton_7 = QtWidgets.QPushButton(self.form)
        self.cal_pushButton_7.setGeometry(QtCore.QRect(730, 20, 41, 31))
        self.cal_pushButton_7.setStyleSheet("background: #AA0000;\n"
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
        self.cal_pushButton_7.setObjectName("cal_pushButton_7")
        self.cal_pushButton_7.clicked.connect(lambda: sys.exit(0))
        self.cal_label_2 = QtWidgets.QLabel(self.form)
        self.cal_label_2.setGeometry(QtCore.QRect(0, 0, 800, 74))
        self.cal_label_2.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: bold;\n"
        "font-size: 36px;\n"
        "line-height: 42px;\n"
        "\n"
        "color: #FFFFFF;\n"
        "background-color: #E09825;")
        self.cal_label_2.setObjectName("cal_label_2")
        self.cal_pushButton_10 = QtWidgets.QPushButton(self.form)
        self.cal_pushButton_10.setGeometry(QtCore.QRect(10, 300, 65, 65))
        self.cal_pushButton_10.setStyleSheet("\n"
        "border-image: url(:/back/assets/back.png);\n"
        "border-radius:30px")
        self.cal_pushButton_10.setText("")
        self.cal_pushButton_10.setObjectName("cal_pushButton_10")
        self.cal_pushButton_10.setIcon(QIcon('assets/back.png'))
        self.cal_pushButton_10.setIconSize(QtCore.QSize(50, 50))
        self.cal_pushButton_10.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.cal_pushButton_11 = QtWidgets.QPushButton(self.form)
        self.cal_pushButton_11.setGeometry(QtCore.QRect(720, 300, 65, 65))
        self.cal_pushButton_11.setStyleSheet("\n"
        "border-image: url(:/check/assets/check2.png);\n"
        "border-radius:30px\n"
        "")
        self.cal_pushButton_11.setText("")
        self.cal_pushButton_11.setObjectName("cal_pushButton_11")
        self.cal_pushButton_11.setIcon(QIcon('assets/check2.png'))
        self.cal_pushButton_11.setIconSize(QtCore.QSize(50, 50))
        self.cal_pushButton_11.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.cal_pushButton_11.clicked.connect(self.cal_save)

        #region Scroll 1
        self.cal_scrollArea = QtWidgets.QScrollArea(self.form)
        self.cal_scrollArea.setGeometry(QtCore.QRect(30, 80, 550, 200))
        self.cal_scrollArea.setWidgetResizable(True)
        self.cal_scrollArea.setObjectName("cal_scrollArea")
        self.cal_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.cal_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 534, 472))
        self.cal_scrollAreaWidgetContents.setObjectName("cal_scrollAreaWidgetContents")
        self.cal_gridLayout = QtWidgets.QGridLayout(self.cal_scrollAreaWidgetContents)
        self.cal_gridLayout.setObjectName("cal_gridLayout")
        self.cal_lineEdit_12 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents)
        self.cal_lineEdit_12.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_lineEdit_12.setObjectName("cal_lineEdit_12")
        self.cal_lineEdit_12.setText(self.dat.bottles["1"][0])
        self.cal_gridLayout.addWidget(self.cal_lineEdit_12, 0, 2, 1, 1)

        
        self.cal_lineEdit_15 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents)
        self.cal_lineEdit_15.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_lineEdit_15.setObjectName("cal_lineEdit_15")
        self.cal_lineEdit_15.setText(self.dat.bottles["2"][0])
        self.cal_gridLayout.addWidget(self.cal_lineEdit_15, 1, 2, 1, 1)

        
        self.cal_horizontalSlider = QtWidgets.QSlider(self.cal_scrollAreaWidgetContents)
        self.cal_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.cal_horizontalSlider.setObjectName("cal_horizontalSlider")
        self.cal_gridLayout.addWidget(self.cal_horizontalSlider, 0, 3, 1, 1)

        self.cal_lineEdit_10 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents)
        self.cal_lineEdit_10.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_lineEdit_10.setObjectName("cal_lineEdit_10")
        self.cal_lineEdit_10.setText(self.dat.bottles["3"][0])
        self.cal_gridLayout.addWidget(self.cal_lineEdit_10, 2, 2, 1, 1)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cal_horizontalSlider.sizePolicy().hasHeightForWidth())

        self.cal_horizontalSlider_2 = QtWidgets.QSlider(self.cal_scrollAreaWidgetContents)
        self.cal_horizontalSlider_2.setSizePolicy(sizePolicy)
        self.cal_horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.cal_horizontalSlider_2.setObjectName("cal_horizontalSlider_2")
        self.cal_gridLayout.addWidget(self.cal_horizontalSlider_2, 1, 3, 1, 1)

        self.cal_horizontalSlider_3 = QtWidgets.QSlider(self.cal_scrollAreaWidgetContents)
        self.cal_horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.cal_horizontalSlider_3.setObjectName("cal_horizontalSlider_3")
        self.cal_gridLayout.addWidget(self.cal_horizontalSlider_3, 2, 3, 1, 1)

        self.cal_horizontalSlider_4 = QtWidgets.QSlider(self.cal_scrollAreaWidgetContents)
        self.cal_horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.cal_horizontalSlider_4.setObjectName("cal_horizontalSlider_4")
        self.cal_gridLayout.addWidget(self.cal_horizontalSlider_4, 3, 3, 1, 1)

        self.cal_label_22 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents)
        self.cal_label_22.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_label_22.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.cal_label_22.setText("Item---1")
        self.cal_label_22.setObjectName("cal_label_22")
        self.cal_gridLayout.addWidget(self.cal_label_22, 0, 4, 1, 1)

        self.cal_horizontalSlider_5 = QtWidgets.QSlider(self.cal_scrollAreaWidgetContents)
        self.cal_horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.cal_horizontalSlider_5.setObjectName("cal_horizontalSlider_5")
        self.cal_gridLayout.addWidget(self.cal_horizontalSlider_5, 4, 3, 1, 1)

        self.cal_lineEdit_13 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents)
        self.cal_lineEdit_13.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_lineEdit_13.setObjectName("cal_lineEdit_13")
        self.cal_lineEdit_13.setText(self.dat.bottles["4"][0])
        self.cal_gridLayout.addWidget(self.cal_lineEdit_13, 3, 2, 1, 1)
        
        self.cal_label_26 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents)
        self.cal_label_26.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_label_26.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.cal_label_26.setText("Item---2")
        self.cal_label_26.setObjectName("cal_label_26")
        self.cal_gridLayout.addWidget(self.cal_label_26, 1, 4, 1, 1)

        self.cal_horizontalSlider_6 = QtWidgets.QSlider(self.cal_scrollAreaWidgetContents)
        self.cal_horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.cal_horizontalSlider_6.setObjectName("cal_horizontalSlider_6")
        self.cal_gridLayout.addWidget(self.cal_horizontalSlider_6, 5, 3, 1, 1)

        self.cal_label_18 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cal_label_18.sizePolicy().hasHeightForWidth())
        self.cal_label_18.setSizePolicy(sizePolicy)
        self.cal_label_18.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_label_18.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.cal_label_18.setText("Item---3")
        self.cal_label_18.setObjectName("cal_label_18")
        self.cal_gridLayout.addWidget(self.cal_label_18, 2, 4, 1, 1)

        self.cal_lineEdit_11 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents)
        self.cal_lineEdit_11.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_lineEdit_11.setObjectName("cal_lineEdit_11")
        self.cal_lineEdit_11.setText(self.dat.bottles["5"][0])
        self.cal_gridLayout.addWidget(self.cal_lineEdit_11, 4, 2, 1, 1)

        
        self.cal_label_19 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents)
        self.cal_label_19.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_label_19.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.cal_label_19.setText("Item---4")
        self.cal_label_19.setObjectName("cal_label_19")
        self.cal_gridLayout.addWidget(self.cal_label_19, 3, 4, 1, 1)

        self.cal_lineEdit_14 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents)
        self.cal_lineEdit_14.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_lineEdit_14.setObjectName("cal_lineEdit_14")
        self.cal_lineEdit_14.setText(self.dat.bottles["6"][0])
        self.cal_gridLayout.addWidget(self.cal_lineEdit_14, 5, 2, 1, 1)

        
        self.cal_horizontalSlider_7 = QtWidgets.QSlider(self.cal_scrollAreaWidgetContents)
        self.cal_horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.cal_horizontalSlider_7.setObjectName("cal_horizontalSlider_7")
        self.cal_gridLayout.addWidget(self.cal_horizontalSlider_7, 6, 3, 1, 1)

        self.cal_horizontalSlider_8 = QtWidgets.QSlider(self.cal_scrollAreaWidgetContents)
        self.cal_horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.cal_horizontalSlider_8.setObjectName("cal_horizontalSlider_8")
        self.cal_gridLayout.addWidget(self.cal_horizontalSlider_8, 7, 3, 1, 1)

        self.cal_horizontalSlider_9 = QtWidgets.QSlider(self.cal_scrollAreaWidgetContents)
        self.cal_horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.cal_horizontalSlider_9.setObjectName("cal_horizontalSlider_9")
        self.cal_gridLayout.addWidget(self.cal_horizontalSlider_9, 8, 3, 1, 1)

        self.cal_label_21 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents)
        self.cal_label_21.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_label_21.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.cal_label_21.setText("Item---5")
        self.cal_label_21.setObjectName("cal_label_21")
        self.cal_gridLayout.addWidget(self.cal_label_21, 4, 4, 1, 1)

        self.cal_lineEdit_9 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents)
        self.cal_lineEdit_9.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_lineEdit_9.setObjectName("cal_lineEdit_9")
        self.cal_lineEdit_9.setText(self.dat.bottles["7"][0])
        self.cal_gridLayout.addWidget(self.cal_lineEdit_9, 6, 2, 1, 1)

        
        self.cal_label_20 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents)
        self.cal_label_20.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_label_20.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.cal_label_20.setText("Item---6")
        self.cal_label_20.setObjectName("cal_label_20")
        self.cal_gridLayout.addWidget(self.cal_label_20, 5, 4, 1, 1)

        self.cal_label_24 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents)
        self.cal_label_24.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_label_24.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.cal_label_24.setText("Item---7")
        self.cal_label_24.setObjectName("cal_label_24")
        self.cal_gridLayout.addWidget(self.cal_label_24, 6, 4, 1, 1)

        self.cal_lineEdit_7 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.cal_lineEdit_7.sizePolicy().hasHeightForWidth())
        self.cal_lineEdit_7.setSizePolicy(sizePolicy)
        self.cal_lineEdit_7.setMinimumSize(QtCore.QSize(30, 40))
        self.cal_lineEdit_7.setObjectName("cal_lineEdit_7")
        self.cal_lineEdit_7.setText(self.dat.bottles["8"][0])
        self.cal_gridLayout.addWidget(self.cal_lineEdit_7, 7, 2, 1, 1)

        
        self.cal_label_23 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents)
        self.cal_label_23.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_label_23.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.cal_label_23.setText("Item---8")
        self.cal_label_23.setObjectName("cal_label_23")
        self.cal_gridLayout.addWidget(self.cal_label_23, 7, 4, 1, 1)

        self.cal_lineEdit_8 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents)
        self.cal_lineEdit_8.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_lineEdit_8.setObjectName("cal_lineEdit_8")
        self.cal_lineEdit_8.setText(self.dat.bottles["9"][0])
        self.cal_gridLayout.addWidget(self.cal_lineEdit_8, 8, 2, 1, 1)

        
        self.cal_label_25 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents)
        self.cal_label_25.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_label_25.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.cal_label_25.setText("Item---9")
        self.cal_label_25.setObjectName("cal_label_25")
        self.cal_gridLayout.addWidget(self.cal_label_25, 8, 4, 1, 1)

        self.cal_lineEdit_16 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents)
        self.cal_lineEdit_16.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_lineEdit_16.setObjectName("cal_lineEdit_16")
        self.cal_lineEdit_16.setText(self.dat.bottles["10"][0])
        self.cal_gridLayout.addWidget(self.cal_lineEdit_16, 9, 2, 1, 1)

        
        self.cal_horizontalSlider_10 = QtWidgets.QSlider(self.cal_scrollAreaWidgetContents)
        self.cal_horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.cal_horizontalSlider_10.setObjectName("cal_horizontalSlider_10")
        self.cal_gridLayout.addWidget(self.cal_horizontalSlider_10, 9, 3, 1, 1)

        self.cal_label_27 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents)
        self.cal_label_27.setMinimumSize(QtCore.QSize(0, 40))
        self.cal_label_27.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.cal_label_27.setText("Item---10")
        self.cal_label_27.setObjectName("cal_label_27")
        self.cal_gridLayout.addWidget(self.cal_label_27, 9, 4, 1, 1)

        self.cal_scrollArea.setWidget(self.cal_scrollAreaWidgetContents)

        #endregion Scroll 1
        
        #region Slider formatter
        self.cal_horizontalSlider.setMaximum(3000)
        self.cal_horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider.valueChanged.connect(self.cal_update_val)
        self.cal_horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider.setTickInterval(100)


        self.cal_horizontalSlider_2.setMaximum(3000)
        self.cal_horizontalSlider_2.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_2.valueChanged.connect(self.cal_update_val)
        self.cal_horizontalSlider_2.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_2.setTickInterval(100)


        self.cal_horizontalSlider_3.setMaximum(3000)
        self.cal_horizontalSlider_3.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_3.valueChanged.connect(self.cal_update_val)
        self.cal_horizontalSlider_3.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_3.setTickInterval(100)


        self.cal_horizontalSlider_4.setMaximum(3000)
        self.cal_horizontalSlider_4.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_4.valueChanged.connect(self.cal_update_val)
        self.cal_horizontalSlider_4.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_4.setTickInterval(100)


        self.cal_horizontalSlider_5.setMaximum(3000)
        self.cal_horizontalSlider_5.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_5.valueChanged.connect(self.cal_update_val)
        self.cal_horizontalSlider_5.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_5.setTickInterval(100)


        self.cal_horizontalSlider_6.setMaximum(3000)
        self.cal_horizontalSlider_6.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_6.valueChanged.connect(self.cal_update_val)
        self.cal_horizontalSlider_6.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_6.setTickInterval(100)


        self.cal_horizontalSlider_7.setMaximum(3000)
        self.cal_horizontalSlider_7.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_7.valueChanged.connect(self.cal_update_val)
        self.cal_horizontalSlider_7.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_7.setTickInterval(100)


        self.cal_horizontalSlider_8.setMaximum(3000)
        self.cal_horizontalSlider_8.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_8.valueChanged.connect(self.cal_update_val)
        self.cal_horizontalSlider_8.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_8.setTickInterval(100)


        self.cal_horizontalSlider_9.setMaximum(3000)
        self.cal_horizontalSlider_9.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_9.valueChanged.connect(self.cal_update_val)
        self.cal_horizontalSlider_9.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_9.setTickInterval(100)


        self.cal_horizontalSlider_10.setMaximum(3000)
        self.cal_horizontalSlider_10.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_10.valueChanged.connect(self.cal_update_val)
        self.cal_horizontalSlider_10.setTickPosition(QSlider.TicksBelow)
        self.cal_horizontalSlider_10.setTickInterval(100)
        #endregion Slider formatter

        #region Scroll 2
        self.cal_scrollArea_2 = QtWidgets.QScrollArea(self.form)
        self.cal_scrollArea_2.setGeometry(QtCore.QRect(600, 80, 162, 200))
        self.cal_scrollArea_2.setWidgetResizable(True)
        self.cal_scrollArea_2.setObjectName("cal_scrollArea_2")
        self.cal_scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.cal_scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 146, 336))
        self.cal_scrollAreaWidgetContents_2.setObjectName("cal_scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.cal_scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("cal_verticalLayout")
        self.cal_label_12 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents_2)
        self.cal_label_12.setObjectName("cal_label_12")
        self.verticalLayout.addWidget(self.cal_label_12)
        self.cal_lineEdit = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents_2)
        self.cal_lineEdit.setObjectName("cal_lineEdit")
        self.cal_lineEdit.setText(self.dat.boxes['1'])

        self.verticalLayout.addWidget(self.cal_lineEdit)
        self.cal_label_13 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents_2)
        self.cal_label_13.setObjectName("cal_label_13")
        self.verticalLayout.addWidget(self.cal_label_13)
        self.cal_lineEdit_2 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents_2)
        self.cal_lineEdit_2.setObjectName("cal_lineEdit_2")
        self.cal_lineEdit_2.setText(self.dat.boxes['2'])
        
        self.verticalLayout.addWidget(self.cal_lineEdit_2)
        self.cal_label_14 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents_2)
        self.cal_label_14.setObjectName("cal_label_14")
        self.verticalLayout.addWidget(self.cal_label_14)
        self.cal_lineEdit_3 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents_2)
        self.cal_lineEdit_3.setObjectName("cal_lineEdit_3")
        self.cal_lineEdit_3.setText(self.dat.boxes['3'])
        
        self.verticalLayout.addWidget(self.cal_lineEdit_3)
        self.cal_label_15 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents_2)
        self.cal_label_15.setObjectName("cal_label_15")
        self.verticalLayout.addWidget(self.cal_label_15)
        self.cal_lineEdit_4 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents_2)
        self.cal_lineEdit_4.setObjectName("cal_lineEdit_4")
        self.cal_lineEdit_4.setText(self.dat.boxes['4'])
        
        self.verticalLayout.addWidget(self.cal_lineEdit_4)
        self.cal_label_16 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents_2)
        self.cal_label_16.setObjectName("cal_label_16")
        self.verticalLayout.addWidget(self.cal_label_16)
        self.cal_lineEdit_5 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents_2)
        self.cal_lineEdit_5.setObjectName("cal_lineEdit_5")
        self.cal_lineEdit_5.setText(self.dat.boxes['5'])
        
        self.verticalLayout.addWidget(self.cal_lineEdit_5)
        self.cal_label_17 = QtWidgets.QLabel(self.cal_scrollAreaWidgetContents_2)
        self.cal_label_17.setObjectName("cal_label_17")
        self.verticalLayout.addWidget(self.cal_label_17)
        self.cal_lineEdit_6 = QtWidgets.QLineEdit(self.cal_scrollAreaWidgetContents_2)
        self.cal_lineEdit_6.setObjectName("cal_lineEdit_6")
        self.cal_lineEdit_6.setText(self.dat.boxes['6'])
        
        self.verticalLayout.addWidget(self.cal_lineEdit_6)
        self.cal_scrollArea_2.setWidget(self.cal_scrollAreaWidgetContents_2)
        self.cal_label_2.raise_()
        self.cal_pushButton_7.raise_()
        self.cal_pushButton_11.raise_()
        self.cal_pushButton_10.raise_()
        self.cal_scrollArea.raise_()
        self.cal_scrollArea_2.raise_()
        #endregion Scroll 2

        self.cal_retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.form)

    def cal_update_val(self):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle("Mixology")

        self.cal_horizontalSlider.setValue(int(self.cal_horizontalSlider.value()/100)*100)
        self.cal_horizontalSlider_2.setValue(int(self.cal_horizontalSlider_2.value()/100)*100)
        self.cal_horizontalSlider_3.setValue(int(self.cal_horizontalSlider_3.value()/100)*100)
        self.cal_horizontalSlider_4.setValue(int(self.cal_horizontalSlider_4.value()/100)*100)
        self.cal_horizontalSlider_5.setValue(int(self.cal_horizontalSlider_5.value()/100)*100)
        self.cal_horizontalSlider_6.setValue(int(self.cal_horizontalSlider_6.value()/100)*100)
        self.cal_horizontalSlider_7.setValue(int(self.cal_horizontalSlider_7.value()/100)*100)
        self.cal_horizontalSlider_8.setValue(int(self.cal_horizontalSlider_8.value()/100)*100)
        self.cal_horizontalSlider_9.setValue(int(self.cal_horizontalSlider_9.value()/100)*100)
        self.cal_horizontalSlider_10.setValue(int(self.cal_horizontalSlider_10.value()/100)*100)

        self.cal_label_22.setText(str(self.cal_horizontalSlider.value())+" ml")
        self.cal_label_26.setText(str(self.cal_horizontalSlider_2.value())+" ml")
        self.cal_label_18.setText(str(self.cal_horizontalSlider_3.value())+" ml")
        self.cal_label_19.setText(str(self.cal_horizontalSlider_4.value())+" ml")
        self.cal_label_21.setText(str(self.cal_horizontalSlider_5.value())+" ml")
        self.cal_label_20.setText(str(self.cal_horizontalSlider_6.value())+" ml")
        self.cal_label_24.setText(str(self.cal_horizontalSlider_7.value())+" ml")
        self.cal_label_23.setText(str(self.cal_horizontalSlider_8.value())+" ml")
        self.cal_label_25.setText(str(self.cal_horizontalSlider_9.value())+" ml")
        self.cal_label_27.setText(str(self.cal_horizontalSlider_10.value())+" ml")

    def cal_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle(_translate("self.form", "self.form"))
        self.cal_pushButton_7.setText(_translate("self.form", "X"))
        self.cal_label_2.setText(_translate("self.form", "    CALIBRATE"))
        self.cal_label_12.setText(_translate("self.form", "Box 1"))
        self.cal_label_13.setText(_translate("self.form", "Box 2"))
        self.cal_label_14.setText(_translate("self.form", "Box 3"))
        self.cal_label_15.setText(_translate("self.form", "Box 4"))
        self.cal_label_16.setText(_translate("self.form", "Box 5"))
        self.cal_label_17.setText(_translate("self.form", "Box 6"))
        self.cal_label_22.setText(str(self.dat.bottles["1"][1])+" ml")
        self.cal_label_26.setText(str(self.dat.bottles["2"][1])+" ml")
        self.cal_label_18.setText(str(self.dat.bottles["3"][1])+" ml")
        self.cal_label_19.setText(str(self.dat.bottles["4"][1])+" ml")
        self.cal_label_21.setText(str(self.dat.bottles["5"][1])+" ml")
        self.cal_label_20.setText(str(self.dat.bottles["6"][1])+" ml")
        self.cal_label_24.setText(str(self.dat.bottles["7"][1])+" ml")
        self.cal_label_23.setText(str(self.dat.bottles["8"][1])+" ml")
        self.cal_label_25.setText(str(self.dat.bottles["9"][1])+" ml")
        self.cal_label_27.setText(str(self.dat.bottles["10"][1])+" ml")
        self.cal_horizontalSlider.setValue(self.dat.bottles["1"][1])
        self.cal_horizontalSlider_2.setValue(self.dat.bottles["2"][1])
        self.cal_horizontalSlider_3.setValue(self.dat.bottles["3"][1])
        self.cal_horizontalSlider_4.setValue(self.dat.bottles["4"][1])
        self.cal_horizontalSlider_5.setValue(self.dat.bottles["5"][1])
        self.cal_horizontalSlider_6.setValue(self.dat.bottles["6"][1])
        self.cal_horizontalSlider_7.setValue(self.dat.bottles["7"][1])
        self.cal_horizontalSlider_8.setValue(self.dat.bottles["8"][1])
        self.cal_horizontalSlider_9.setValue(self.dat.bottles["9"][1])
        self.cal_horizontalSlider_10.setValue(self.dat.bottles["10"][1])
        
    def cal_save(self):
        self.dat.change_bottle(1,self.cal_lineEdit_12.text(),self.cal_horizontalSlider.value())
        self.dat.change_bottle(2,self.cal_lineEdit_15.text(),self.cal_horizontalSlider_2.value())
        self.dat.change_bottle(3,self.cal_lineEdit_10.text(),self.cal_horizontalSlider_3.value())
        self.dat.change_bottle(4,self.cal_lineEdit_13.text(),self.cal_horizontalSlider_4.value())
        self.dat.change_bottle(5,self.cal_lineEdit_11.text(),self.cal_horizontalSlider_5.value())
        self.dat.change_bottle(6,self.cal_lineEdit_14.text(),self.cal_horizontalSlider_6.value())
        self.dat.change_bottle(7,self.cal_lineEdit_9.text(),self.cal_horizontalSlider_7.value())
        self.dat.change_bottle(8,self.cal_lineEdit_7.text(),self.cal_horizontalSlider_8.value())
        self.dat.change_bottle(9,self.cal_lineEdit_8.text(),self.cal_horizontalSlider_9.value())
        self.dat.change_bottle(10,self.cal_lineEdit_16.text(),self.cal_horizontalSlider_10.value())
        self.dat.change_box(1,self.cal_lineEdit.text())
        self.dat.change_box(2,self.cal_lineEdit_2.text())
        self.dat.change_box(3,self.cal_lineEdit_3.text())
        self.dat.change_box(4,self.cal_lineEdit_4.text())
        self.dat.change_box(5,self.cal_lineEdit_5.text())
        self.dat.change_box(6,self.cal_lineEdit_6.text())
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Information Updated")
        # msg.setInformativeText('More information')
        msg.setWindowTitle("Done")
        msg.exec_()
        self.dat.__init__()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    ui.calibrate_form()
    Form.show()
    sys.exit(app.exec_())

