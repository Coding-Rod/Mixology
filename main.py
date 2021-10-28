# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'First_Page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

# TODO: Index
# TODO: Create State machine

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def main(self, Form):
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(800, 380)
        Form.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 180, 150, 60))
        self.pushButton.setStyleSheet("background: #AA0000;\n"
"border: 0.5px solid rgba(255, 255, 255, 0.48);\n"
"border-radius: 25px;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"\n"
"color: #FFFFFF;\n"
"border-image: url(/home/osvaldo/Documentos/Mixology/Proxlight_Designer_Export/img2.png)")
        self.pushButton.setText("Create")
        self.pushButton.clicked.connect(self.create_form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 20, 41, 31))
        self.pushButton_4.setStyleSheet("background: #AA0000;\n"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 180, 150, 60))
        self.pushButton_5.setStyleSheet("background: #AA0000;\n"
"border: 0.5px solid rgba(255, 255, 255, 0.48);\n"
"border-radius: 25px;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"\n"
"color: #FFFFFF;\n"
"border-image: url(/home/osvaldo/Documentos/Mixology/Proxlight_Designer_Export/img1.png)")
        self.pushButton_5.setText("Calibrate")
        self.pushButton_5.clicked.connect(self.calibrate_form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 180, 150, 60))
        self.pushButton_6.setStyleSheet("background: #AA0000;\n"
"border: 0.5px solid rgba(255, 255, 255, 0.48);\n"
"border-radius: 25px;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"\n"
"color: #FFFFFF;\n"
"border-image: url(/home/osvaldo/Documentos/Mixology/Proxlight_Designer_Export/img0.png)")
        self.pushButton_6.setText("Select")
        self.pushButton_6.clicked.connect(self.select_form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(Form)
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
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_4.setText(_translate("Form", "X"))
        self.pushButton_4.clicked.connect(lambda: self.form.close())
        self.label.setText(_translate("Form", "    MIXOLOGY"))

    def create_form(self):
        # TODO: change to Create window
        print("Create window")
    
    def calibrate_form(self):
        # TODO: change to Calibrate window
        print("Calibrate window")

    def select_form(self):
        # TODO: change to Select window
        print("Select window")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

