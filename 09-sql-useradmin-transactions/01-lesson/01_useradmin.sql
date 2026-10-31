CREATE USER 'city_reader'@'%'
IDENTIFIED BY 'ReadOnly_09!';

GRANT SELECT ON world.city
TO 'city_reader'@'%';

SHOW GRANTS FOR 'city_reader'@'%';

SELECT CURRENT_USER(), CONNECTION_ID();


-- Connect as city_reader in DataGrip
-- Check who is logged in

SELECT CURRENT_USER(), CONNECTION_ID(); -- city_reader

-- In the new console, this should be allowed

SELECT Name, Population
FROM city;

-- This is to be rejected

SELECT *
FROM country;

UPDATE city
SET Population = 100
WHERE CountryCode = 'NOR'
  AND Name = 'Oslo';