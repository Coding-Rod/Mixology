# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/Select.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

# TODO: Give functionality
# TODO: Index
# TODO: Change labels
# TODO: Change colors
# TODO: Constructor

from PyQt5 import QtCore, QtGui, QtWidgets
from apis.data import Data
# from apis.control import Control
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def select(self, Form):
        self.form = Form
        self.dat = Data()
        Form.setObjectName("Form")
        Form.resize(800, 380)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(730, 30, 41, 31))
        self.pushButton_8.setStyleSheet("background: #AA0000;\n"
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
"border-radius: 10px;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"\n"
"color: #FFFFFF;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: sys.exit(0))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 300, 65, 65))
        self.pushButton.setStyleSheet("border-image: url(:/back/assets/back.png);\n"
"\n"
"border-radius:30px")
        self.pushButton.setText("")
        self.pushButton.setIcon(QIcon('assets/back.png'))
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet("border-radius:30px\noverflow:hidden;")
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
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
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
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"\n"
"")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 0, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 1, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_33.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 2, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 2, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
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
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 3, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 4, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
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
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 5, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_19.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 5, 3, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_38.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 6, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_37.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 7, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 6, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_30.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: #FFFFFF;")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 8, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 7, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_41.setEnabled(True)
        self.label_41.setMinimumSize(QtCore.QSize(0, 40))
        self.label_41.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_41.setBaseSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 8, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.add_to_queue(1))

        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.add_to_queue(2))

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.add_to_queue(3))

        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.add_to_queue(4))

        self.gridLayout.addWidget(self.pushButton_6, 3, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.add_to_queue(5))

        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda: self.add_to_queue(6))

        self.gridLayout.addWidget(self.pushButton_10, 5, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda: self.add_to_queue(7))

        self.gridLayout.addWidget(self.pushButton_11, 6, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(lambda: self.add_to_queue(8))

        self.gridLayout.addWidget(self.pushButton_12, 7, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(lambda: self.add_to_queue(9))

        self.gridLayout.addWidget(self.pushButton_13, 8, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 300, 65, 65))
        self.pushButton_2.setStyleSheet("border-image: url(:/check/assets/check2.png);\n"
"\n"
"border-radius:30px")
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(QIcon('assets/play.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setText("Clean queue")
        self.pushButton_14.clicked.connect(self.clear_queue)
        self.pushButton_14.setGeometry(QtCore.QRect(350, 300, 100, 65))
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(650, 300, 65, 65))
        self.pushButton_15.setStyleSheet("border-image: url(:/check/assets/check2.png);\n"
"\n"
"border-radius:30px")
        self.pushButton_15.setText("")
        self.pushButton_15.setIcon(QIcon('assets/trash2.png'))
        self.pushButton_15.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_15.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.pushButton_15.setObjectName("pushButton_15")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def toggleTrashcan(self):
        # TODO: toggleTrashcan
        pass

    def deleteRecipe(self,id):
        # TODO: deleteRecipe
        pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_8.setText(_translate("Form", "X"))
        self.label_18.setText(_translate("Form", "    SELECT"))
        self.pushButton_9.setText(_translate("Form", "X"))
        
        try:
            self.label_36.setVisible(True)
            self.label_36.setText(_translate("Form", self.dat.df.Name[0]))
            self.label_7.setVisible(True)
            self.label_7.setText(_translate("Form", self.dat.df.Ingredients[0]+","+self.dat.df.Boxes[0]))
            self.pushButton_3.setVisible(True)
            self.pushButton_3.setText(_translate("Form", "add queue"))
        except:
            self.label_36.setVisible(False)
            self.label_7.setVisible(False)
            self.pushButton_3.setVisible(False)
        try:
            self.label_32.setVisible(True)
            self.label_32.setText(_translate("Form", self.dat.df.Name[1]))
            self.label_16.setVisible(True)
            self.label_16.setText(_translate("Form", self.dat.df.Ingredients[1]+","+self.dat.df.Boxes[1]))
            self.pushButton_4.setVisible(True)
            self.pushButton_4.setText(_translate("Form", "add queue"))
        except:
            self.label_32.setVisible(False)
            self.label_16.setVisible(False)
            self.pushButton_4.setVisible(False)
        try:
            self.label_22.setVisible(True)
            self.label_22.setText(_translate("Form", self.dat.df.Name[2]))
            self.label_33.setVisible(True)
            self.label_33.setText(_translate("Form", self.dat.df.Ingredients[2]+","+self.dat.df.Boxes[2]))
            self.pushButton_5.setVisible(True)
            self.pushButton_5.setText(_translate("Form", "add queue"))
        except:
            self.label_22.setVisible(False)
            self.label_33.setVisible(False)
            self.pushButton_5.setVisible(False)
        try:
            self.label_40.setVisible(True)
            self.label_40.setText(_translate("Form", self.dat.df.Name[3]))
            self.label_23.setVisible(True)
            self.label_23.setText(_translate("Form", self.dat.df.Ingredients[3]+","+self.dat.df.Boxes[3]))
            self.pushButton_6.setVisible(True)
            self.pushButton_6.setText(_translate("Form", "add queue"))
        except:
            self.label_40.setVisible(False)
            self.label_23.setVisible(False)
            self.pushButton_6.setVisible(False)
        try:
            self.label_31.setVisible(True)
            self.label_31.setText(_translate("Form", self.dat.df.Name[4]))
            self.label_28.setVisible(True)
            self.label_28.setText(_translate("Form", self.dat.df.Ingredients[4]+","+self.dat.df.Boxes[4]))
            self.pushButton_7.setVisible(True)
            self.pushButton_7.setText(_translate("Form", "add queue"))
        except:
            self.label_31.setVisible(False)
            self.label_28.setVisible(False)
            self.pushButton_7.setVisible(False)
        try:
            self.label_24.setVisible(True)
            self.label_24.setText(_translate("Form", self.dat.df.Name[5]))
            self.label_19.setVisible(True)
            self.label_19.setText(_translate("Form", self.dat.df.Ingredients[5]+","+self.dat.df.Boxes[5]))
            self.pushButton_10.setVisible(True)
            self.pushButton_10.setText(_translate("Form", "add queue"))
        except:
            self.label_24.setVisible(False)
            self.label_19.setVisible(False)
            self.pushButton_10.setVisible(False)
        try:
            self.label_20.setVisible(True)
            self.label_20.setText(_translate("Form", self.dat.df.Name[6]))
            self.label_38.setVisible(True)
            self.label_38.setText(_translate("Form", self.dat.df.Ingredients[6]+","+self.dat.df.Boxes[6]))
            self.pushButton_11.setVisible(True)
            self.pushButton_11.setText(_translate("Form", "add queue"))
        except:
            self.label_20.setVisible(False)
            self.label_38.setVisible(False)
            self.pushButton_11.setVisible(False)
        try:
            self.label_25.setVisible(True)
            self.label_25.setText(_translate("Form", self.dat.df.Name[7]))
            self.label_37.setVisible(True)
            self.label_37.setText(_translate("Form", self.dat.df.Ingredients[7]+","+self.dat.df.Boxes[7]))
            self.pushButton_12.setVisible(True)
            self.pushButton_12.setText(_translate("Form", "add queue"))
        except:
            self.label_25.setVisible(False)
            self.label_37.setVisible(False)
            self.pushButton_12.setVisible(False)
        try:
            self.label_41.setVisible(True)
            self.label_41.setText(_translate("Form", self.dat.df.Name[8]))
            self.label_30.setVisible(True)
            self.label_30.setText(_translate("Form", self.dat.df.Ingredients[8]+","+self.dat.df.Boxes[8]))
            self.pushButton_13.setVisible(True)
            self.pushButton_13.setText(_translate("Form", "add queue"))
        except:
            self.label_41.setVisible(False)
            self.label_30.setVisible(False)
            self.pushButton_13.setVisible(False)

    def add_to_queue(self, id):
        self.dat.add_to_queue(id)
        self.dat.__init__()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("- "+str(("\n- ").join([self.dat.df.Name[list(self.dat.df.ID).index(x)] for x in self.dat.queue.values()])))
        # msg.setInformativeText('More information')
        msg.setWindowTitle("Actual queue")
        ret = msg.exec_()

    def clear_queue(self):
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

    def prepare(self):
        # TODO: Show progress bar
        # TODO: get queue
        # TODO: verify and validate queue
        # TODO: control pumps
        # TODO: control leds
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.select(Form)
    Form.show()
    sys.exit(app.exec_())

