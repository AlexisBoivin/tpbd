import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importer la classe Ui_MainWindow du fichier demo.py
from livre import Ui_MainWindow

cnx = mysql.connector.connect(
    user='Lecteur', 
    password='Viveleslivres',
    host='localhost',
    database='LoupSolitaire')



def chargerPartie(self):
    parametre = {
        "id": self.idSauvegarde
    }
    query = """SELECT * FROM sauvegarde 
    INNER JOIN fiche_personnage ON sauvegarde.id_personnage  = fiche_personnage.id
    INNER JOIN chapitre ON chapitre.id = sauvegarde.id_chapitre
    INNER JOIN livre ON livre.id = chapitre.id_livre
    INNER JOIN lien_chapitre ON no_chapitre_origine = chapitre.id
    INNER JOIN equipement ON equipement.id_personnage = fiche_personnage.id
    WHERE sauvegarde.id = %(id)s;"""
    cursor. cnx.cursor(dictionary=True)
    cursor.execute(query, parametre)
    for (ligne) in cursor:
        self.comboBoxtitre.CurrentText = str(ligne["livre.titre"])
        self.lineEditNomPersonnage.text = str(ligne["fiche_personnage.nom"])
        self.textEditObjet.text = str(ligne["equipement.objets"])
        self.textEditspeciaux.text = str(ligne["equipement.objets_speciaux"])
        self.textEditBourse.text = str(ligne["equipement.bourse"])
        self.textEditRepas.text = str(ligne["equipement.repas"])
        self.spinBoxH.Value = ligne["habilete"]
        self.spinBoxE.Value = ligne["endurance"]
        self.textBrowserTexteChapitre.text = str(ligne["chapitre.texte"])
        self.lineEditNomChapitre.text = str(ligne["nom_chapitre"])
    cursor.close()

    query = "SELECT nom FROM disciplinesconnus INNER JOIN discipline_kai ON id = id_discipline WHERE id_personnage = %(id)s"
    cursor.cnx.cursor(dictionary=True)
    cursor.execute(query, parametre)
    disciplines = cursor.fetchall()
    self.comboBoxdiscipline1.currentIndex = disciplines[1]
    self.comboBoxdiscipline2.currentIndex = disciplines[2]
    self.comboBoxdiscipline3.currentIndex = disciplines[3]
    self.comboBoxdiscipline4.currentIndex = disciplines[4]
    self.comboBoxdiscipline5.currentIndex = disciplines[5]
    cursor.close()
    query = "SELECT nom FROM armespossede INNER JOIN armes ON id = id_arme WHERE id_personnage = %(id)s"
    cursor.cnx.cursor(dictionary=True)
    cursor.execute(query, parametre)
    armes = cursor.fetchall()
    self.comboBoxArme1.currentIndex = armes[1]
    self.comboBoxArme2.currentIndex = armes[2]
    cursor.close()

def choixChapitre(self):
    self.comboBoxChoixSuivant.clear()
    parametre = {
        "no": self.lineEditNomChapitre.text()
    }
    query = "SELECT c2.nom_chapitre AS lacolonne FROM chapitre c INNER JOIN lien_chapitre lc ON no_chapitre_origine = c.id INNER JOIN chapitre c2 ON no_chapitre_destination = c2.id WHERE c.nom_chapitre = %(no)s ;"
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query, parametre)
    for (ligne) in cursor:
        self.comboBoxChoixSuivant.addItem(ligne["lacolonne"])

def choixDisciplineKai(self):
    query = "SELECT nom FROM discipline_kai;"
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    for (ligne) in cursor:
        self.comboBoxdiscipline1.addItem(str(ligne["nom"]))
        self.comboBoxdiscipline2.addItem(str(ligne["nom"]))
        self.comboBoxdiscipline3.addItem(str(ligne["nom"]))
        self.comboBoxdiscipline4.addItem(str(ligne["nom"]))
        self.comboBoxdiscipline5.addItem(str(ligne["nom"]))
    cursor.close()

def choixArmes(self):
    query = "SELECT nom FROM armes;"
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    for (ligne) in cursor:
        self.comboBoxArme1.addItem(str(ligne["nom"]))
        self.comboBoxArme2.addItem(str(ligne["nom"]))
    cursor.close()

def choixSauvegarde(self):
    query = """SELECT sauvegarde.id, nom, nom_chapitre FROM sauvegarde
    INNER JOIN fiche_personnage ON fiche_personnage.id = sauvegarde.id_personnage
    INNER JOIN chapitre ON chapitre.id = id_chapitre;"""
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    for (ligne) in cursor:
        self.comboBoxSauvegarde.addItem(str(ligne["nom"] + " - Chapitre: " + ligne["nom_chapitre"]))
    cursor.close()

def afficherTitre(self):
    query = "SELECT titre FROM livre;"
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    for (ligne) in cursor:
        self.comboBoxtitre.addItem(str(ligne["titre"]))
    cursor.close()

