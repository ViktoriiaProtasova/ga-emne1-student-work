-- Hvis alle byer med befolkninger er flere innbygninger enn gjennomsnittet
-- av innbyggere for byer i hele verden

SELECT AVG(Population)
FROM city; -- 350468.2236


SELECT Name, Population
FROM city
WHERE Population > 350468.2236
ORDER BY Population;


SELECT Name, Population
FROM city
WHERE Population > (
 SELECT AVG(Population)
 FROM city
)
ORDER BY Population DESC;


SELECT Code, Name
FROM country
WHERE Code IN (
    SELECT CountryCode
    FROM city
    WHERE Population >= 1000000
)
ORDER BY Name;