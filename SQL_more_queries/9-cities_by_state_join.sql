-- Select columns from cities and states tables
-- Join cities table with states table based on state_id matching id
-- Order the results by cities.id in ascending order
SELECT cities.id AS id , cities.name AS name, states.name AS name
	FROM cities
	INNER JOIN states ON states.id = cities.state_id
	ORDER BY cities.id ASC
