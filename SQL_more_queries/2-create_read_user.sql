-- Create the database if it does not exist
-- Create the MySQL server user user_0d_2 if it does not exist
-- Grant all privileges to the user on the entire MySQL server
-- Set the password for the user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
ALTER USER user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
