#!/usr/bin/python3

'''
deletes all State objects with a name containing the letter a from
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

    # deletes all State objects with a name containing the letter a
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states.all():
        session.delete(state)

    # Commit the session to save the changes to the database
    session.commit()

    # Close the session
    session.close()
