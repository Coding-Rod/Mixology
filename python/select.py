# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/Select.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 380)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(730, 30, 41, 31))
        self.pushButton_8.setStyleSheet("background: #AA0000;\n"
"border: 0.5px solid rgba(255, 255, 255, 0.48);\n"
"box-sizing: border-box;\n"
"border-radius: 10px;\n"
"transform: matrix(1, 0, 0, 1, 0, 0);\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"\n"
"color: #FFFFFF;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 800, 74))
        self.label_18.setStyleSheet("font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 36px;\n"
"line-height: 42px;\n"
"\n"
"color: #FFFFFF;\n"
"background-color: #E09825;")
        self.label_18.setObjectName("label_18")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(730, 20, 41, 31))
        self.pushButton_9.setStyleSheet("background: #AA0000;\n"
"border: 0.5px solid rgba(255, 255, 255, 0.48);\n"
"box-sizing: border-box;\n"
"border-radius: 10px;\n"
"transform: matrix(1, 0, 0, 1, 0, 0);\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"\n"
"color: #FFFFFF;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 300, 65, 65))
        self.pushButton.setStyleSheet("border-image: url(:/back/assets/back.png);\n"
"\n"
"border-radius:30px")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(70, 80, 651, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -228, 635, 426))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 3, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_36.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"\n"
"")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 7, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 6, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_33.setFont(font)
        self.label_33.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_33.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 6, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_23.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 3, 3, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_40.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 8, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 5, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_28.setFont(font)
        self.label_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_28.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 4, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_19.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 3, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_38.setFont(font)
        self.label_38.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_38.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 7, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_37.setFont(font)
        self.label_37.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_37.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 8, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_30.setFont(font)
        self.label_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_30.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 5, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 4, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_41.setEnabled(True)
        self.label_41.setMinimumSize(QtCore.QSize(0, 40))
        self.label_41.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_41.setBaseSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 5, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 6, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 7, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 8, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 310, 65, 65))
        self.pushButton_2.setStyleSheet("border-image: url(:/check/assets/check2.png);\n"
"\n"
"border-radius:30px")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_8.setText(_translate("Form", "X"))
        self.label_18.setText(_translate("Form", "    SELECT"))
        self.pushButton_9.setText(_translate("Form", "X"))
        self.label_7.setText(_translate("Form", "Vainilla, choclate, leche, coco, agua"))
        self.label_16.setText(_translate("Form", "chocolate"))
        self.label_36.setText(_translate("Form", "1. chocolate"))
        self.label_32.setText(_translate("Form", "2. vainilla"))
        self.label_33.setText(_translate("Form", "Vainilla"))
        self.label_22.setText(_translate("Form", "1. chocolate"))
        self.label_23.setText(_translate("Form", "chocolate"))
        self.label_40.setText(_translate("Form", "2. vainilla"))
        self.label_31.setText(_translate("Form", "1. chocolate"))
        self.label_28.setText(_translate("Form", "Vainilla"))
        self.label_24.setText(_translate("Form", "1. chocolate"))
        self.label_19.setText(_translate("Form", "Vainilla"))
        self.label_38.setText(_translate("Form", "chocolate"))
        self.label_37.setText(_translate("Form", "Vainilla"))
        self.label_20.setText(_translate("Form", "2. vainilla"))
        self.label_30.setText(_translate("Form", "chocolate"))
        self.label_25.setText(_translate("Form", "2. vainilla"))
        self.label_41.setText(_translate("Form", "2. vainilla"))
        self.pushButton_3.setText(_translate("Form", "add queue"))
        self.pushButton_4.setText(_translate("Form", "add queue"))
        self.pushButton_5.setText(_translate("Form", "add queue"))
        self.pushButton_6.setText(_translate("Form", "add queue"))
        self.pushButton_7.setText(_translate("Form", "add queue"))
        self.pushButton_10.setText(_translate("Form", "add queue"))
        self.pushButton_11.setText(_translate("Form", "add queue"))
        self.pushButton_12.setText(_translate("Form", "add queue"))
        self.pushButton_13.setText(_translate("Form", "add queue"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

