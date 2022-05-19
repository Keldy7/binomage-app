

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from my_interface import Ui_MainWindow
from Pyqt5.uic import loadUi
#import addDialog
#from editDialog import Ui_Dialog
import sqlite3
import random

conn = sqlite3.connect('Binoap.db') #connection à ma bdd

cur = conn.cursor() #creation d'un curseur

#creation de deux tables dans ma bd
cur.execute("CREATE TABLE IF NOT EXISTS PARRAIN_MARRAINE(Matricule TEXT PRIMARY KEY, Nom TEXT, Prenom TEXT, Classe TEXT, Homme TEXT, Femme TEXT);") #création de la table  avec ses colonnes
conn.commit()
cur.execute("CREATE TABLE IF NOT EXISTS FILEULE(Id_fileule TEXT PRIMARY KEY, Nom_F TEXT, Prenom_F TEXT, Classe_F TEXT, Homme_F TEXT, Femme_F TEXT, Matricule TEXT, FOREIGN KEY(Matricule) REFERENCES PARRAIN_MARRAINE(Matricule));") #création de la table  avec ses colonnes
conn.commit()
conn.close()  #fermer ma connection

class les_parrains(QDialog): #gère les données d'un parrain
    
    def __init__(self, Id, Nom, Prenom, Classe, Filiere, Sexe):
        super(les_parrains,self).__init__()
        loadUi("part2.ui",self)
        self.mat = Id
        self.nom = Nom
        self.prenom = Prenom 
        self.classe = Classe
        self.filiere = Filiere
        self.sexe = Sexe
        self.valider.clicked.connect(self.ajout_info)
        
    '''def Show_Add_Dialog(self):
        self.adding = AddDialog()
        self.adding.pushButton.clicked.connect(self.Add_Data)
        self.adding.exec()'''
        
        
    def ajout_info(self):
        
        mat = self.lineEdit_mat.text()
        name = self.lineEdit_nom.text()
        pre = self.lineEdit_pre.text()
        clas = self.lineEdit_class.text()
        boy = self.homme.text()
        girl = self.femme.text()
        inf_par = [mat,name,pre,clas,boy,girl]
        cur.execute("INSERT INTO PARRAIN_MARRAINE VALUES(?,?,?,?,?,?)",inf_par)
        print(mat,name,pre,clas,boy,girl)
        conn.commit()
        conn.close()
            
    
        
    '''def modif_info():
        
        cur.execute("SELECT Matricule FROM PARRAIN_MARRAINE")
        recup = cur.fetchall()
        
        for m in recup:
            Liste.append(m)
        #methode pour rendre en liste le tuple resultat2
        L = [x for el in Liste for x in el] #list comprehension
        print (L)
        
        while mat not in L:
            mat = input("Ce matricule ne figure pas dans la base de données.Entrez à nouveau le matricule à modifier: ")
        else:
            new_mat = input("\nMatricule INP: ").upper()
            new_nom = input("Nom: ").upper()
            new_prenom = input ("Prénom: ").capitalize()
            new_classe = input("Classe: ").upper()
            new_filiere = input("Filière: ").upper()
            new_sexe = input("Sexe: ").upper()
        _parrain = les_parrains(new_mat,new_nom,new_prenom,new_classe,new_filiere,new_sexe)
            
        cur.execute("UPDATE PARRAIN_MARRAINE SET Matricule= ? , Nom= ? , Prenom = ? , Classe = ? , Filiere = ? , Sexe = ? WHERE Matricule = ? ", (_parrain.mat, _parrain.nom, _parrain.prenom, _parrain.classe, _parrain.filiere, _parrain.sexe,mat))
        conn.commit()
        print("Modification effectuée avec succès!!\n\n")
        
        
    def supp_info():

        mat = input("\nEntrez le matricule à supprimer :")
        Liste = []
        cur.execute("SELECT Matricule FROM PARRAIN_MARRAINE")
        recup = cur.fetchall()
        for m in recup:
            Liste.append(m)
        #methode pour rendre en liste le tuple resultat2
        L = [x for el in Liste for x in el] #list comprehension
        print (L)
        while mat not in L:
            mat = input("Ce matricule ne figure pas dans la base de données.Entrez à nouveau le matricule à supprimer: ")
        else:
            cur.execute("DELETE FROM PARRAIN_MARRAINE WHERE Matricule= ?", (mat,))
            conn.commit()
            print("Suppression effectuée avec succès!!\n\n")
        
            
class MainApp(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.Init_Ui()
        

    def Init_Ui(self):
        self.setupUi(self)
        self.Load_Database()
        self.show()
        self.pushButton.clicked.connect(self.Show_Add_Dialog)
        
    def Show_Add_Dialog(self):
        self.adding = AddDialog()
        self.adding.pushButton.clicked.connect(self.Add_Data)
        self.adding.exec()
        
    def add_Data(self):
         mat = self.adding.lineEdit.text()
         name = self.lineEdit_2.text()
         pre = self.lineEdit_3.text()
         clas = self.lineEdit_4.text()
         boy = self.radioButton.text()
         girl = self.radioButton_2.txt()
         
         try:'''
             
        
'''import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()'''
sys.exit(app.exec_())

