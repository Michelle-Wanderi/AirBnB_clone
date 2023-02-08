# parent class BaseModel that defines common attributes/methods for other classes

import uuid
from datetime import datetime


class BaseModel():
    """This is the parent class where all the classes will inherit from

   Attributes:
   id: the basemodel id
   created_at : the datetime at creation
   updated_at : the datetime of last update 
    
    
    
    """
