#!/usr/bin/python3
"""The User class that inheirits from BaseModel superclass"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class
    Attributes:
        email (str): email of the user
        password (str): password of user
        first_name (str): FirstName of user
        last_name (str): LastName of User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
