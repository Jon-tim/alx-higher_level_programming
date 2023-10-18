-- list cities in the database
SELECT cities.id, cities.name
NATURAL JOIN states.name
ORDER BY cities.id ASC;
