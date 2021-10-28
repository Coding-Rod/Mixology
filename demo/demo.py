# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Create.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QMessageBox

from apis.data import Data

class Main(object):
    def setupUi(self, Form):
        self.dat = Data()
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(800, 1000)
        Form.setStyleSheet("background-color: rgb(238, 238, 238);")
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

        #region sliders
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 80, 100, 50))
        self.label.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 100, 50))
        self.label_3.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 100, 50))
        self.label_4.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 100, 50))
        self.label_5.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 360, 100, 50))
        self.label_6.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 430, 100, 50))
        self.label_7.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 500, 100, 50))
        self.label_8.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 570, 100, 50))
        self.label_9.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(30, 640, 100, 50))
        self.label_10.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(30, 730, 100, 50))
        self.label_11.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_11.setObjectName("label_11")

        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(160, 100, 160, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(160, 170, 160, 16))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(Form)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(160, 240, 160, 16))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_4 = QtWidgets.QSlider(Form)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(160, 310, 160, 16))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_5 = QtWidgets.QSlider(Form)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(160, 380, 160, 16))
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.horizontalSlider_6 = QtWidgets.QSlider(Form)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(160, 450, 160, 16))
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.horizontalSlider_7 = QtWidgets.QSlider(Form)
        self.horizontalSlider_7.setGeometry(QtCore.QRect(160, 520, 160, 16))
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.horizontalSlider_8 = QtWidgets.QSlider(Form)
        self.horizontalSlider_8.setGeometry(QtCore.QRect(160, 590, 160, 16))
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.horizontalSlider_9 = QtWidgets.QSlider(Form)
        self.horizontalSlider_9.setGeometry(QtCore.QRect(160, 660, 160, 16))
        self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_9.setObjectName("horizontalSlider_9")
        self.horizontalSlider_10 = QtWidgets.QSlider(Form)
        self.horizontalSlider_10.setGeometry(QtCore.QRect(160, 730, 160, 16))
        self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_10.setObjectName("horizontalSlider_10")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(360, 30, 170, 25))
        self.lineEdit.setStyleSheet("border-radius: 10px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(260, 25, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: #E09825;\n"
"color: #FFFFFF;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setLineWidth(1)
        self.textEdit.setObjectName("textEdit")

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

        #endregion sliders

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
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(530, 80, 150, 50))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(530, 150, 150, 50))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(530, 220, 150, 50))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(530, 290, 150, 50))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(530, 360, 150, 50))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(530, 430, 150, 50))
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalSlider_11 = QtWidgets.QSlider(Form)
        self.horizontalSlider_11.setGeometry(QtCore.QRect(590, 540, 80, 16))
        self.horizontalSlider_11.setMaximum(1)
        self.horizontalSlider_11.setSliderPosition(0)
        self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_11.setObjectName("horizontalSlider_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(500, 540, 67, 17))
        self.label_12.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 300, 65, 65))
        self.pushButton.setIcon(QIcon('assets/back.png'))
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 300, 65, 65))
        self.pushButton_2.setIcon(QIcon('assets/check2.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.showMessage)
        # self.pushButton.clicked.connect(lambda: self.pushButton_2.setVisible(False))
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_7.clicked.connect(lambda: sys.exit(0))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle("Mixology")

        self.horizontalSlider.setValue(self.dat.bottles['1'][1])
        self.horizontalSlider_2.setValue(self.dat.bottles['2'][1])
        self.horizontalSlider_3.setValue(self.dat.bottles['3'][1])
        self.horizontalSlider_4.setValue(self.dat.bottles['4'][1])
        self.horizontalSlider_5.setValue(self.dat.bottles['5'][1])
        self.horizontalSlider_6.setValue(self.dat.bottles['6'][1])
        self.horizontalSlider_7.setValue(self.dat.bottles['7'][1])
        self.horizontalSlider_8.setValue(self.dat.bottles['8'][1])
        self.horizontalSlider_9.setValue(self.dat.bottles['9'][1])
        self.horizontalSlider_10.setValue(self.dat.bottles['10'][1])

        self.label_2.setText(_translate("Form", "    CREATE"))
        self.label.setText(_translate("Form", self.dat.bottles['1'][0])+"\n"+str(self.dat.bottles['1'][1]))
        self.label_3.setText(_translate("Form", self.dat.bottles['2'][0])+"\n"+str(self.dat.bottles['2'][1]))
        self.label_4.setText(_translate("Form", self.dat.bottles['3'][0])+"\n"+str(self.dat.bottles['3'][1]))
        self.label_5.setText(_translate("Form", self.dat.bottles['4'][0])+"\n"+str(self.dat.bottles['4'][1]))
        self.label_6.setText(_translate("Form", self.dat.bottles['5'][0])+"\n"+str(self.dat.bottles['5'][1]))
        self.label_7.setText(_translate("Form", self.dat.bottles['6'][0])+"\n"+str(self.dat.bottles['6'][1]))
        self.label_8.setText(_translate("Form", self.dat.bottles['7'][0])+"\n"+str(self.dat.bottles['7'][1]))
        self.label_9.setText(_translate("Form", self.dat.bottles['8'][0])+"\n"+str(self.dat.bottles['8'][1]))
        self.label_10.setText(_translate("Form", self.dat.bottles['9'][0])+"\n"+str(self.dat.bottles['9'][1]))
        self.label_11.setText(_translate("Form", self.dat.bottles['10'][0])+"\n"+str(self.dat.bottles['10'][1]))
        self.pushButton_7.setText(_translate("Form", "X"))
        self.checkBox.setText(_translate("Form", self.dat.boxes['1']))
        self.checkBox_2.setText(_translate("Form", self.dat.boxes['2']))
        self.checkBox_3.setText(_translate("Form", self.dat.boxes['3']))
        self.checkBox_4.setText(_translate("Form", self.dat.boxes['4']))
        self.checkBox_5.setText(_translate("Form", self.dat.boxes['5']))
        self.checkBox_6.setText(_translate("Form", self.dat.boxes['6']))
        self.label_12.setText(_translate("Form", "MIX"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"margin 0; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Name</span></p></body></html>"))

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
        self.label.setText(_translate("Form", self.dat.bottles['1'][0])+"\n"+str(self.horizontalSlider.value()))
        self.label_3.setText(_translate("Form", self.dat.bottles['2'][0])+"\n"+str(self.horizontalSlider_2.value()))
        self.label_4.setText(_translate("Form", self.dat.bottles['3'][0])+"\n"+str(self.horizontalSlider_3.value()))
        self.label_5.setText(_translate("Form", self.dat.bottles['4'][0])+"\n"+str(self.horizontalSlider_4.value()))
        self.label_6.setText(_translate("Form", self.dat.bottles['5'][0])+"\n"+str(self.horizontalSlider_5.value()))
        self.label_7.setText(_translate("Form", self.dat.bottles['6'][0])+"\n"+str(self.horizontalSlider_6.value()))
        self.label_8.setText(_translate("Form", self.dat.bottles['7'][0])+"\n"+str(self.horizontalSlider_7.value()))
        self.label_9.setText(_translate("Form", self.dat.bottles['8'][0])+"\n"+str(self.horizontalSlider_8.value()))
        self.label_10.setText(_translate("Form", self.dat.bottles['9'][0])+"\n"+str(self.horizontalSlider_9.value()))
        self.label_11.setText(_translate("Form", self.dat.bottles['10'][0])+"\n"+str(self.horizontalSlider_10.value()))

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
        print("Saved")

    def showMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('More information')
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Main()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

