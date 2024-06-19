#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Assign command-line arguments to variables
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host='localhost',
            user=username,
            password=password,
            database=database,
            port=3306
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query to fetch all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        states = cursor.fetchall()

        # Display results as per example format
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        sys.exit(1)

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if db:
            db.close()
