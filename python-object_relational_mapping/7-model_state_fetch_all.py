#!/usr/bin/python3
"""
Script to list all cities of a specific state from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect
    (
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Prepare SQL query to select all cities of the specified state, sorted by id
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cur.execute(query, (state_name,))

    # Fetch all the rows returned by the query
    cities = cur.fetchall()

    # Print each city
    for city in cities:
        print(city)
    # Close cursor and connection
    cur.close()
    db.close()

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                            sys.argv[2],
                                                            sys.argv[3]),
                                                            pool_pre_ping=True)
    Base.metadata.create_all(engine)
