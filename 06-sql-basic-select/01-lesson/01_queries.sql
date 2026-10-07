SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR';

SELECT Name, Population
FROM city
WHERE Population > 1000000;

SELECT Name, Population
FROM city
WHERE CountryCode = 'SWE';

SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR'
    AND Population > 200000;

SELECT Name, Population
FROM city
WHERE (CountryCode = 'NOR'
       OR CountryCode = 'SWE')
  AND Population > 200000;

SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR'
ORDER BY Population DESC;

SELECT Name, Population
FROM city
ORDER BY Population DESC, ID ASC
LIMIT 5;

SELECT Name, Population
FROM city
WHERE CountryCode = 'SWE'
  AND Population > 100000
ORDER BY Population DESC;

SELECT Name
FROM city
WHERE Name LIKE 'N%'
ORDER BY Name;

SELECT Name
FROM city
WHERE Name LIKE 'O__o'
ORDER BY Name;

SELECT Name
FROM city
WHERE Name LIKE '%land%'
ORDER BY Name;

SELECT Name, CountryCode
FROM city
WHERE CountryCode IN
    ('NOR', 'SWE', 'DNK')
ORDER BY CountryCode, Name;

SELECT Name, IndepYear
FROM country
WHERE IndepYear IS NULL;

SELECT COUNT(*) AS CityCount
FROM city
WHERE CountryCode = 'NOR';

SELECT Name, Population
FROM country
WHERE Continent = 'Europe'
  AND Population > 5000000;

SELECT COUNT(*) AS CountryCount
FROM country
WHERE Continent = 'Europe'
  AND Population > 5000000;