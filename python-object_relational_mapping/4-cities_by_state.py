#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute SQL query to select all cities sorted by id
    cur.execute("SELECT * FROM cities ORDER BY id ASC")

    # Fetch all the rows returned by the query
    cities = cur.fetchall()

    # Print each city
    for city in cities:
            print(city)
    # Close cursor and connection
    cur.close()
    db.close()
