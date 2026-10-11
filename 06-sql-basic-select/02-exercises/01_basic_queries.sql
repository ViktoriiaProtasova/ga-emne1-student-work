-- Task 2: Database concepts

-- Task 2.1: What do the different parts do?
-- A database is an organized collection of data stored in tables, so it is
-- easy to find, change and connect information. In our setup, World is the
-- database. It holds the tables city, country and countrylanguage.
-- A DBMS (database management system) is the program that manages the
-- database: it stores the data, receives queries, keeps the data correct and
-- controls access. In our setup, MySQL is the DBMS.
-- SQL (Structured Query Language) is the language we use to talk to the DBMS.
-- For example, SELECT Name FROM country; asks MySQL for all country names.
-- DataGrip is the client: a graphical tool where we connect to the MySQL
-- server, write and run SQL, and browse tables and results.
-- Docker runs MySQL in a container, so we do not have to install and
-- configure MySQL manually, and every computer gets the same environment.

-- Task 2.2: Table, row and column
-- One row in city represents one city (for example one record for Oslo).
-- ID: a unique number that identifies the city.
-- Name: the name of the city.
-- CountryCode: a three-letter code for the country the city belongs to.
-- District: the district, state or region where the city is located.
-- Population: the number of people living in the city.
-- Data types (In DataGrip, they look like this:):
--   ID         INT       (whole number)
--   Name       CHAR(35)  (text, up to 35 characters)
--   Population INT       (whole number)
-- Names and population need different data types because they hold different
-- kinds of data. A name is text, so it needs a text type. A population is a
-- number, so it needs a numeric type. With a number type we can sort by size,
-- compare values and calculate (SUM, AVG), which does not work properly on text.

-- Task 2.3: Keys and relationships
-- The primary key in city is ID. The primary key in country is Code.
-- city.CountryCode is a foreign key. It refers to country.Code, so each city
-- points to exactly one country. This links the two tables together.
-- Many cities can have the same CountryCode because one country has many
-- cities, for example many cities have the code NOR.
-- A city name is a bad primary key because it is not unique. Different
-- cities can have the same name (for example cities called Springfield in
-- different countries), and a primary key must identify exactly one row.
-- A name can also change over time, while a key should be stable.

-- 3 Velg kolonner med SELECT Oppgave

-- 3.1 Utforsk landtabellen

SELECT *
FROM country;

-- Oppgave 3.2 En kort landoversikt

SELECT Code, Name, Continent
FROM country;

SELECT Name, Code, Continent
FROM country;

-- Oppgave 3.3 Andre opplysninger om byene

SELECT Name, CountryCode, District
FROM city;

-- 4 Filtrer rader med WHERE

-- Oppgave 4.1 Byer i Japan

SELECT CountryCode, Name, District, Population
FROM city
WHERE CountryCode = 'JPN';

-- Oppgave 4.2 Søramerikanske land

SELECT Name, Population
FROM country
WHERE Continent = 'South America';

-- Oppgave 4.3 Små land etter areal

SELECT  Name, SurfaceArea
FROM country
WHERE SurfaceArea <= 1000.00;

-- Oppgave 4.4 Et annet distrikt

SELECT  Name, CountryCode, District
FROM city
WHERE District <> 'California';

-- 5 Kombiner betingelser Oppgave

-- 5.1 Store brasilianske byer

SELECT Name, Population
FROM city
WHERE CountryCode = 'BRA' AND Population > 500000;

-- Oppgave 5.2 Et intervall for folketall

SELECT Name, Population
FROM country
WHERE Population > 2000000 AND Population < 8000000;

-- Oppgave 5.3 To land og ett felles krav

SELECT  Name, CountryCode, Population
FROM city
WHERE (CountryCode ='AUS' OR CountryCode = 'NZL')
    AND Population > 200000;

-- 6 Sortering og avgrensning

--  Oppgave 6.1 Land i alfabetisk rekkefølge

SELECT  Name, Region
FROM country
WHERE Continent = 'Asia'
ORDER BY Name;

-- Oppgave 6.2 De største landene etter areal

SELECT  Name, SurfaceArea
FROM country
ORDER BY SurfaceArea DESC, Code
LIMIT 8;

-- Oppgave 6.3 Sortering på flere kolonner

SELECT Name, District, Population
FROM city
WHERE CountryCode = 'CAN'
ORDER BY District, Population DESC, ID;

-- Oppgave 6.4 Fem vilkårlige eller fem bestemte

SELECT Code, Name
FROM country
ORDER BY Name
LIMIT 5;

-- 7 Tekstsøk med LIKE

-- Oppgave 7.1 Landnavn med en bestemt start

SELECT Name
FROM country
WHERE Name LIKE 'Br%'
ORDER BY Name;

-- Oppgave 7.2 Slutten eller midten av navnet

SELECT Name
FROM country
WHERE Name LIKE '%stan'
ORDER BY Name;

SELECT Name
FROM country
WHERE Name LIKE '%is%'
ORDER BY Name;

-- Oppgave 7.3 Nøyaktig ett tegn

SELECT Name
FROM country
WHERE Name LIKE '_a%'
ORDER BY Name;

SELECT Name
FROM country
WHERE Name LIKE '____'
ORDER BY Name;

-- 8 Lister og manglende verdier

-- Oppgave 8.1 Tre land med IN

SELECT Name, CountryCode, Population
FROM city
WHERE CountryCode IN ('FRA', 'ESP', 'PRT')
    AND Population > 300000
ORDER BY CountryCode, Name;

-- Oppgave 8.2 IN og OR

SELECT Name, CountryCode, Population
FROM city
WHERE (CountryCode = 'FRA'
      OR CountryCode = 'ESP'
      OR CountryCode = 'PRT')
  AND Population > 300000
