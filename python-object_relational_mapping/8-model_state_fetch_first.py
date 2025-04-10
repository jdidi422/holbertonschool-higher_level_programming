#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Check input arguments
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} "
              "<mysql username> <mysql password> <database name>")
        sys.exit(1)

    # DB connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create tables
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print the first states
    state = session.query(State).order_by(State.id).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
    session.close()