# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Select.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 380)
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
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 65, 65))
        self.pushButton.setStyleSheet("border-image: url(:/prefijoNuevo/back.png);\n"
"border-radius:30px")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 380, 65, 65))
        self.pushButton_2.setStyleSheet("border-image: url(:/thrash/thrash2.png);\n"
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

