#!/usr/bin/python3
"""
contains the class definition of a City.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy import ForeignKey
import sys


class City(Base):
    """
    State class that defines the structure of states table
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


if __name__ == "__main__":
    # Check input arguments
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} "
              "<username> <password> <database>")
        sys.exit(1)

    # Create an engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)