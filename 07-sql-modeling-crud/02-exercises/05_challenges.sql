-- Challenge 1: Volunteers and Animals.

-- https://drive.google.com/file/d/1wZZeFzZVost1Kz8yIT3HnO3mXFCxp3hY/view?usp=sharing

-- The pair (volunteer_id, animal_id) must be UNIQUE because one row means
-- "this volunteer follows up this animal". The same fact should be stored
-- only once. Without the constraint, the same volunteer could be linked to
-- the same animal twice, which gives duplicate and confusing data.

-- Each foreign key alone must NOT be UNIQUE:
-- If volunteer_id were UNIQUE, a volunteer could appear in only one row,
-- so one volunteer could follow only one animal.
-- If animal_id were UNIQUE, an animal could appear in only one row,
-- so each animal could have only one volunteer.
-- Both would break the many-to-many relationship, which is the whole
-- reason for having the link table.


-- Challenge 2: Build and test the junction table.

CREATE TABLE volunteers (
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (name)
);

CREATE TABLE volunteers_animals (
    volunteer_id INT NOT NULL,
    animal_id INT NOT NULL,
    PRIMARY KEY (volunteer_id, animal_id),
    FOREIGN KEY (volunteer_id) REFERENCES volunteers (id),
    FOREIGN KEY (animal_id)    REFERENCES animals (id)
);

INSERT INTO volunteers (name)
VALUES ('Emily Carter'),  -- 1
       ('James Wilson'),  -- 2
       ('Sophie Turner'); -- 3

SELECT *
FROM volunteers;

SELECT id, name, species
FROM animals;

INSERT INTO volunteers_animals (volunteer_id, animal_id)
VALUES (1, 3 ),
       (1, 4 ),
       (2, 1 ),
       (2, 2 ),
       (2, 9 ),
       (2, 10 ),
       (3, 5 ),
       (3, 6 ),
       (3, 3 );

INSERT INTO volunteers_animals (volunteer_id, animal_id)
VALUES (3, 3 );

-- Duplicate entry '3-3' for key 'volunteers_animals.PRIMARY'

DELETE FROM volunteers_animals
WHERE volunteer_id = 2
  AND animal_id = 10;

SELECT *
FROM volunteers_animals
WHERE volunteer_id = 2 AND  animal_id = 10;

-- DELETE FROM volunteers_animals
-- WHERE (volunteer_id, animal_id) = (2, 10);


-- Challenge 3: At most one profile per volunteer

-- https://drive.google.com/file/d/17eUliIx7-OPjDIidslIvEEmHlyDR9bX7/view?usp=sharing

CREATE TABLE volunteer_profiles (
    id INT AUTO_INCREMENT,
    volunteer_id INT NOT NULL UNIQUE,
    phone VARCHAR(30),
    bio VARCHAR(250),
    PRIMARY KEY (id),
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(id)
);

INSERT INTO volunteer_profiles (volunteer_id, phone, bio)
VALUES (1,'+47 123 45 678', 'Loves working with cats.');

INSERT INTO volunteer_profiles (volunteer_id, phone, bio)
VALUES (1, '+47 987 65 432', 'Second profile.');

-- Duplicate entry '1' for key 'volunteer_profiles.volunteer_id'

-- Modellen tillater at en frivillig ikke har noen profil,
-- fordi kravene ligger i volunteer_profiles, ikke i volunteers.
-- FOREIGN KEY og NOT NULL på volunteer_id sørger for at hver profil
-- tilhører en eksisterende frivillig,
-- og UNIQUE sørger for at en frivillig har høyst én profil.
-- Ingenting i volunteers krever at det finnes en rad i volunteer_profiles.
-- En frivillig er en egen rad som kan eksistere uten profil,
-- og profilen er en valgfri, separat rad.
-- Derfor er forholdet «null eller én» sett fra frivillig,
-- og «nøyaktig én» sett fra profil.


-- Challenge 4: NULL and empty text

