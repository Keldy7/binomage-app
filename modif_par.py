# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Aude KOUASSY\venv\Projet_Vac\modif_par.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import photos_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(956, 662)
        
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(80, 110, 841, 451))
        self.frame.setStyleSheet("QWidget#frame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(116, 0, 81, 255), stop:1 rgba(102, 64, 255, 255));\n"
"border-radius:40px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 400, 121, 20))
        self.label.setStyleSheet("\n"
"font: 10pt \"Bradley Hand ITC\";\n"
"text-decoration: underline;")
        self.label.setObjectName("label")
        
        self.app_name = QtWidgets.QLabel(self.frame)
        self.app_name.setGeometry(QtCore.QRect(90, 30, 231, 61))
        self.app_name.setStyleSheet("font: 36pt \"Forte\";")
        self.app_name.setObjectName("app_name")
        
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(409, 110, 401, 221))
        self.frame_2.setStyleSheet("background-color:white;\n"
"border-radius:14px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 341, 20))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:rgb(204, 31, 167);\n"
"border-bottom:1px solid rgb(204, 31, 167);\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        
        self.message = QtWidgets.QLabel(self.frame_2)
        self.message.setGeometry(QtCore.QRect(10, 110, 361, 20))
        self.message.setStyleSheet("background-color: None;\n"
"font: 87 italic 9pt \"Segoe UI\";")
        self.message.setText("")
        self.message.setObjectName("message")
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(500, 90, 211, 31))
        self.label_2.setStyleSheet("background-color: rgb(244, 217, 255);\n"
"font: 20pt \"TAKE CUTE\";\n"
"border-radius:10px;")
        self.label_2.setObjectName("label_2")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 10, 31, 23))
        self.pushButton_2.setStyleSheet("background:transparent;")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/effacer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 10, 31, 23))
        self.pushButton_4.setStyleSheet("background:transparent;")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icones/accueil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.valider = QtWidgets.QPushButton(self.frame)
        self.valider.setGeometry(QtCore.QRect(560, 380, 111, 23))
        self.valider.setStyleSheet("QPushButton{\n"
"color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(106, 0, 91, 255), stop:1 rgba(100, 60, 255, 255));\n"
"border-radius: 10px;\n"
"background-color:white;\n"
"font:10pt \"Verdana Pro Semibold\";\n"
"padding:18px;\n"
"}\n"
"QPushButton:hover{\n"
"border-top-color:#084870;\n"
"background:white;\n"
"color:#c910c9;\n"
"}\n"
"QPushButton:active{\n"
"border-top-color:#409ad6;\n"
"background:white;\n"
"}"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/C:/Users/Aude KOUASSY/Desktop/icones/cooche.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.valider.setIcon(icon2)
        self.valider.setObjectName("valider")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(770, 10, 31, 23))
        self.pushButton_7.setStyleSheet("background:transparent;")
        self.pushButton_7.setText("")        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/C:/Users/Aude KOUASSY/Desktop/icones/effacer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setObjectName("pushButton_7")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(740, 10, 31, 23))
        self.pushButton_6.setStyleSheet("background:transparent;")
        self.pushButton_6.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/C:/Users/Aude KOUASSY/Desktop/icones/accueil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 200, 291, 61))
        self.label_3.setStyleSheet("\n"
"font: 24pt \"Smile Candy\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bino\'App - Modification Parrain"))
        Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setText(_translate("Dialog", "Modern GUI v-2021"))
        self.app_name.setText(_translate("Dialog", "Bino\'App"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Matricule à modifier"))
        self.label_2.setText(_translate("Dialog", "PARRAIN/MARRAINE"))
        self.valider.setText(_translate("Dialog", "Valider"))
        self.label_3.setText(_translate("Dialog", "MODIFICATION"))
