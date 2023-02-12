#!/usr/bin/python3

"""State Model that inherits from the BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class
    Attributes:
        name(str) -> Name of the state
    """
    name = ""
