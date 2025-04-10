#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import (create_engine)
import sys
from model_state import Base, State
from model_city import City
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

    result = session.query(State, City).join(City).order_by(State.id, City.id)
    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()