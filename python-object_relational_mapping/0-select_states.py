#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
        # Connect to MySQL database
        db = MySQLdb.connect(
            host='localhost',
            user=username,
            password=password,
            database=database,
            port=3306)

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query to fetch all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        states = cursor.fetchall()

        # Display results as per example format
        for state_row in states_row:
            print(state_row)

        # Close cursor and connection
        cursor.close()
        db.close()
