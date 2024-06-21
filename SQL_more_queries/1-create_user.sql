-- This script creates the MySQL server user user_0d_1
-- The user should have all privileges on the MySQL server
-- The user password should be set to user_0d_1_pwd
-- If the user already exists, the script should not fail

-- Create the MySQL server user user_0d_1 if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Grant all privileges to the user on the entire MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
