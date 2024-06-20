#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        )
    # Create a cursor object
    curs = db.cursor()
    # Execute the query to fetch all states sorted by id
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all rows
    states = curs.fetchall()
    # Display results as per example format
    for state in states:
        print(state)
    # Close cursor and connection
    curs.close()
    db.close()
