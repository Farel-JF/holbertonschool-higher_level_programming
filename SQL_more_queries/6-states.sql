-- Create the database if it does not exist
-- Create the table if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT NOT NULL UNIQUE ,
    name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);