#mise a jour des armes et disciplines assosciés aux personnages.
def armesEtdiscipline(self):

    nom = self.lineEditnomPersonnage.text()
    querypersonnage = f"SELECT id FROM fiche_personnage WHERE nom = {nom};"
    print(nom)
    cursor = cnx.cursor(dictionary=True)
    idpersonnage = cursor.execute(querypersonnage)
    cursor.close()
    parametre = {
        "id_personnage":idpersonnage,
        "arme1": self.comboBoxArme1.CurrentText(),
        "arme2": self.comboBoxArme2.CurrentText(),
        "discipline1": self.comboBoxdiscipline1.CurrentText(),
        "discipline2": self.comboBoxdiscipline2.CurrentText(),
        "discipline3": self.comboBoxdiscipline3.CurrentText(),
        "discipline4": self.comboBoxdiscipline4.CurrentText(),
        "discipline5": self.comboBoxdiscipline5.CurrentText()
    }
    query = """DELETE FROM armespossede WHERE id_personnage = %(id_personnage)s;
		DELETE FROM disciplinesconnues WHERE id_personnage = %(id_personnage)s;
		UPDATE fiche_personnage SET habilete = %(habilete)s, endurance = %(endurance)s WHERE id = %(id_personnage)s;
		INSERT INTO armespossede (id_personnage, id_arme) VALUES
		(%(id_personnage)s, %(arme1)s),
		(%(id_personnage)s, %(arme2)s);
		INSERT INTO disciplinesconnues (id_personnage, id_discipline) VALUES
		(%(id_personnage)s, %(discipline1)s),
		(%(id_personnage)s, %(discipline2)s),
        (%(id_personnage)s, %(discipline3)s),
        (%(id_personnage)s, %(discipline4)s),
        (%(id_personnage)s, %(discipline5)s);"""
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    for (ligne) in cursor:
        self.comboBoxtitre.addItem(str(ligne["titre"]))
        lesSauvegardes[i] = ligne["sauvegarde.id"]
        i += 1
    cursor.close()




def remplirChapitre(self, chapitre):
    if chapitre == "":
        chapitre = "Avertir le roi"
    parametre = {
        "nomchapitre": chapitre
    }
    query = "SELECT nom_chapitre, texte FROM chapitre WHERE nom_chapitre = %(nomchapitre)s"
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query, parametre)
    for ligne in cursor:
        text = ligne["texte"]
    self.textEditPrincipale.setText(text)
    self.lineEditNomChapitre.setText(chapitre)
    cursor.close()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)
        idSauvgarde = 0
        lesSauvegardes = {}
        self.comboBoxSauvegarde.currentIndexChanged.connect(self.changerselection)
        choixDisciplineKai(self)
        choixArmes(self)
        afficherTitre(self)
        choixSauvegarde(self)
        remplirChapitre(self, "Avertir le roi")
        choixChapitre(self)
    def changerselection(self, i):
        idSauvegarde = lesSauvegardes[i]
        # On a accès à tous les éléments de notre interface


    def changerChapitre(self):
        no = self.comboBoxChoixSuivant.currentText()
        parametre = {
            "no": no
        }
        remplirChapitre(self, no)
        choixChapitre(self)

    def creerPersonnage(self):
        parametre = {
            "nom" : self.lineEditnomPersonnage.text,
            "discipline1": self.comboBoxdiscipline1.currentText(),
            "discipline2": self.comboBoxdiscipline2.currentText(),
            "discipline3": self.comboBoxdiscipline3.currentText(),
            "discipline4": self.comboBoxdiscipline4.currentText(),
            "discipline5": self.comboBoxdiscipline5.currentText(),
            "arme1": self.comboBoxArme1.currentText(),
            "arme2": self.comboBoxArme2.currentText()
        }
        query = "CALL nouveau_personnage(%(nom)s, %(discipline1)s, %(discipline2)s, %(discipline3)s, %(discipline4)s, %(discipline5)s, %(arme1)s, %(arme2)s );"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, parametre)
    def supprimer_sauvegarde(self):
        parametre = {
            "id": self.lineEditIdSauvegarde.text
        }
        query = "CALL supprimer_sauvegarde();"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, parametre)
        for (ligne) in cursor:
            self.comboBoxtitre.addItem(str(ligne["titre"]))
        cursor.close()
    
    def sauvegarder(self):
        self.creerPersonnage()
        armesEtdiscipline(self)
    ##trouver id personnage
        parametrepersonnage = {
            "nom":self.lineEditnomPersonnage.text()
        }
        querypersonnage = "SELECT id FROM fiche_personnage WHERE nom = %(nom)s;"
        cursor = cnx.cursor(dictionary=True)
        idpersonnage = cursor.execute(querypersonnage, parametrepersonnage)
        cursor.close()
    ##trouver id chapitre
        cursor = cnx.cursor(dictionary=True)
        parametrechapitre = {
            "livre": self.comboBoxtitre.CurrentText()
        }
        querychapitre =  "SELECT chapitre.id FROM chapitre INNER JOIN livre ON id_livre = livre.id WHERE titre = %(livre)s"
        chapitre = cursor.execute(querychapitre, parametrechapitre)
        cursor.close()

    ##insert into sauvegarde
        parametre = {
            "id_personnage":idpersonnage,
            "habilete": self.spinBoxH.Value(),
            "endurance": self.spinBoxE.Value(),
            "chapitre": chapitre
        }
        query = "INSERT INTO sauvegarde (id_personnage, id_chapitre) VALUES (%(id_personnage)s, %(chapitre)s);"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, parametre)
    #fonction qui charge une partie.
#############
app = QApplication(sys.argv) 
window = MainWindow()
window.show()
app.exec()
