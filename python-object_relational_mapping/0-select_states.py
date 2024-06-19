#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""

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
        cursor = db.cursor()

        # Execute the query to fetch all states sorted by id
        cur.execute("""SELECT * FROM states ORDER BY id""")

        # Fetch all rows
        states = cursor.fetchall()

         # Print each row
        for row in query_rows:
            print(row)

        # Close cursor and connection
        cursor.close()
        db.close()
