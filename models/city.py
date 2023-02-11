#!/usr/bin/python3
from models.base_model import BaseModel

"""
City Module inheriting from the BaseModel
"""


class City(BaseModel):
    """City Class
    Attributes:
        state_id (str) -> State.id
        name (str) -> name of the city
    """
    name = ""
    state_id = ""
