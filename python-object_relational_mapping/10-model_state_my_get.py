#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Check input arguments
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} "
              "<mysql username> <mysql password> <database name>"
              "<state name to search>")
        sys.exit(1)

    searched_state = sys.argv[4]

    # DB connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create tables
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print the first states
    states = session.query(State).filter(State.name == searched_state).all()

    if states:
        for state in states:
            print(f"{state.id}")
            break
    else:
        print("Not found")

    session.close()