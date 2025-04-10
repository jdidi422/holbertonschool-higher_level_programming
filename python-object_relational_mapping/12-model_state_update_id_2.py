#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

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

    update_state = update(State).where(State.id == 2).values(name='New Mexico')
    session.execute(update_state)
    session.commit()
    session.close()