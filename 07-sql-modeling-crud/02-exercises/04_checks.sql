-- Task 9.1 Primary keys with different names
SELECT *
FROM country;

SELECT *
FROM countrylanguage;

-- country: the primary key is the single column Code.
-- countrylanguage: the primary key consists of two columns, CountryCode and Language.

-- countrylanguage has a composite primary key,
-- because it combines two columns (CountryCode and Language) to identify a row.

-- A row in countrylanguage describes one language in one country.
-- The same language is spoken in many countries (for example, English appears for NOR, SWE, USA and others),
-- so a language value alone would match several rows.
-- Likewise, one country has many languages, so the country code alone is not unique either.
-- Only the combination of CountryCode and Language (for example, NOR + English)
-- occurs exactly once, so both columns are needed to identify a row.

-- Task 9.2 Examine language information

SELECT CountryCode, Language, Percentage
FROM countrylanguage
WHERE CountryCode = 'NOR';

SELECT Name
FROM country
WHERE Code = 'NOR';

-- Exercise 10.1 Commas and parentheses

CREATE TABLE scratch_tags (
 id INT AUTO_INCREMENT,
 label VARCHAR(30) NOT NULL,
 PRIMARY KEY (id)
);

-- A comma must separate each column or constraint definition,
-- so one is missing after label VARCHAR(30) NOT NULL.
-- No comma may follow the last definition,
-- so the one after PRIMARY KEY (id) must be removed.

-- Task 10.2 Columns and values

SELECT area_id
FROM areas
WHERE name = 'Cat Wing';

INSERT INTO animals (name, species, area_id)
VALUES ('Tyra', 'cat', 1);

-- Task 10.3 Valid SQL with incorrect selection

SELECT id
FROM animals
WHERE name = 'Luna' and species = 'rabbit';

UPDATE animals
SET weight = 2.50
WHERE id = 6;

-- Task 10.4 Deletion is not a SELECT

SELECT id
FROM animals
WHERE name = 'Nova';

DELETE FROM animals
WHERE id = 9;