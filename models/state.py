#!/usr/bin/python3
"""This is the state class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """for filestorage to match state_id with state.id"""
            city_list = []
            c_dict = models.storage.all(City)
            for c in c_dict.values():
                if self.id == c.state_id:
                    city_list.append(c)
            return city_list
