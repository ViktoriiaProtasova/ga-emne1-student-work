-- Task 4.1 Register the areas

INSERT INTO areas (name)
VALUES ('Cat Wing');

INSERT INTO areas (name)
VALUES ('Dog Wing'),
       ('Small Animals'),
       ('Quiet Zone');


-- Task 4.2 Register the animals

INSERT INTO animals (name, species, weight, admitted_on, area_id)
VALUES ('Luna', 'cat', 3.80, '2026-09-12', 1),
       ('Milo', 'cat', 4.20, NULL, 1),
       ('Rex', 'dog', 18.50, '2026-09-15', 2),
       ('Nala', 'dog', NULL, '2026-09-17', 2),
       ('Pip', 'rabbit', 1.60, '2026-09-20', 4),
       ('Luna', 'rabbit', 2.10, NULL, 4);


-- Task 4.3 Find specific rows

SELECT id, name, species, area_id
FROM animals
ORDER BY species, id;

SELECT name
FROM animals
WHERE name = 'Luna';

SELECT name
FROM animals
WHERE name = 'Luna' AND id = 1;

SELECT name
FROM animals
WHERE admitted_on IS NULL;

SELECT name
FROM animals
WHERE weight IS NULL;

-- Task 4.4 Check counts and placement

SELECT COUNT(*) AS areas_count
FROM areas;

SELECT COUNT(*) AS animals_count
FROM animals;

SELECT name
FROM animals
WHERE area_id = 3;

SELECT COUNT(*) AS small_animals_count
FROM animals
WHERE area_id = 4;

-- Task 5.1 An area name that already exists

INSERT INTO areas (name)
VALUES ('Cat Wing');

-- Duplicate entry 'Cat Wing' for key 'areas.name' because 'areas.name' is unique

-- Task 5.2 A mandatory value is missing

INSERT INTO animals (name, species, weight, admitted_on, area_id)
VALUES (NULL, 'cat', 3.80, '2026-09-12', 1);

-- Column 'name' cannot be null because we set the as NOT NULL

INSERT INTO animals (name, species, weight, admitted_on, area_id)
VALUES ('Kira', 'cat', 3.80, '2026-09-12', NULL);

-- Column 'area_id' cannot be null because we set the as NOT NULL

-- Task 5.3 An area that does not exist

SELECT id
FROM areas
WHERE id = 5;

INSERT INTO animals (name, species, weight, admitted_on, area_id)
VALUES ('Kira', 'cat', 3.80, '2026-09-12', 5);

-- Cannot add or update a child row: a foreign key constraint fails
-- (`animal_shelter_practice`.`animals`, CONSTRAINT `animals_ibfk_1`
-- FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`))
-- This means that `animals.area_id` references an existing `areas.id`.

-- Task 5.4 An ID that is already in use

SELECT id, name
FROM animals;

INSERT INTO animals (id, name, species, weight, admitted_on, area_id)
VALUES (1,'Kira', 'cat', 3.80, '2026-09-12', 5);

--  Duplicate entry '1' for key 'animals.PRIMARY'

SELECT COUNT(*) FROM areas;    -- 4
SELECT COUNT(*) FROM animals;  -- 6

-- A primary key has a single purpose: to uniquely identify a row.
-- Therefore, it must be unique and non-NULL.
-- If there were two rows with `id = 1`,
-- the DBMS would not know which specific row is being referred to
-- in an `UPDATE`, `DELETE`, or foreign key operation.
-- A name is not a key.
-- Different animals can have the same name (e.g., two named "Luna"),
-- but they are distinguished by their IDs.
-- There is no `UNIQUE` constraint on the `name` column,
-- so the DBMS does not prohibit duplicates.