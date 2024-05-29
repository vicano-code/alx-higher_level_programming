#!/usr/bin/python3

'''
contains the class definition of a State and an
instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    class definition of a State and an
    instance Base = declarative_base()
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    '''define the relationship with the city class'''
    cities = relationship("City", backref="state")
