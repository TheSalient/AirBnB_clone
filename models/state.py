#!/usr/bin/env  python3
'''
    Implementation for the State with name public attributes.
'''

from models.base_model import BaseModel, Base
import os
import models


class State(BaseModel, Base):
    '''
        Implementation for the State with name public attributes.
    '''
    name = ""
