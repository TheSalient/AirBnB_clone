#!/usr/bin/python3
'''
    Implementation for the City with name state_id public attributes.
'''
from models.base_model import BaseModel, Base
import os


class City(BaseModel, Base):
    '''
        Implementation for the City with name state_id public attributes.
    '''
    state_id = ""
    name = ""
