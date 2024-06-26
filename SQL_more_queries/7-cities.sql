-- Create the database if it does not exist
-- Create the cities table if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
