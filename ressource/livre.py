# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'livre.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(250, 50, 341, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEditPrincipale = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEditPrincipale.setGeometry(QtCore.QRect(0, 0, 341, 1261))
        self.textEditPrincipale.setReadOnly(True)
        self.textEditPrincipale.setObjectName("textEditPrincipale")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.spinBoxE = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxE.setGeometry(QtCore.QRect(710, 40, 81, 71))
        self.spinBoxE.setObjectName("spinBoxE")
        self.spinBoxH = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxH.setGeometry(QtCore.QRect(620, 40, 81, 71))
        self.spinBoxH.setObjectName("spinBoxH")
        self.sauvegardeButton = QtWidgets.QPushButton(self.centralwidget)
        self.sauvegardeButton.setGeometry(QtCore.QRect(520, 490, 141, 41))
        self.sauvegardeButton.setObjectName("sauvegardeButton")
        self.chargerButton = QtWidgets.QPushButton(self.centralwidget)
        self.chargerButton.setGeometry(QtCore.QRect(660, 490, 131, 41))
        self.chargerButton.setObjectName("chargerButton")
        self.labelsauvegarde = QtWidgets.QLabel(self.centralwidget)
        self.labelsauvegarde.setGeometry(QtCore.QRect(600, 410, 201, 41))
        self.labelsauvegarde.setObjectName("labelsauvegarde")
        self.labelHabilete = QtWidgets.QLabel(self.centralwidget)
        self.labelHabilete.setGeometry(QtCore.QRect(620, 10, 71, 16))
        self.labelHabilete.setObjectName("labelHabilete")
        self.labelEndurance = QtWidgets.QLabel(self.centralwidget)
        self.labelEndurance.setGeometry(QtCore.QRect(710, 10, 81, 16))
        self.labelEndurance.setObjectName("labelEndurance")
        self.comboBoxdiscipline1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxdiscipline1.setGeometry(QtCore.QRect(10, 160, 231, 22))
        self.comboBoxdiscipline1.setObjectName("comboBoxdiscipline1")
        self.comboBoxdiscipline2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxdiscipline2.setGeometry(QtCore.QRect(10, 180, 231, 22))
        self.comboBoxdiscipline2.setObjectName("comboBoxdiscipline2")
        self.comboBoxdiscipline3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxdiscipline3.setGeometry(QtCore.QRect(10, 200, 231, 22))
        self.comboBoxdiscipline3.setObjectName("comboBoxdiscipline3")
        self.comboBoxdiscipline4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxdiscipline4.setGeometry(QtCore.QRect(10, 220, 231, 22))
        self.comboBoxdiscipline4.setObjectName("comboBoxdiscipline4")
        self.comboBoxdiscipline5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxdiscipline5.setGeometry(QtCore.QRect(10, 240, 231, 22))
        self.comboBoxdiscipline5.setObjectName("comboBoxdiscipline5")
        self.comboBoxArme1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxArme1.setGeometry(QtCore.QRect(10, 300, 231, 22))
        self.comboBoxArme1.setObjectName("comboBoxArme1")
        self.comboBoxArme2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxArme2.setGeometry(QtCore.QRect(10, 320, 231, 22))
        self.comboBoxArme2.setObjectName("comboBoxArme2")
        self.labelArmes = QtWidgets.QLabel(self.centralwidget)
        self.labelArmes.setGeometry(QtCore.QRect(10, 270, 141, 20))
        self.labelArmes.setObjectName("labelArmes")
        self.labeldisciplines = QtWidgets.QLabel(self.centralwidget)
        self.labeldisciplines.setGeometry(QtCore.QRect(10, 130, 121, 20))
        self.labeldisciplines.setObjectName("labeldisciplines")
        self.labeltitrelivre = QtWidgets.QLabel(self.centralwidget)
        self.labeltitrelivre.setGeometry(QtCore.QRect(20, 10, 55, 16))
        self.labeltitrelivre.setObjectName("labeltitrelivre")
        self.textEditBourse = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditBourse.setGeometry(QtCore.QRect(620, 160, 171, 87))
        self.textEditBourse.setObjectName("textEditBourse")
        self.textEditObjet = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditObjet.setGeometry(QtCore.QRect(10, 370, 231, 201))
        self.textEditObjet.setObjectName("textEditObjet")
        self.labelSacADos = QtWidgets.QLabel(self.centralwidget)
        self.labelSacADos.setGeometry(QtCore.QRect(10, 350, 91, 16))
        self.labelSacADos.setObjectName("labelSacADos")
        self.comboBoxChoixSuivant = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxChoixSuivant.setGeometry(QtCore.QRect(250, 430, 171, 31))
        self.comboBoxChoixSuivant.setObjectName("comboBoxChoixSuivant")
        self.textEditRepas = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditRepas.setGeometry(QtCore.QRect(620, 280, 171, 87))
        self.textEditRepas.setObjectName("textEditRepas")
        self.labelbourse = QtWidgets.QLabel(self.centralwidget)
        self.labelbourse.setGeometry(QtCore.QRect(620, 140, 121, 16))
        self.labelbourse.setObjectName("labelbourse")
        self.labelRepas = QtWidgets.QLabel(self.centralwidget)
        self.labelRepas.setGeometry(QtCore.QRect(620, 260, 121, 16))
        self.labelRepas.setObjectName("labelRepas")
        self.pushButtonSupprimerSauvegarde = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSupprimerSauvegarde.setGeometry(QtCore.QRect(520, 530, 141, 41))
        self.pushButtonSupprimerSauvegarde.setObjectName("pushButtonSupprimerSauvegarde")
        self.comboBoxtitre = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxtitre.setGeometry(QtCore.QRect(10, 40, 231, 31))
        self.comboBoxtitre.setObjectName("comboBoxtitre")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 470, 101, 16))
        self.label_2.setObjectName("label_2")
        self.textEditspeciaux = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditspeciaux.setGeometry(QtCore.QRect(250, 490, 261, 91))
        self.textEditspeciaux.setObjectName("textEditspeciaux")
        self.lineEditnomPersonnage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditnomPersonnage.setGeometry(QtCore.QRect(10, 100, 231, 22))
        self.lineEditnomPersonnage.setObjectName("lineEditnomPersonnage")
        self.lineEditNomChapitre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNomChapitre.setGeometry(QtCore.QRect(250, 11, 341, 31))
        self.lineEditNomChapitre.setObjectName("lineEditNomChapitre")
        self.comboBoxSauvegarde = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSauvegarde.setGeometry(QtCore.QRect(600, 460, 191, 22))
        self.comboBoxSauvegarde.setObjectName("comboBoxSauvegarde")
        self.pushButtonCreerPersonnage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCreerPersonnage.setGeometry(QtCore.QRect(600, 390, 181, 28))
        self.pushButtonCreerPersonnage.setObjectName("pushButtonCreerPersonnage")
        self.spinBoxIdSauvegarde = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxIdSauvegarde.setGeometry(QtCore.QRect(530, 460, 51, 22))
        self.spinBoxIdSauvegarde.setReadOnly(True)
        self.spinBoxIdSauvegarde.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxIdSauvegarde.setObjectName("spinBoxIdSauvegarde")
        self.pushButtonAller = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAller.setGeometry(QtCore.QRect(430, 430, 93, 31))
        self.pushButtonAller.setObjectName("pushButtonAller")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
       # self.comboBoxdiscipline1.activated['QString'].connect(MainWindow.choixDisciplineKai) # type: ignore
        self.pushButtonCreerPersonnage.clicked.connect(MainWindow.creerPersonnage) # type: ignore
        self.sauvegardeButton.clicked.connect(MainWindow.sauvegarder) # type: ignore
        self.pushButtonSupprimerSauvegarde.clicked.connect(MainWindow.supprimer_sauvegarde) # type: ignore
        #self.chargerButton.clicked.connect(MainWindow.chargerPartie) # type: ignore
        self.pushButtonAller.clicked.connect(MainWindow.changerChapitre) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sauvegardeButton.setText(_translate("MainWindow", "Sauvegarder"))
        self.chargerButton.setText(_translate("MainWindow", "Charger Sauvegarde"))
        self.labelsauvegarde.setText(_translate("MainWindow", "Sélectionner une Sauvegarde"))
        self.labelHabilete.setText(_translate("MainWindow", "Habileté"))
        self.labelEndurance.setText(_translate("MainWindow", "Endurance"))
        self.labelArmes.setText(_translate("MainWindow", "Armes"))
        self.labeldisciplines.setText(_translate("MainWindow", "Disciplines Kai"))
        self.labeltitrelivre.setText(_translate("MainWindow", "Livre"))
        self.labelSacADos.setText(_translate("MainWindow", "Objets"))
        self.labelbourse.setText(_translate("MainWindow", "Bourse"))
        self.labelRepas.setText(_translate("MainWindow", "Repas"))
        self.pushButtonSupprimerSauvegarde.setText(_translate("MainWindow", "Supprimer Sauvegarde"))
        self.label.setText(_translate("MainWindow", "Nom du personnage"))
        self.label_2.setText(_translate("MainWindow", "Objet spéciaux"))
        self.pushButtonCreerPersonnage.setText(_translate("MainWindow", "Créer Personnage"))
        self.pushButtonAller.setText(_translate("MainWindow", "Aller"))
