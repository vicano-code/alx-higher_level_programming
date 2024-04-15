#!/usr/bin/python3

'''
 lists all State objects that contain the letter a from the
 database hbtn_0e_6_usa
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session maker
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # Query all State objects that contain the letter a from the database
    states = session.query(State).filter(State.name.like('%a%'))

    # Print the list of states
    for state in states.all():
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
