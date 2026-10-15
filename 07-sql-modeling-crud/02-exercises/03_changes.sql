-- Task 6.1 Add a status

ALTER TABLE  animals
ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'new';

SELECT status
FROM animals;

INSERT INTO animals (name, species, area_id)
VALUES ('Nova', 'cat',  1);

SELECT id, name, weight, admitted_on, status
FROM animals;

-- Animal 'Nova' has NULL in weight and admitted_on but 'new' in status column
-- Because we set the as DEFAULT value

-- Task 6.2 Change the default value

ALTER TABLE animals
MODIFY COLUMN status VARCHAR(20) NOT NULL DEFAULT 'available';

INSERT INTO animals (name, species, area_id)
VALUES ('Oreo', 'cat',  1);

SELECT id, name, weight, admitted_on, status
FROM animals;

-- The new default value didn't affect existing rows

-- Task 6.3 Give the name field more space

ALTER TABLE animals
MODIFY COLUMN name VARCHAR(60) NOT NULL;

DESCRIBE animals;

-- `ALTER TABLE` changes the rules governing how a table stores data
-- (such as the space allocated to a column or the constraints in effect),
-- whereas `UPDATE` modifies the actual stored data within individual rows.

-- Task 6.4 Remove a column and a table

CREATE TABLE IF NOT EXISTS scratch_labels(
    id INT AUTO_INCREMENT,
    title VARCHAR(20),
    PRIMARY KEY (id)
);

INSERT INTO scratch_labels (title)
VALUES ('Temporary label');

SELECT title
FROM scratch_labels;

ALTER TABLE scratch_labels
DROP COLUMN title;

DROP TABLE scratch_labels;

-- ALTER TABLE DROP COLUMN removes column with all rows
-- DROP TABLE removes the table at all

-- Checkpoint

SELECT COUNT(*) AS areas_count
FROM areas;

SELECT COUNT(*) AS animals_count
FROM animals;

SELECT name
FROM animals;

-- Task 7.1 Two animals with the same name

SELECT id, name
FROM animals
WHERE name = 'Luna' AND species = 'cat';

UPDATE animals
SET weight = 3.90
WHERE id = 1;

SELECT id, name, weight
FROM animals
WHERE name = 'Luna';

-- If we had simply used `WHERE name = 'Luna'` in the update
-- Both rows would be updated

-- Task 7.2 Two changes in one statement

SELECT id, name
FROM animals
WHERE name = 'Rex' AND species = 'dog';

UPDATE animals
SET name = 'Rex Jr', weight = 19.20
WHERE id = 3;

SELECT *
FROM animals
WHERE id = 3;

-- Task 7.3 Move an animal

SELECT id, name
FROM animals
WHERE Name = 'Luna' AND species = 'rabbit';

SELECT id, name
FROM areas
WHERE name = 'Quiet Zone'; -- 4

UPDATE animals
SET area_id = 4 -- Quiet Zone
WHERE id = 6;

SELECT *
FROM animals
WHERE species = 'rabbit';

-- We change the foreign key instead of the section name
-- because the foreign key refers on the areas table where the section name is stored

-- Task 7.4 A known value becomes unknown again

SELECT id, name
FROM animals
WHERE name = 'Nala';

UPDATE animals
SET weight = 14.60
WHERE id = 4;

SELECT id, name, weight
FROM animals
WHERE id = 4;

UPDATE animals
SET weight = NULL
WHERE id = 4;

SELECT id, name, weight
FROM animals
WHERE weight IS NULL;

-- Difference between NULL and 0 in a numeric column (e.g. weight):
-- NULL = weight is unknown, 0 = weight is known and equals zero.

-- SELECT * FROM animals WHERE weight = NULL;     -- returns nothing (comparison with NULL is never true)
-- SELECT * FROM animals WHERE weight IS NULL;    -- returns animals with unknown weight
-- SELECT * FROM animals WHERE weight = 0;        -- returns animals whose weight is exactly 0
