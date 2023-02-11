#!/usr/bin/python3
from models.base_model import BaseModel

"""
State Model that inherits from the BaseModel
"""


class State(BaseModel):
    """State class
    Attributes:
        name(str) -> Name of the state
    """
    name = ""
