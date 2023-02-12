#!/usr/bin/python3
"""
City Module inheriting from the BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class
    Attributes:
        state_id (str) -> State.id
        name (str) -> name of the city
    """
    name = ""
    state_id = ""
