-- Select the id of the state California
-- Use the id to fetch cities of California, sorted by cities.id
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
