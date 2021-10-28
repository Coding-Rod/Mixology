# -*- coding: utf-8 -*-

# self.form implementation generated from reading ui file 'First_Page.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

# TODO: Index


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def __init__(self, Form):
        self.form = Form
        self.form.setObjectName("form")
        self.form.resize(800, 380)
        self.form.setStyleSheet("background-color: rgb(236, 236, 236);\n")
        self.state = 0
        self.state_machine(0)

    #region home_screen
    def main(self): 
        self.pushButton = QtWidgets.QPushButton(self.form)
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
        self.pushButton.clicked.connect(lambda: self.state_machine(1))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.form)
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
        self.pushButton_5 = QtWidgets.QPushButton(self.form)
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
        self.pushButton_5.clicked.connect(lambda: self.state_machine(2))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.form)
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
        self.pushButton_6.clicked.connect(lambda: self.state_machine(3))
        self.pushButton_6.setObjectName("pushButton_6")
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
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle(_translate("self.form", "self.form"))
        self.pushButton_4.setText(_translate("self.form", "X"))
        self.pushButton_4.clicked.connect(lambda: self.form.close())
        self.label.setText(_translate("self.form", "    MIXOLOGY"))

    def create_form(self):
        # TODO: change to Create window
        print("Create window")
    
    def calibrate_form(self):
        # TODO: change to Calibrate window
        print("Calibrate window")

    def select_form(self):
        # TODO: change to Select window
        print("Select window")

    #endregion home_screen
    
    def state_machine(self,state):
        self.state = state
        print(self.state)
        if self.state == 0:
            self.main()
        if self.state == 1:
            self.create_form()
        if self.state == 2:
            self.calibrate_form()
        if self.state == 3:
            self.select_form()

        #region visible
        #region main
        self.pushButton.setVisible(self.state == 0)
        self.pushButton_4 .setVisible(self.state == 0)
        self.pushButton_5.setVisible(self.state == 0)
        self.pushButton_6.setVisible(self.state == 0)
        self.label.setVisible(self.state == 0)
        #endregion main
        #region create

        #endregion create
        #region calibrate

        #endregion calibrate
        #region select

        #endregion select
        #endregion visible

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())

