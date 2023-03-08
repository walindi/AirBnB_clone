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

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the BaseModel instance"""

        className = self.__class__.__name__
        return f"[{className}] (self.id) self.__dict__"
