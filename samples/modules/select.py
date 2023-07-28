# -*- coding: utf-8 -*-

# self.form implementation generated from reading ui file 'uis/Select.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from logic.data import Data
# from logic.control import Control
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def __init__(self, Form):
        self.form = Form
        self.dat = Data()
        self.trash = False

    def select_form(self):
        self.form.setObjectName("Form")
        self.form.resize(800, 380)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.form.setFont(font)
        self.sel_pushButton_8 = QtWidgets.QPushButton(self.form)
        self.sel_pushButton_8.setGeometry(QtCore.QRect(730, 30, 41, 31))
        self.sel_pushButton_8.setStyleSheet("background: #AA0000;\n"
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
        self.sel_pushButton_8.setObjectName("pushButton_8")
        self.sel_label_18 = QtWidgets.QLabel(self.form)
        self.sel_label_18.setGeometry(QtCore.QRect(0, 0, 800, 74))
        self.sel_label_18.setStyleSheet("font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: bold;\n"
        "font-size: 36px;\n"
        "line-height: 42px;\n"
        "\n"
        "color: #FFFFFF;\n"
        "background-color: #E09825;")
        self.sel_label_18.setObjectName("label_18")
        self.sel_pushButton_9 = QtWidgets.QPushButton(self.form)
        self.sel_pushButton_9.setGeometry(QtCore.QRect(730, 20, 41, 31))
        self.sel_pushButton_9.setStyleSheet("background: #AA0000;\n"
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
        self.sel_pushButton_9.setObjectName("pushButton_9")
        self.sel_pushButton_9.clicked.connect(lambda: sys.exit(0))
        self.sel_pushButton = QtWidgets.QPushButton(self.form)
        self.sel_pushButton.setGeometry(QtCore.QRect(30, 300, 65, 65))
        self.sel_pushButton.setStyleSheet("border-image: url(:/back/assets/back.png);\n"
        "\n"
        "border-radius:30px")
        self.sel_pushButton.setText("")
        self.sel_pushButton.setIcon(QIcon('assets/back.png'))
        self.sel_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.sel_pushButton.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.sel_pushButton.setObjectName("pushButton")
        self.sel_scrollArea = QtWidgets.QScrollArea(self.form)
        self.sel_scrollArea.setGeometry(QtCore.QRect(70, 80, 651, 200))
        self.sel_scrollArea.setWidgetResizable(True)
        self.sel_scrollArea.setObjectName("scrollArea")
        self.sel_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.sel_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -228, 635, 426))
        self.sel_scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sel_gridLayout = QtWidgets.QGridLayout(self.sel_scrollAreaWidgetContents)
        self.sel_gridLayout.setObjectName("gridLayout")
        self.sel_label_7 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        self.sel_label_7.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_7.setFont(font)
        self.sel_label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_label_7.setStyleSheet("background-color: rgb(186, 189, 182);\n"
        "color: #000000;")
        self.sel_label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_7.setObjectName("label_7")
        self.sel_gridLayout.addWidget(self.sel_label_7, 0, 3, 1, 1)
        self.sel_label_16 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_16.setFont(font)
        self.sel_label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_label_16.setStyleSheet("background-color: rgb(136, 138, 133);\n"
        "color: #FFFFFF;")
        self.sel_label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_16.setObjectName("label_16")
        self.sel_gridLayout.addWidget(self.sel_label_16, 1, 3, 1, 1)
        self.sel_label_36 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        self.sel_label_36.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_36.setFont(font)
        self.sel_label_36.setStyleSheet("background-color: rgb(136, 138, 133);\n"
        "color: #FFFFFF;\n"
        "\n"
        "\n"
        "\n"
        "")
        self.sel_label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_36.setObjectName("label_36")
        self.sel_gridLayout.addWidget(self.sel_label_36, 0, 1, 1, 1)
        self.sel_label_32 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        self.sel_label_32.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_32.setFont(font)
        self.sel_label_32.setStyleSheet("background-color: rgb(186, 189, 182);\n"
        "color: #000000;\n"
        "\n"
        "\n"
        "")
        self.sel_label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_32.setObjectName("label_32")
        self.sel_gridLayout.addWidget(self.sel_label_32, 1, 1, 1, 1)
        self.sel_label_33 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_33.setFont(font)
        self.sel_label_33.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_label_33.setStyleSheet("background-color: rgb(186, 189, 182);\n"
        "color: #000000;")
        self.sel_label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_33.setObjectName("label_33")
        self.sel_gridLayout.addWidget(self.sel_label_33, 2, 3, 1, 1)
        self.sel_label_22 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        self.sel_label_22.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_22.setFont(font)
        self.sel_label_22.setStyleSheet("background-color: rgb(136, 138, 133);\n"
        "color: #FFFFFF;\n"
        "\n"
        "\n"
        "")
        self.sel_label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_22.setObjectName("label_22")
        self.sel_gridLayout.addWidget(self.sel_label_22, 2, 1, 1, 1)
        self.sel_label_23 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_23.setFont(font)
        self.sel_label_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_label_23.setStyleSheet("background-color: rgb(136, 138, 133);\n"
        "color: #FFFFFF;")
        self.sel_label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_23.setObjectName("label_23")
        self.sel_gridLayout.addWidget(self.sel_label_23, 3, 3, 1, 1)
        self.sel_label_40 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        self.sel_label_40.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_40.setFont(font)
        self.sel_label_40.setStyleSheet("background-color: rgb(186, 189, 182);\n"
        "color: #000000;\n"
        "\n"
        "\n"
        "")
        self.sel_label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_40.setObjectName("label_40")
        self.sel_gridLayout.addWidget(self.sel_label_40, 3, 1, 1, 1)
        self.sel_label_31 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        self.sel_label_31.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_31.setFont(font)
        self.sel_label_31.setStyleSheet("background-color: rgb(136, 138, 133);\n"
        "color: #FFFFFF;\n"
        "\n"
        "\n"
        "")
        self.sel_label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_31.setObjectName("label_31")
        self.sel_gridLayout.addWidget(self.sel_label_31, 4, 1, 1, 1)
        self.sel_label_28 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_28.setFont(font)
        self.sel_label_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_label_28.setStyleSheet("background-color: rgb(186, 189, 182);\n"
        "color: #000000;")
        self.sel_label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_28.setObjectName("label_28")
        self.sel_gridLayout.addWidget(self.sel_label_28, 4, 3, 1, 1)
        self.sel_label_24 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        self.sel_label_24.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_24.setFont(font)
        self.sel_label_24.setStyleSheet("background-color: rgb(186, 189, 182);\n"
        "color: #000000;\n"
        "\n"
        "\n"
        "")
        self.sel_label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_24.setObjectName("label_24")
        self.sel_gridLayout.addWidget(self.sel_label_24, 5, 1, 1, 1)
        self.sel_label_19 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_19.setFont(font)
        self.sel_label_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_label_19.setStyleSheet("background-color: rgb(136, 138, 133);\n"
        "color: #FFFFFF;")
        self.sel_label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_19.setObjectName("label_19")
        self.sel_gridLayout.addWidget(self.sel_label_19, 5, 3, 1, 1)
        self.sel_label_38 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_38.setFont(font)
        self.sel_label_38.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_label_38.setStyleSheet("background-color: rgb(186, 189, 182);\n"
        "color: #000000;")
        self.sel_label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_38.setObjectName("label_38")
        self.sel_gridLayout.addWidget(self.sel_label_38, 6, 3, 1, 1)
        self.sel_label_37 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_37.setFont(font)
        self.sel_label_37.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_label_37.setStyleSheet("background-color: rgb(136, 138, 133);\n"
        "color: #FFFFFF;\n")
        self.sel_label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_37.setObjectName("label_37")
        self.sel_gridLayout.addWidget(self.sel_label_37, 7, 3, 1, 1)
        self.sel_label_20 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        self.sel_label_20.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_20.setFont(font)
        self.sel_label_20.setStyleSheet("background-color: rgb(136, 138, 133);\n"
        "color: #FFFFFF;\n"
        "\n"
        "\n"
        "")
        self.sel_label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_20.setObjectName("label_20")
        self.sel_gridLayout.addWidget(self.sel_label_20, 6, 1, 1, 1)
        self.sel_label_30 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_30.setFont(font)
        self.sel_label_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_label_30.setStyleSheet("background-color: rgb(186, 189, 182);\n"
        "color: #000000;")
        self.sel_label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_30.setObjectName("label_30")
        self.sel_gridLayout.addWidget(self.sel_label_30, 8, 3, 1, 1)
        self.sel_label_25 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        self.sel_label_25.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_25.setFont(font)
        self.sel_label_25.setStyleSheet("background-color: rgb(186, 189, 182);\n"
        "color: #000000;\n"
        "\n"
        "\n"
        "")
        self.sel_label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_25.setObjectName("label_25")
        self.sel_gridLayout.addWidget(self.sel_label_25, 7, 1, 1, 1)
        self.sel_label_41 = QtWidgets.QLabel(self.sel_scrollAreaWidgetContents)
        self.sel_label_41.setEnabled(True)
        self.sel_label_41.setMinimumSize(QtCore.QSize(0, 40))
        self.sel_label_41.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sel_label_41.setBaseSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sel_label_41.setFont(font)
        self.sel_label_41.setStyleSheet("background-color: rgb(136, 138, 133);\n"
        "color: #FFFFFF;\n"
        "\n"
        "\n"
        "")
        self.sel_label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.sel_label_41.setObjectName("label_41")
        self.sel_gridLayout.addWidget(self.sel_label_41, 8, 1, 1, 1)
        self.sel_pushButton_3 = QtWidgets.QPushButton(self.sel_scrollAreaWidgetContents)
        self.sel_pushButton_3.setObjectName("pushButton_3")
        self.sel_pushButton_3.clicked.connect(lambda: self.sel_add_to_queue(1,[self.sel_pushButton_3,self.sel_label_36,self.sel_label_7]))

        self.sel_gridLayout.addWidget(self.sel_pushButton_3, 0, 0, 1, 1)
        self.sel_pushButton_4 = QtWidgets.QPushButton(self.sel_scrollAreaWidgetContents)
        self.sel_pushButton_4.setObjectName("pushButton_4")
        self.sel_pushButton_4.clicked.connect(lambda: self.sel_add_to_queue(2,[self.sel_pushButton_4,self.sel_label_32,self.sel_label_16]))

        self.sel_gridLayout.addWidget(self.sel_pushButton_4, 1, 0, 1, 1)
        self.sel_pushButton_5 = QtWidgets.QPushButton(self.sel_scrollAreaWidgetContents)
        self.sel_pushButton_5.setObjectName("pushButton_5")
        self.sel_pushButton_5.clicked.connect(lambda: self.sel_add_to_queue(3,[self.sel_pushButton_5,self.sel_label_22,self.sel_label_33]))

        self.sel_gridLayout.addWidget(self.sel_pushButton_5, 2, 0, 1, 1)
        self.sel_pushButton_6 = QtWidgets.QPushButton(self.sel_scrollAreaWidgetContents)
        self.sel_pushButton_6.setObjectName("pushButton_6")
        self.sel_pushButton_6.clicked.connect(lambda: self.sel_add_to_queue(4,[self.sel_pushButton_6,self.sel_label_40,self.sel_label_23]))

        self.sel_gridLayout.addWidget(self.sel_pushButton_6, 3, 0, 1, 1)
        self.sel_pushButton_7 = QtWidgets.QPushButton(self.sel_scrollAreaWidgetContents)
        self.sel_pushButton_7.setObjectName("pushButton_7")
        self.sel_pushButton_7.clicked.connect(lambda: self.sel_add_to_queue(5,[self.sel_pushButton_7,self.sel_label_31,self.sel_label_28]))

        self.sel_gridLayout.addWidget(self.sel_pushButton_7, 4, 0, 1, 1)
        self.sel_pushButton_10 = QtWidgets.QPushButton(self.sel_scrollAreaWidgetContents)
        self.sel_pushButton_10.setObjectName("pushButton_10")
        self.sel_pushButton_10.clicked.connect(lambda: self.sel_add_to_queue(6,[self.sel_pushButton_10,self.sel_label_24,self.sel_label_19]))

        self.sel_gridLayout.addWidget(self.sel_pushButton_10, 5, 0, 1, 1)
        self.sel_pushButton_11 = QtWidgets.QPushButton(self.sel_scrollAreaWidgetContents)
        self.sel_pushButton_11.setObjectName("pushButton_11")
        self.sel_pushButton_11.clicked.connect(lambda: self.sel_add_to_queue(7,[self.sel_pushButton_11,self.sel_label_20,self.sel_label_38]))

        self.sel_gridLayout.addWidget(self.sel_pushButton_11, 6, 0, 1, 1)
        self.sel_pushButton_12 = QtWidgets.QPushButton(self.sel_scrollAreaWidgetContents)
        self.sel_pushButton_12.setObjectName("pushButton_12")
        self.sel_pushButton_12.clicked.connect(lambda: self.sel_add_to_queue(8,[self.sel_pushButton_12,self.sel_label_25,self.sel_label_37]))

        self.sel_gridLayout.addWidget(self.sel_pushButton_12, 7, 0, 1, 1)
        self.sel_pushButton_13 = QtWidgets.QPushButton(self.sel_scrollAreaWidgetContents)
        self.sel_pushButton_13.setObjectName("pushButton_13")
        self.sel_pushButton_13.clicked.connect(lambda: self.sel_add_to_queue(9,[self.sel_pushButton_13,self.sel_label_41,self.sel_label_30]))

        self.sel_gridLayout.addWidget(self.sel_pushButton_13, 8, 0, 1, 1)
        self.sel_scrollArea.setWidget(self.sel_scrollAreaWidgetContents)
        self.sel_pushButton_2 = QtWidgets.QPushButton(self.form)
        self.sel_pushButton_2.setGeometry(QtCore.QRect(720, 300, 65, 65))
        self.sel_pushButton_2.setStyleSheet("border-image: url(:/check/assets/check2.png);\n"
        "\n"
        "border-radius:30px")
        self.sel_pushButton_2.setText("")
        self.sel_pushButton_2.setIcon(QIcon('assets/play.png'))
        self.sel_pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.sel_pushButton_2.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.sel_pushButton_2.setObjectName("pushButton_2")
        self.sel_pushButton_2.clicked.connect(self.sel_prepare)

        self.sel_pushButton_14 = QtWidgets.QPushButton(self.form)
        self.sel_pushButton_14.setText("Clean queue")
        self.sel_pushButton_14.clicked.connect(self.sel_clear_queue)
        self.sel_pushButton_14.setGeometry(QtCore.QRect(350, 300, 100, 65))
        self.sel_pushButton_14.setObjectName("pushButton_14")

        self.sel_pushButton_15 = QtWidgets.QPushButton(self.form)
        self.sel_pushButton_15.setGeometry(QtCore.QRect(650, 300, 65, 65))
        self.sel_pushButton_15.setStyleSheet("border-image: url(:/check/assets/check2.png);\n"
        "\n"
        "border-radius:30px")
        self.sel_pushButton_15.setText("")
        self.sel_pushButton_15.setIcon(QIcon('assets/trash2.png'))
        self.sel_pushButton_15.setIconSize(QtCore.QSize(50, 50))
        self.sel_pushButton_15.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.sel_pushButton_15.setObjectName("pushButton_15")
        self.sel_pushButton_15.clicked.connect(self.sel_toggleTrashcan)
        self.sel_retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.form)

    def sel_toggleTrashcan(self):
        self.trash = not self.trash
        self.sel_label_7.setStyleSheet("background-color: #D32F2F; color: #FFFFFF;" if self.trash else "background-color: rgb(186, 189, 182);\ncolor: #000000;")
        self.sel_label_32.setStyleSheet("background-color: #D32F2F; color: #FFFFFF;" if self.trash else "background-color: rgb(186, 189, 182);\ncolor: #000000;")
        self.sel_label_33.setStyleSheet("background-color: #D32F2F; color: #FFFFFF;" if self.trash else "background-color: rgb(186, 189, 182);\ncolor: #000000;")
        self.sel_label_40.setStyleSheet("background-color: #D32F2F; color: #FFFFFF;" if self.trash else "background-color: rgb(186, 189, 182);\ncolor: #000000;")
        self.sel_label_28.setStyleSheet("background-color: #D32F2F; color: #FFFFFF;" if self.trash else "background-color: rgb(186, 189, 182);\ncolor: #000000;")
        self.sel_label_24.setStyleSheet("background-color: #D32F2F; color: #FFFFFF;" if self.trash else "background-color: rgb(186, 189, 182);\ncolor: #000000;")
        self.sel_label_38.setStyleSheet("background-color: #D32F2F; color: #FFFFFF;" if self.trash else "background-color: rgb(186, 189, 182);\ncolor: #000000;")
        self.sel_label_30.setStyleSheet("background-color: #D32F2F; color: #FFFFFF;" if self.trash else "background-color: rgb(186, 189, 182);\ncolor: #000000;")
        self.sel_label_25.setStyleSheet("background-color: #D32F2F; color: #FFFFFF;" if self.trash else "background-color: rgb(186, 189, 182);\ncolor: #000000;")

        self.sel_label_16.setStyleSheet("background-color: #E57373; color: #000000;" if self.trash else "background-color: rgb(136, 138, 133);\ncolor: #FFFFFF;")
        self.sel_label_36.setStyleSheet("background-color: #E57373; color: #000000;" if self.trash else "background-color: rgb(136, 138, 133);\ncolor: #FFFFFF;")
        self.sel_label_22.setStyleSheet("background-color: #E57373; color: #000000;" if self.trash else "background-color: rgb(136, 138, 133);\ncolor: #FFFFFF;")
        self.sel_label_23.setStyleSheet("background-color: #E57373; color: #000000;" if self.trash else "background-color: rgb(136, 138, 133);\ncolor: #FFFFFF;")
        self.sel_label_31.setStyleSheet("background-color: #E57373; color: #000000;" if self.trash else "background-color: rgb(136, 138, 133);\ncolor: #FFFFFF;")
        self.sel_label_19.setStyleSheet("background-color: #E57373; color: #000000;" if self.trash else "background-color: rgb(136, 138, 133);\ncolor: #FFFFFF;")
        self.sel_label_37.setStyleSheet("background-color: #E57373; color: #000000;" if self.trash else "background-color: rgb(136, 138, 133);\ncolor: #FFFFFF;")
        self.sel_label_20.setStyleSheet("background-color: #E57373; color: #000000;" if self.trash else "background-color: rgb(136, 138, 133);\ncolor: #FFFFFF;")
        self.sel_label_41.setStyleSheet("background-color: #E57373; color: #000000;" if self.trash else "background-color: rgb(136, 138, 133);\ncolor: #FFFFFF;")

        self.sel_pushButton_3.setText("Remove" if self.trash else "Add queue")
        self.sel_pushButton_4.setText("Remove" if self.trash else "Add queue")
        self.sel_pushButton_5.setText("Remove" if self.trash else "Add queue")
        self.sel_pushButton_6.setText("Remove" if self.trash else "Add queue")
        self.sel_pushButton_7.setText("Remove" if self.trash else "Add queue")
        self.sel_pushButton_10.setText("Remove" if self.trash else "Add queue")
        self.sel_pushButton_11.setText("Remove" if self.trash else "Add queue")
        self.sel_pushButton_12.setText("Remove" if self.trash else "Add queue")
        self.sel_pushButton_13.setText("Remove" if self.trash else "Add queue")

        self.sel_pushButton_15.setIcon(QIcon('assets/list.png' if self.trash else 'assets/trash2.png'))

    def sel_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle(_translate("self.form", "self.form"))
        self.sel_pushButton_8.setText(_translate("self.form", "X"))
        self.sel_label_18.setText(_translate("self.form", "    SELECT"))
        self.sel_pushButton_9.setText(_translate("self.form", "X"))
        
        try:
            self.sel_label_36.setVisible(True)
            self.sel_label_36.setText(_translate("self.form", self.dat.df.Name[0]))
            self.sel_label_7.setVisible(True)
            self.sel_label_7.setText(_translate("self.form", self.dat.df.Ingredients[0]+","+self.dat.df.Boxes[0]))
            self.sel_pushButton_3.setVisible(True)
            self.sel_pushButton_3.setText(_translate("self.form", "add queue"))
        except:
            self.sel_label_36.setVisible(False)
            self.sel_label_7.setVisible(False)
            self.sel_pushButton_3.setVisible(False)
        try:
            self.sel_label_32.setVisible(True)
            self.sel_label_32.setText(_translate("self.form", self.dat.df.Name[1]))
            self.sel_label_16.setVisible(True)
            self.sel_label_16.setText(_translate("self.form", self.dat.df.Ingredients[1]+","+self.dat.df.Boxes[1]))
            self.sel_pushButton_4.setVisible(True)
            self.sel_pushButton_4.setText(_translate("self.form", "add queue"))
        except:
            self.sel_label_32.setVisible(False)
            self.sel_label_16.setVisible(False)
            self.sel_pushButton_4.setVisible(False)
        try:
            self.sel_label_22.setVisible(True)
            self.sel_label_22.setText(_translate("self.form", self.dat.df.Name[2]))
            self.sel_label_33.setVisible(True)
            self.sel_label_33.setText(_translate("self.form", self.dat.df.Ingredients[2]+","+self.dat.df.Boxes[2]))
            self.sel_pushButton_5.setVisible(True)
            self.sel_pushButton_5.setText(_translate("self.form", "add queue"))
        except:
            self.sel_label_22.setVisible(False)
            self.sel_label_33.setVisible(False)
            self.sel_pushButton_5.setVisible(False)
        try:
            self.sel_label_40.setVisible(True)
            self.sel_label_40.setText(_translate("self.form", self.dat.df.Name[3]))
            self.sel_label_23.setVisible(True)
            self.sel_label_23.setText(_translate("self.form", self.dat.df.Ingredients[3]+","+self.dat.df.Boxes[3]))
            self.sel_pushButton_6.setVisible(True)
            self.sel_pushButton_6.setText(_translate("self.form", "add queue"))
        except:
            self.sel_label_40.setVisible(False)
            self.sel_label_23.setVisible(False)
            self.sel_pushButton_6.setVisible(False)
        try:
            self.sel_label_31.setVisible(True)
            self.sel_label_31.setText(_translate("self.form", self.dat.df.Name[4]))
            self.sel_label_28.setVisible(True)
            self.sel_label_28.setText(_translate("self.form", self.dat.df.Ingredients[4]+","+self.dat.df.Boxes[4]))
            self.sel_pushButton_7.setVisible(True)
            self.sel_pushButton_7.setText(_translate("self.form", "add queue"))
        except:
            self.sel_label_31.setVisible(False)
            self.sel_label_28.setVisible(False)
            self.sel_pushButton_7.setVisible(False)
        try:
            self.sel_label_24.setVisible(True)
            self.sel_label_24.setText(_translate("self.form", self.dat.df.Name[5]))
            self.sel_label_19.setVisible(True)
            self.sel_label_19.setText(_translate("self.form", self.dat.df.Ingredients[5]+","+self.dat.df.Boxes[5]))
            self.sel_pushButton_10.setVisible(True)
            self.sel_pushButton_10.setText(_translate("self.form", "add queue"))
        except:
            self.sel_label_24.setVisible(False)
            self.sel_label_19.setVisible(False)
            self.sel_pushButton_10.setVisible(False)
        try:
            self.sel_label_20.setVisible(True)
            self.sel_label_20.setText(_translate("self.form", self.dat.df.Name[6]))
            self.sel_label_38.setVisible(True)
            self.sel_label_38.setText(_translate("self.form", self.dat.df.Ingredients[6]+","+self.dat.df.Boxes[6]))
            self.sel_pushButton_11.setVisible(True)
            self.sel_pushButton_11.setText(_translate("self.form", "add queue"))
        except:
            self.sel_label_20.setVisible(False)
            self.sel_label_38.setVisible(False)
            self.sel_pushButton_11.setVisible(False)
        try:
            self.sel_label_25.setVisible(True)
            self.sel_label_25.setText(_translate("self.form", self.dat.df.Name[7]))
            self.sel_label_37.setVisible(True)
            self.sel_label_37.setText(_translate("self.form", self.dat.df.Ingredients[7]+","+self.dat.df.Boxes[7]))
            self.sel_pushButton_12.setVisible(True)
            self.sel_pushButton_12.setText(_translate("self.form", "add queue"))
        except:
            self.sel_label_25.setVisible(False)
            self.sel_label_37.setVisible(False)
            self.sel_pushButton_12.setVisible(False)
        try:
            self.sel_label_41.setVisible(True)
            self.sel_label_41.setText(_translate("self.form", self.dat.df.Name[8]))
            self.sel_label_30.setVisible(True)
            self.sel_label_30.setText(_translate("self.form", self.dat.df.Ingredients[8]+","+self.dat.df.Boxes[8]))
            self.sel_pushButton_13.setVisible(True)
            self.sel_pushButton_13.setText(_translate("self.form", "add queue"))
        except:
            self.sel_label_41.setVisible(False)
            self.sel_label_30.setVisible(False)
            self.sel_pushButton_13.setVisible(False)

    def sel_add_to_queue(self, id, functions):
        if self.trash:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Are you sure you want to delete this recipe?")
            # msg.setInformativeText('More information')
            msg.setWindowTitle("Confirm dialog")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            ret = msg.exec_()
            if (ret == QMessageBox.Yes):
                self.dat.remove_recipe(id)
                [x.setVisible(False) for x in functions]
        else:
            self.dat.add_to_queue(id)
            self.dat.__init__()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("- "+str(("\n- ").join([self.dat.df.Name[list(self.dat.df.ID).index(x)] for x in self.dat.queue.values()])))
            # msg.setInformativeText('More information')
            msg.setWindowTitle("Actual queue")
            ret = msg.exec_()

    def sel_clear_queue(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Are you sure you want to clean queue?")
        # msg.setInformativeText('More information')
        msg.setWindowTitle("Confirm dialog")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msg.exec_()
        if (ret == QMessageBox.Yes):
            self.dat.clean_queue()
            self.dat.__init__()

    def sel_prepare(self):
        msg = QMessageBox()
        # create Label
        msg.setIconPixmap(QPixmap('assets/wait.gif').scaledToWidth(100))
        icon_label = msg.findChild(QLabel, "qt_msgboxex_icon_label")
        movie = QMovie('assets/wait.gif')
        # avoid garbage collector
        setattr(msg, 'icon_label', movie)
        icon_label.setMovie(movie)
        movie.start()

        msg.setText("Preparing your beverage...")
        msg.setWindowTitle(" ")
        msg.setModal(False)
        # msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    ui.select_form()
    Form.show()
    sys.exit(app.exec_())

