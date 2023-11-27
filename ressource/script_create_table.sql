#Base de Donnée TP Livre dont vous êtes le héros
DROP DATABASE IF EXISTS LoupSolitaire;
CREATE DATABASE LoupSolitaire;
USE LoupSolitaire;

CREATE TABLE fiche_personnage(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	habilete INTEGER NOT NULL DEFAULT 10,
	endurance INTEGER NOT NULL DEFAULT 20,
	nom VARCHAR(100) NOT NULL DEFAULT ("Loup Solitaire")
	CHECK (habilete >= 0 AND endurance >= 0));

CREATE TABLE discipline_kai(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(100) NOT NULL,
	texte TEXT NOT NULL);

CREATE TABLE disciplinesconnues (
	id_personnage INTEGER,
	id_discipline INTEGER,
	PRIMARY KEY(id_personnage, id_discipline),
	FOREIGN KEY (id_personnage) REFERENCES fiche_personnage(id),
	FOREIGN KEY (id_discipline) REFERENCES  discipline_kai(id)
	);
CREATE TABLE armes (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(100) NOT NULL);
	
CREATE TABLE armespossede (
	id_personnage INTEGER,
	id_arme INTEGER,
	PRIMARY KEY (id_personnage, id_arme),
	FOREIGN KEY (id_personnage) REFERENCES fiche_personnage(id),
	FOREIGN KEY (id_arme) REFERENCES armes(id));

CREATE TABLE equipement (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	objets VARCHAR(255) NULL,
	objets_speciaux VARCHAR(255) NULL,
	bourse INTEGER NULL,
	repas VARCHAR(255) NULL,
	id_personnage INTEGER NOT NULL,
	FOREIGN KEY (id_personnage) REFERENCES fiche_personnage(id));
	
CREATE TABLE livre (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	titre VARCHAR(100)NOT NULL);

CREATE TABLE chapitre (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom_chapitre VARCHAR(100) NOT NULL,
	texte LONGTEXT NOT NULL,
	id_livre INTEGER,
	FOREIGN KEY (id_livre) REFERENCES livre(id));

CREATE TABLE sauvegarde (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	id_personnage INTEGER,
	id_chapitre INTEGER,
	date_sauvegarde DATETIME DEFAULT current_timestamp(),
	FOREIGN KEY (id_personnage) REFERENCES fiche_personnage(id),
	FOREIGN KEY (id_chapitre) REFERENCES chapitre(id));
	
	
CREATE TABLE lien_chapitre (
	no_chapitre_origine INTEGER,
	no_chapitre_destination INTEGER,
	PRIMARY KEY (no_chapitre_origine, no_chapitre_destination),
	FOREIGN KEY (no_chapitre_origine) REFERENCES chapitre(id),
	FOREIGN KEY (no_chapitre_destination) REFERENCES chapitre(id));




/*Création d'un utilisateur aux accès restreints.*/


CREATE USER IF NOT EXISTS 'Lecteur' IDENTIFIED BY 'Viveleslivres';

GRANT SELECT, INSERT, UPDATE, DELETE
ON LoupSolitaire.fiche_personnage
TO Lecteur;

GRANT SELECT, INSERT, UPDATE, DELETE
ON LoupSolitaire.armespossede
TO Lecteur;

GRANT SELECT, INSERT, UPDATE, DELETE
ON LoupSolitaire.disciplinesconnues
TO Lecteur;

GRANT SELECT, INSERT, UPDATE, DELETE
ON LoupSolitaire.equipement
TO Lecteur;

GRANT SELECT, INSERT, UPDATE, DELETE
ON LoupSolitaire.sauvegarde
TO Lecteur;

GRANT SELECT
ON LoupSolitaire.discipline_kai 
TO Lecteur;

GRANT SELECT
ON LoupSolitaire.armes 
TO Lecteur;

GRANT SELECT
ON LoupSolitaire.livre
TO Lecteur;

GRANT SELECT
ON LoupSolitaire.chapitre 
TO Lecteur;

GRANT SELECT
ON LoupSolitaire.lien_chapitre 
TO Lecteur;