ORDER BY CountryCode, Name;

-- Oppgave 8.3 Manglende levealder

SELECT  Name, LifeExpectancy
FROM country
WHERE LifeExpectancy IS NULL;

-- Oppgave 8.4 Registrert levealder

SELECT  Name, LifeExpectancy
FROM country
WHERE LifeExpectancy IS NOT NULL
ORDER BY LifeExpectancy DESC, Code
LIMIT 10;


-- 9 Tell rader med COUNT

-- Oppgave 9.1 Hvor mange byer og land

SELECT COUNT(*) AS CountryCount
FROM country;

SELECT COUNT(*) AS CityCount
FROM city;

-- Oppgave 9.2 Tell et filtrert utvalg

SELECT COUNT(*) AS LargeCityCount
FROM city
WHERE CountryCode = 'MEX'
    AND Population > 500000;

SELECT Name, Population
FROM city
WHERE CountryCode = 'MEX'
  AND Population > 500000;

-- Oppgave 9.3 Hvor mange verdier mangler

SELECT COUNT(*)
FROM country
WHERE LifeExpectancy IS NULL;

SELECT COUNT(*)
FROM country
WHERE LifeExpectancy IS NOT NULL;

-- 10 Les og rett spørringer

-- Oppgave 10.1 Tegn har forsvunnet

SELECT Name, Population
FROM city
WHERE CountryCode = 'ITA';

-- Oppgave 10.2 Tekstverdier

SELECT Name, Population
FROM city
WHERE CountryCode = 'ITA';

-- Oppgave 10.3 Hvilke byer slipper gjennom

SELECT Name, CountryCode, Population
FROM city
WHERE (CountryCode = 'EGY'
   OR CountryCode = 'MAR')
   AND Population > 1000000;

-- Oppgave 10.4 Tomt resultat betyr ikke alltid riktige betingelser

SELECT Name, HeadOfState
FROM country
WHERE HeadOfState IS NULL;

-- Utfordring 1 Land i tre regioner

SELECT Name, Region, Population, SurfaceArea
FROM country
WHERE Region IN ('Caribbean', 'Polynesia' 'Micronesia')
    AND Population > 100000
    AND SurfaceArea < 10000
ORDER BY Region, Population DESC, Code;

SELECT COUNT(*)
FROM country
WHERE Region IN ('Caribbean', 'Polynesia' 'Micronesia')
  AND Population > 100000
  AND SurfaceArea < 10000;

-- Utfordring 2 Offisielle språk

SELECT CountryCode, Language, Percentage
FROM countrylanguage
WHERE CountryCode = 'IND'
    AND IsOfficial = 'T'
ORDER BY Percentage DESC, Language;

SELECT CountryCode, Language, Percentage
FROM countrylanguage
WHERE Language = 'Spanish'
    AND IsOfficial = 'T'
ORDER BY Percentage DESC;

SELECT COUNT(*)
FROM countrylanguage
WHERE Language = 'Spanish'
  AND IsOfficial = 'T';

-- Utfordring 3 To forskjellige måter å telle på

SELECT COUNT(*) AS CountryCount
FROM country;

SELECT COUNT(LifeExpectancy) AS KnownLifeExpectancyCount
FROM country;

-- Utfordring 4 Undersøk like bynavn

SELECT ID, Name, CountryCode, District
FROM city
WHERE Name LIKE 'San Jose'
ORDER BY CountryCode, ID;

SELECT ID, Name, CountryCode, District
FROM city
WHERE ID = 3803;

-- Utfordring 5 Et tomt utvalg

SELECT Name, Population
FROM city
ORDER BY Population DESC
LIMIT 1;

SELECT Name, Population
FROM city
WHERE Population > 10500000;

SELECT COUNT(*)
FROM city
WHERE Population > 10500000;

-- Version 1 returns zero rows: no city has a population above the limit,
-- so the result set is empty.
-- Version 2 returns one row with the value 0: COUNT(*) always returns one
-- row, and here the count of matching rows is 0.
-- Zero rows means "nothing was found"; one row with 0 means "the answer is 0".

-- Utfordring 6 Dine egne spørsmål

-- Question 1 (three conditions): Which European countries have more than
-- 5 million people, a surface area under 100,000 km2, and a life expectancy
-- above 75 years?
-- sorted alphabetically.

-- Conditions: Europe AND more than 5 million people AND surface area under
-- 100,000 km2 AND life expectancy above 75 years.
-- sorted alphabetically.
-- Checked: every row meets all four conditions; loosening one condition
-- gives more rows, so each condition has an effect.

SELECT Name, Population
FROM country
WHERE Continent = 'Europe'
    AND Population > 5000000
    AND SurfaceArea < 100000
    AND LifeExpectancy > 75
ORDER BY Name;


-- Question 2 (text pattern with LIKE): Which countries have a name that
-- ends with "land"? Sorted alphabetically.

-- Uses LIKE with the pattern '%land' (anything before "land"),
-- sorted alphabetically.
-- Checked: every name in the result ends with "land".

SELECT Name
FROM country
WHERE Name LIKE '%land'
ORDER BY Name;

-- Question 3 (sorted top list with LIMIT): Which are the 10 most populated
-- cities in the database?

-- Sorted from the largest population down, limited to 10 rows.
-- Checked: the population values decrease down the list and there are
-- exactly 10 rows.

SELECT Name, Population
FROM city
ORDER BY Population DESC
LIMIT 10;

-- Question 4 (COUNT): How many countries are in Africa?

-- COUNT(*) returns the number of matching rows as a single value.
-- Checked: running the same query with SELECT Name instead of COUNT(*)
-- gives a list with the same number of rows.

SELECT COUNT(*) AS AfricanCountries
FROM country
WHERE Continent = 'Africa';