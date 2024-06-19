-- Select columns from cities and states tables
-- Join cities table with states table based on state_id matching id
-- Order the results by cities.id in ascending order
SELECT cities.id AS cities_id , cities.name AS cities_name, states.name AS state_name
	FROM cities
	INNER JOIN states ON cities.state_id = states.id
	ORDER BY cities.id ASC
