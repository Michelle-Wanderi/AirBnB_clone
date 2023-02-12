#!/usr/bin/python3

"""Places model, inheritting from the BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class
    Attributes:
        city_id (str) -> City.id
        user_id (str) -> City.id
        name (str) -> name of place
        description (str) -> description of place
        number_rooms (int) -> Number of rooms: default is 0
        number_bathrooms (int) -> Number of bathrooms: default is 0
        max_guest (int) -> Maximum number of guests: default is 0
        price_by_night (int) -> charing rate by night: default is 0
        latitude (float) -> Geographical lattitude
        longitude (float) -> Geographical longitude
        amenity_ids (list) -> list of strings of ameninty ID's
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
