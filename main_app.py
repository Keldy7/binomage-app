

from PyQt5 import QtCore, QtGui, QtWidgets
from my_interface import Ui_MainWindow


import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
