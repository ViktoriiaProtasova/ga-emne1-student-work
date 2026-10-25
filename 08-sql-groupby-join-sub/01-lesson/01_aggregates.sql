USE world;
SELECT *
FROM country;

SELECT MAX(Population)
FROM country;

SELECT SUM(Population) AS total_population,
       AVG(Population) AS avg_population,
       MIN(Population) AS min_population,
       MAX(Population) AS max_population
FROM city
WHERE CountryCode = 'NOR';

SELECT Name, Population / 1000000 AS pop_millions
FROM country
WHERE Population > 1000000
ORDER BY  pop_millions DESC;

SELECT Continent, Region,
       COUNT(*) AS country_count,
       SUM(Population) AS population
FROM country
GROUP BY Continent, Region
ORDER BY Continent, population DESC;

SELECT Continent,
       COUNT(*),
       SUM(Population)
FROM country
GROUP BY Continent
ORDER BY Continent, SUM(Population) DESC;


SELECT SUM(Population) , COUNT(*)
FROM country
ORDER BY Continent, SUM(Population) DESC;


SELECT Continent, COUNT(*) AS country_count
FROM country
WHERE Population > 10000000
GROUP BY Continent
HAVING country_count >= 5
ORDER BY country_count;


SELECT CountryCode, COUNT(*), AVG(Population)
FROM city
GROUP BY CountryCode
HAVING COUNT(*) >= 20
ORDER BY AVG(Population) DESC;