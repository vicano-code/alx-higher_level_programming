#!/usr/bin/python3

'''
update table - changes the name of a State object from
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

# update row in table
row = session.query(State).filter(State.id == 2).first()
row.name = "New Mexico"
session.commit()

# Close the session
session.close()
