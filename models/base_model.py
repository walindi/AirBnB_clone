#!/usr/bin/python3
"""base class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Class constructor

        Args:
            *args (any): Unused
            **kwargs (dict): k/v pairs of attributes
        """

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = v

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Public instance method
        Updates the public intance attribute updated_at with
        the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance
        """

        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """Return string representation of the BaseModel instance"""

        className = self.__class__.__name__
        return f"[{className}] ({self.id}) {self.__dict__}"
