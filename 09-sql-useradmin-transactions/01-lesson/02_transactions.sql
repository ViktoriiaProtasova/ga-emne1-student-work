-- User A (root)
SELECT CURRENT_USER(), CONNECTION_ID();

SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR'
  AND Name IN ('Oslo', 'Bergen');

START TRANSACTION;

UPDATE city
SET Population = Population - 100000
WHERE CountryCode = 'NOR'
  AND Name = 'Oslo';

UPDATE city
SET Population = Population + 100000
WHERE CountryCode = 'NOR'
  AND Name = 'Bergen';

COMMIT;

START TRANSACTION;

UPDATE city
SET Population = Population + 100000
WHERE CountryCode = 'NOR'
  AND Name = 'Oslo';

UPDATE city
SET Population = Population - 100000
WHERE CountryCode = 'NOR'
  AND Name = 'Bergen';

COMMIT;

-- User B (city_reader)
SELECT CURRENT_USER(), CONNECTION_ID();

SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR'
  AND Name IN ('Oslo', 'Bergen');