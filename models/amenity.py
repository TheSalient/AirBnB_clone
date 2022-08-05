#!/usr/bin/env  python3
'''
    Implementation for the Amenity with name public attributes.
'''

from models.base_model import BaseModel, Base
import os
import models


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenity with name public attributes.
    '''
    name = ""
