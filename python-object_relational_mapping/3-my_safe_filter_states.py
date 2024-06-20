#!/usr/bin/python3
"""
Script to display states from hbtn_0e_0_usa where name matches given argument
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

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Prepare SQL query with parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch all the rows returned by the query
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