CREATE  TABLE scratch_names (
    id INT AUTO_INCREMENT,
    nickname VARCHAR(40) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO scratch_names (nickname)
VALUES ('');

SELECT *
FROM scratch_names;

INSERT INTO scratch_names (nickname)
VALUES (Null);

-- Column 'nickname' cannot be null

SELECT id, nickname
FROM scratch_names
WHERE nickname = '';

-- Verdien NOT NULL er ikke nok til å kreve et meningsfullt navn
-- Fordi den ikke begrenser bruken av for eksempel ''.

DROP TABLE scratch_names;


-- Challenge 5: Creating a Model Independently

-- https://drive.google.com/file/d/1_SKCTkqg6Q6iJzgMNTAVXHKBL9Woxuo2/view?usp=sharing

CREATE DATABASE IF NOT EXISTS astronomy_practice;

USE astronomy_practice;

SELECT DATABASE();

CREATE TABLE telescopes (
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    diameter_mm DECIMAL(5,1) NOT NULL,
    PRIMARY KEY (id),
    CHECK (diameter_mm > 0)
);

-- Diameter is stored as DECIMAL(5,1) NOT NULL
-- because a diameter can have one decimal (e.g. 203.2 mm)
-- and club telescopes stay well below 10 000 mm.

CREATE TABLE observations (
    id INT AUTO_INCREMENT,
    observation_date DATE NOT NULL,
    object_name VARCHAR(40) NOT NULL,
    telescope_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (telescope_id) REFERENCES telescopes(id)
);

INSERT INTO telescopes (name, diameter_mm)
VALUES ('Celestron NexStar 8SE', 203.2),
       ('Sky-Watcher 130P', 130.0);

SELECT * FROM telescopes;

INSERT INTO observations (observation_date, object_name, telescope_id)
VALUES ('2026-09-10', 'Jupiter', 1),
       ('2026-09-12', 'Andromeda Galaxy', 1),
       ('2026-09-15', 'Orion Nebula', 2),
       ('2026-09-18', 'Saturn', 2);

SELECT id
FROM observations
WHERE observation_date = '2026-09-18';

UPDATE observations
SET observation_date = '2026-10-19'
WHERE id = 4;

SELECT *
FROM observations
WHERE id = 4;

DELETE FROM telescopes
WHERE id = 1;

-- Cannot delete or update a parent row: a foreign key constraint fails
-- (`astronomy_practice`.`observations`, CONSTRAINT `observations_ibfk_1` FOREIGN KEY
-- (`telescope_id`) REFERENCES `telescopes` (`id`))

SELECT *
FROM telescopes;

SELECT object_name
FROM observations
WHERE observation_date = '2026-09-15';

SELECT object_name, observation_date
FROM observations
WHERE telescope_id = 2
ORDER BY observation_date;

-- Challenge 6: Explain and verify your own work

-- 1. Fremmednøkkel

-- FOREIGN KEY (telescope_id) REFERENCES telescopes(id)

-- Hva den gjør: Hver verdi i observations.telescope_id må finnes som id i telescopes.
-- En observasjon kan dermed ikke tilhøre et teleskop som ikke finnes.
-- Hvordan jeg kontrollerte: Jeg prøvde DELETE FROM telescopes WHERE id = 1;.
-- MySQL ga feilmeldingen Cannot delete or update a parent row: a foreign key constraint fails,
-- fordi observasjoner fortsatt peker på teleskop 1. Det viser at nøkkelen fungerer.
-- Feil jeg kunne gjort: Opprette observations før telescopes (nøkkelen peker da på en tabell som ikke finnes),
-- eller sette inn en observasjon med telescope_id = 99.

-- 2. Strukturendring

-- ALTER TABLE observations
-- ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'new';

-- Hva den gjør: Legger til kolonnen status i en tabell som allerede finnes.
-- Eksisterende rader får verdien 'new' fordi vi har satt DEFAULT.
-- Hvordan jeg kontrollerte: SELECT id, name, status FROM animals; viser at alle rader har new.
-- Kolonnen kan også ses i tabellstrukturen i DataGrip.
-- Feil jeg kunne gjort: Bruke NOT NULL uten DEFAULT på en tabell med data, slik at de gamle radene mangler verdi.
-- Eller kjøre setningen to ganger: kolonnen finnes da allerede, og det gir feil.

-- 3. Dataendring

-- UPDATE observations
-- SET observation_date = '2026-10-19'
-- WHERE id = 4;

-- Hva den gjør: Endrer datoen for kun observasjonen med id = 4.
-- Hvordan jeg kontrollerte: SELECT * FROM observations WHERE id = 4; viser den nye datoen.
-- Feil jeg kunne gjort: Glemme WHERE, slik at datoen endres i alle rader.
-- Derfor kjører jeg først en SELECT med samme WHERE-betingelse.

-- Kjørerekkefølge for SQL-filene

-- 1. Creation:        CREATE DATABASE, CREATE TABLE telescopes,
--                     CREATE TABLE observations
-- 2. Start data:      INSERT INTO telescopes, INSERT INTO observations
-- 3. Later changes:   ALTER TABLE (strukturendring), UPDATE (dataendring)
-- 4. Expected to fail: DELETE FROM telescopes WHERE id = 1
--                     (the foreign key stops it on purpose)
-- 5. Checks:          SELECT statements

-- Tabellen telescopes må opprettes og fylles før observations, fordi fremmednøkkelen peker på rader som må finnes.
-- Hvorfor noen setninger ikke bør kjøres flere ganger
-- CREATE TABLE feiler andre gang, fordi tabellen allerede finnes.
-- ALTER TABLE ... ADD COLUMN feiler andre gang, fordi kolonnen allerede finnes.
-- INSERT feiler ikke, men legger inn de samme radene på nytt og gir duplikater.
-- DELETE og UPDATE kan gi et annet resultat andre gang, fordi dataene allerede er endret.
-- En UPDATE uten WHERE kan ødelegge mange rader.
-- Derfor kjører vi filene én gang, i riktig rekkefølge.
-- Hvis noe går galt, er det enklest å slette databasen og starte på nytt.
