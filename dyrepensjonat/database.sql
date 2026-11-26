-- Oppgave 1 – Opprett database og implementer datamodellen

-- https://drive.google.com/file/d/1mASiiO5UoqMO5Wvl-bq15uf5a0Lf7amz/view?usp=sharing

DROP DATABASE IF EXISTS dyrepensjonat;

CREATE DATABASE IF NOT EXISTS dyrepensjonat;

USE dyrepensjonat;

CREATE TABLE owners
(
    owner_id INT AUTO_INCREMENT NOT NULL,
    name     VARCHAR(100)       NOT NULL,
    phone    VARCHAR(20)        NOT NULL,
    email    VARCHAR(120)       NOT NULL,
    PRIMARY KEY (owner_id)
);

CREATE TABLE pets
(
    pet_id   INT AUTO_INCREMENT NOT NULL,
    owner_id INT                NOT NULL,
    name     VARCHAR(80)        NOT NULL,
    species  VARCHAR(40)        NOT NULL,
    breed    VARCHAR(80)        NOT NULL,
    PRIMARY KEY (pet_id),
    FOREIGN KEY (owner_id) REFERENCES owners (owner_id)
);

CREATE TABLE rooms
(
    room_id     INT AUTO_INCREMENT NOT NULL,
    room_number VARCHAR(10)        NOT NULL,
    room_type   VARCHAR(40)        NOT NULL,
    daily_rate  DECIMAL(8, 2)      NOT NULL,
    PRIMARY KEY (room_id),
    UNIQUE (room_number)
);

CREATE TABLE stays
(
    stay_id   INT AUTO_INCREMENT NOT NULL,
    pet_id    INT                NOT NULL,
    room_id   INT                NOT NULL,
    check_in  DATE               NOT NULL,
    check_out DATE               NOT NULL,
    PRIMARY KEY (stay_id),
    FOREIGN KEY (pet_id) REFERENCES pets (pet_id),
    FOREIGN KEY (room_id) REFERENCES rooms (room_id)
);


-- Legger til eiere

INSERT INTO owners(name, phone, email)
VALUES ('Ingrid Hansen', '90000001', 'ingrid.hansen@example.com'),
       ('Thomas Johansen', '90000002', 'thomas.johansen@example.com'),
       ('Maria Olsen', '90000003', 'maria.olsen@example.com'),
       ('Erik Larsen', '90000004', 'erik.larsen@example.com'),
       ('Anne Berg', '90000005', 'anne.berg@example.com'),
       ('Henrik Nilsen', '90000006', 'henrik.nilsen@example.com'),
       ('Silje Andersen', '90000007', 'silje.andersen@example.com'),
       ('Morten Solberg', '90000008', 'morten.solberg@example.com');


-- Legger til kjæledyr

INSERT INTO pets(owner_id, name, species, breed)
VALUES (1, 'Luna', 'Dog', 'Golden Retriever'),
       (1, 'Milo', 'Cat', 'Maine Coon'),
       (2, 'Max', 'Dog', 'Labrador Retriever'),
       (3, 'Bella', 'Dog', 'Border Collie'),
       (3, 'Simba', 'Cat', 'Norwegian Forest Cat'),
       (4, 'Charlie', 'Dog', 'Miniature Poodle'),
       (5, 'Nala', 'Cat', 'Ragdoll'),
       (5, 'Leo', 'Cat', 'British Shorthair'),
       (6, 'Rocky', 'Dog', 'German Shepherd'),
       (7, 'Molly', 'Rabbit', 'Mini Lop'),
       (8, 'Teddy', 'Dog', 'Cocker Spaniel'),
       (8, 'Coco', 'Rabbit', 'Lionhead');


-- Legger til rom

INSERT INTO rooms (room_number, room_type, daily_rate)
VALUES ('H101', 'Dog - Standard', 450.00),
       ('H102', 'Dog - Standard', 450.00),
       ('H103', 'Dog - Large', 550.00),
       ('H104', 'Dog - Premium', 650.00),
       ('K201', 'Cat - Standard', 300.00),
       ('K202', 'Cat - Standard', 300.00),
       ('K203', 'Cat - Premium', 400.00),
       ('S301', 'Small Animals', 200.00);


-- Legger til opphold

INSERT INTO stays (pet_id, room_id, check_in, check_out)
VALUES (1, 1, '2026-11-01', '2026-11-07'),
       (2, 5, '2026-11-01', '2026-11-07'),
       (3, 3, '2026-11-10', '2026-11-15'),
       (4, 2, '2026-11-15', '2026-11-20'),
       (5, 6, '2026-11-15', '2026-11-20'),
       (6, 1, '2026-11-24', '2026-11-30'),
       (7, 7, '2026-11-25', '2026-12-03'),
       (8, 5, '2026-11-25', '2026-12-03'),
       (9, 3, '2026-11-28', '2026-12-05'),
       (10, 8, '2026-12-01', '2026-12-06'),
       (11, 4, '2026-12-02', '2026-12-09'),
       (12, 8, '2026-12-10', '2026-12-15'),
       (1, 1, '2026-12-20', '2026-12-28'),
       (2, 5, '2026-12-20', '2026-12-28'),
       (3, 3, '2026-12-22', '2027-01-03');


-- Kontrollerer eksempeldata

-- SELECT * FROM owners;
-- SELECT * FROM pets;
-- SELECT * FROM rooms;
-- SELECT * FROM stays;