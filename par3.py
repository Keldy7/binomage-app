# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Aude KOUASSY\venv\Projet_Vac\part3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.lineEdit_mat = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_mat.setGeometry(QtCore.QRect(20, 20, 341, 20))
        self.lineEdit_mat.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:rgb(204, 31, 167);\n"
"border-bottom:1px solid rgb(204, 31, 167);\n"
"}")
        self.lineEdit_mat.setText("")
        self.lineEdit_mat.setCursorPosition(0)
        self.lineEdit_mat.setObjectName("lineEdit_mat")
        self.lineEdit_nom = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_nom.setGeometry(QtCore.QRect(20, 60, 341, 20))
        self.lineEdit_nom.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color: rgb(136, 67, 255);\n"
"border-bottom:1px solid rgb(136, 67, 255);\n"
"}")
        self.lineEdit_nom.setText("")
        self.lineEdit_nom.setCursorPosition(0)
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.lineEdit_pre = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_pre.setGeometry(QtCore.QRect(20, 100, 341, 20))
        self.lineEdit_pre.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:rgb(204, 31, 167);\n"
"border-bottom:1px solid rgb(204, 31, 167);\n"
"}")
        self.lineEdit_pre.setText("")
        self.lineEdit_pre.setCursorPosition(0)
        self.lineEdit_pre.setClearButtonEnabled(False)
        self.lineEdit_pre.setObjectName("lineEdit_pre")
        self.lineEdit_class = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_class.setGeometry(QtCore.QRect(20, 140, 341, 20))
        self.lineEdit_class.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:rgb(136, 67, 255);\n"
"border-bottom:1px solid rgb(136, 67, 255);\n"
"}")
        self.lineEdit_class.setText("")
        self.lineEdit_class.setCursorPosition(0)
        self.lineEdit_class.setObjectName("lineEdit_class")
        self.nom_partie = QtWidgets.QLabel(self.frame)
        self.nom_partie.setGeometry(QtCore.QRect(500, 90, 211, 31))
        self.nom_partie.setStyleSheet("background-color: rgb(244, 217, 255);\n"
"font: 20pt \"TAKE CUTE\";\n"
"border-radius:10px;")
        self.nom_partie.setObjectName("nom_partie")
        self.valider = QtWidgets.QPushButton(self.frame)
        self.valider.setGeometry(QtCore.QRect(560, 380, 111, 23))
        self.valider.setStyleSheet("QPushButton{\n"
"color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(106, 0, 91, 255), stop:1 rgba(100, 60, 255, 255));\n"
"border-radius: 10px;\n"
"background-color:white;\n"
"font:10pt \"Verdana Pro Semibold\";\n"
"box-shadow:11px 8px 8px #666666;\n"
"padding:18px;\n"
"-moz-box-shadow:11px 8px 8px #666666;\n"
"-webkit-box-shadow:11px  8px 8px #666666;\n"
"}\n"
"QPushButton:hover{\n"
"border-top-color:#084870;\n"
"background:white;\n"
"color:#c910c9;\n"
"}\n"
"QPushButton:active{\n"
"border-top-color:#409ad6;\n"
"background:white;\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/C:/Users/Aude KOUASSY/Desktop/icones/cooche.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.valider.setIcon(icon)
        self.valider.setObjectName("valider")
        self.home = QtWidgets.QPushButton(self.frame)
        self.home.setGeometry(QtCore.QRect(160, 10, 41, 23))
        self.home.setStyleSheet("background:transparent;")
        self.home.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icones/accueil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home.setIcon(icon1)
        self.home.setObjectName("home")
        self.sortie = QtWidgets.QPushButton(self.frame)
        self.sortie.setGeometry(QtCore.QRect(190, 10, 31, 23))
        self.sortie.setStyleSheet("background:transparent;")
        self.sortie.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icones/effacer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sortie.setIcon(icon2)
        self.sortie.setObjectName("sortie")
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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 291, 61))
        self.label_2.setStyleSheet("\n"
"font: 24pt \"Smile Candy\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Modern GUI v-2021"))
        self.app_name.setText(_translate("Dialog", "Bino\'App"))
        self.lineEdit_mat.setPlaceholderText(_translate("Dialog", "Matricule INP"))
        self.lineEdit_nom.setPlaceholderText(_translate("Dialog", "Nom"))
        self.lineEdit_pre.setPlaceholderText(_translate("Dialog", "Prénom"))
        self.lineEdit_class.setPlaceholderText(_translate("Dialog", "Classe"))
        self.nom_partie.setText(_translate("Dialog", "FILLEUL/FILLEULE"))
        self.valider.setText(_translate("Dialog", "Valider"))
        self.label_2.setText(_translate("Dialog", "ENREGISTREMENT"))
import photos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
