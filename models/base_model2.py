import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            if not hasattr(self, 'id'):
                setattr(self, 'id', str(uuid.uuid4()))
            if not hasattr(self, 'created_at'):
                setattr(self, 'created_at', datetime.now())
            if not hasattr(self, 'updated_at'):
                setattr(self, 'updated_at', datetime.now())
        else:
            setattr(self, 'id', str(uuid.uuid4()))
            setattr(self, 'created_at', datetime.now())
            setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """
        Returns a string representation of BaseModel instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

