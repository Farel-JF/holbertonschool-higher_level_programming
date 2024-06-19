#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import agrv

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # Create a cursor object
    cursor = db.cursor()
    # Execute the query to fetch all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all rows
    states = cursor.fetchall()
    # Display results as per example format
    for state in states:
            print(state)
    # Close the cursor and database connection
    cursor.close()
    db.close()
