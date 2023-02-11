#!/usr/bin/python3
from models.base_model import BaseModel

"""
amenity module inheriting from the BaseModel
"""


class Amenity(BaseModel):
    """
    Amenity Class
    attributes:
        name (str) -> Name of the amenity
    """
    name = ""
