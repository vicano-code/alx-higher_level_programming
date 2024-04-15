#!/usr/bin/python3

'''
prints the State object with the name passed as argument from
the database hbtn_0e_6_usa
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

    # Query State objects from the database with the name passed as argument
    state = session.query(State).filter(State.name == sys.argv[4]).all()

    # Print
    if state:
        print("f{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
