#!/usr/bin/python3
'''
    Implementation for the City with name state_id public attributes.
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
        Implementation for the City with name state_id public attributes.
    '''
    state_id = ""
    name = ""
