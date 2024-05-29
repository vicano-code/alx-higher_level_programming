#!/usr/bin/python3

'''
adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    # add row to table
    row = State(name="Louisiana")
    session.add(row)
    session.commit()

    # query
    query = session.query(State).filter(State.name == "Louisiana")
    state = query.first()
    print(f"{state.id}")

    # Close the session
    session.close()
