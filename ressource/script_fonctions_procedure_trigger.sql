#Fontions tp Loup Solitaire
#Procédure qui crée une sauvegarde.
USE LoupSolitaire;

#procédure qui crée un personnage et son équipement.
DELIMITER $$
DROP PROCEDURE IF EXISTS nouveau_personnage $$
	CREATE PROCEDURE IF NOT EXISTS nouveau_personnage(IN nom VARCHAR(100), IN discipline1 INTEGER , IN discipline2 INTEGER, IN discipline3 INTEGER, IN discipline4 INTEGER, IN discipline5 INTEGER, IN arme1 INTEGER, IN arme2 INTEGER )
		BEGIN
			DECLARE _nom VARCHAR(100);
			DECLARE _discipline1 INTEGER;
			DECLARE _discipline2 INTEGER;
			DECLARE _discipline3 INTEGER;
			DECLARE _discipline4 INTEGER;
			DECLARE _discipline5 INTEGER;
			DECLARE _arme1 INTEGER;
			DECLARE _arme2 INTEGER;
			SET _nom = nom;
			SET _discipline1 = discipline1;
			SET _discipline2 = discipline2;
			SET _discipline3 = discipline3;
			SET _discipline4 = discipline4;
			SET _discipline5 = discipline5;
			SET _arme1 = arme1;
			SET _arme2 = arme2;
			INSERT INTO fiche_personnage (nom)VALUES (_nom);
			INSERT INTO disciplinesconnues (id_personnage, id_discipline) VALUES 
			(last_insert_id(), _discipline1),
			(last_insert_id(), _discipline2),
			(last_insert_id(), _discipline3),
			(last_insert_id(), _discipline4),
			(last_insert_id(), _discipline5);
			INSERT INTO armespossede (id_personnage, id_discipline) VALUES
			(last_insert_id(), _arme1),
			(last_insert_id(), _arme2);
			END $$

DELIMITER ;
DELIMITER $$
	CREATE PROCEDURE IF NOT EXISTS supprimer_sauvegarde(IN id INTEGER)
		BEGIN
			DECLARE _id INTEGER;
			SET _id = id;
			DELETE FROM sauvegarde WHERE id = _id;
		END
		
DELIMITER ;