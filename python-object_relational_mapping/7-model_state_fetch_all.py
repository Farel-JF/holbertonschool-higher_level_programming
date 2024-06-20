#!/usr/bin/python3
"""
Script to list all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create database engine
    user, passwd, database = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, database), pool_pre_ping=True)
    

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session factory
    DBSession = sessionmaker(bind=engine)

    # Create a session
    session = DBSession()

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()

    # Print results as specified
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
