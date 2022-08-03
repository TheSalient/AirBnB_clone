#!/usr/bin/python3
"""Base Model Superclass module"""
import uuid
import datetime
import models


class BaseModel:
    """The base_model superclass"""

    def __init__(self):
        """__init__ method for the superclass"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """string representatipon of the model instance"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute to the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary of all key/value pairs of __dict__
        of the BaseModel instance"""
        bm_dict = dict(self.__dict__)
        bm_dict['__class__'] = type(self).__name__
        bm_dict['created_at'] = bm_dict['created_at'].isoformat()
        bm_dict['updated_at'] = bm_dict['updated_at'].isoformat()
        return bm_dict
