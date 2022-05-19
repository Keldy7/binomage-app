

from PyQt5 import QtSql
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from my_interface import Ui_MainWindow
#import addDialog
#from PyQt5.QCoreApplication import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys


conn = QSqlDatabase.addDatabase("QSQLITE")
conn.setDatabaseName("Bino_Ap.db")
#app = QApplication(sys.argv)   
if not conn.open():
    QMessageBox.critical(None,"App Name - Error","Database Error:%s" % conn.lastError().databaseText(),)
else:
    print("salut")
#sys.exit(1)

req = QSqlQuery()
req.exec_("CREATE TABLE IF NOT EXISTS PARRAIN_MARRAINE(Matricule TEXT PRIMARY KEY, Nom TEXT, Prenom TEXT, Classe TEXT, Homme TEXT, Femme TEXT);")
req.exec_("CREATE TABLE IF NOT EXISTS FILEULE(Id_fileule TEXT PRIMARY KEY, Nom_F TEXT, Prenom_F TEXT, Classe_F TEXT, Homme_F TEXT, Femme_F TEXT, Matricule TEXT, FOREIGN KEY(Matricule) REFERENCES PARRAIN_MARRAINE(Matricule));")
req.first()


class les_parrains(Ui_MainWindow): #gère les données d'un parrain
    def __init__(self):
        super (les_parrains,self).__init__()
        self.setupUi(self)
        self.ui.valider.clicked.connect(lambda:self.ajout_info())
        #hpar.pushButtonpar.clicked.connect(ajout_parrain)
        
    '''def Init_Ui(self):
        
        self.show()'''
    def ajout_info(self):
          
        mat = self.lineEdit_mat.text()
        name = self.lineEdit_nom.text()
        pre = self.lineEdit_pre.text()
        clas = self.lineEdit_class.text()
        boy = self.homme.text()
        girl = self.femme.text()
    
        cur = QtSql.QSqlQuery()
        cur.exec_("INSERT INTO PARRAIN_MARRAINE (Matricule,Nom,Prenom,Classe,Homme,Femme) VALUES (?,?,?,?,?,?);",(mat,name,pre,clas,boy,girl))         #le joueur est désormais inscrit
        cur.first()
        print(mat,name,pre,clas,boy,girl)



'''win = QLabel("Connection successfuuly")
win.setWindowTitle ("App")
win.resize(200,200)
win.show()
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
sys.exit(app.exec())'''
    
  
