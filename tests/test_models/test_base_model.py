#!/usr/bin/python3
"""Unittests for BaseModel"""
import unittest
import time
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class TestBaseModel that holds all the test cases"""

    def test_base_model_class_membership_and_attributes(self):
        """Tests if base model the right class with correct attributes"""
        inst = BaseModel()
        self.assertIsInstance(inst, BaseModel)
        self.assertIsNotNone(inst.id)
        self.assertIsNotNone(inst.created_at)
        self.assertIsNotNone(inst.updated_at)


if __name__ == '__main__':
    unittest.main()
