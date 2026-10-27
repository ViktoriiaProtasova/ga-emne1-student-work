CREATE USER 'city_reader'@'%'
IDENTIFIED BY 'ReadOnly_09!';

GRANT SELECT ON world.city
TO 'city_reader'@'%';

SHOW GRANTS FOR 'city_reader'@'%';

SELECT CURRENT_USER(), CONNECTION_ID();