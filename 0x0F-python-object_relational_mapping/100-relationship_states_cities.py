#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


# Create all tables in the database
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session maker
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California" and the City "San Francisco"
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add the objects to the session and commit
    session.add_all([new_state, new_city])
    session.commit()

    # Close the session
    session.close()
