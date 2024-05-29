#!/usr/bin/python3

'''
prints all City objects from the database hbtn_0e_14_usa
format: (<state name>: (<city id>) <city name>)
'''
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
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

    for a in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(a[0], a[1], a[2]))

    # Close the session
    session.close()
