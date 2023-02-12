#!/usr/bin/python3

"""Review model that inherits from the BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class
    Attributes:
        place_id (str) -> Place.id (place being reviewed)
        user_id (str) -> User.id ( Reviwer)
        text (str) -> The review text
    """
    place_id = ""
    user_id = ""
    text = ""
