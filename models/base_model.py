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
 
def __init__(self, *args, **kwargs):
    """Initializes class instances
    
    If kwargs is not empty its creates an instance
    
    """
if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    created = datetime.fromisoformat(value)
                    self.created_at = created
                elif key == 'updated_at':
                    updated = datetime.fromisoformat(value)
                    self.updated_at = updated
                else:
                    setattr(self, key, value)
else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()