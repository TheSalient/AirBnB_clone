#!/usr/bin/python3
"""Unittests for BaseModel"""
import unittest
import time
from datetime import datetime
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

    def test_base_model_attributes_type(self):
        """Tests if attributes are of the correct type"""
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertEqual(len(instance.id), 36)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_base_model_updated_at_isEqual_created_at_init(self):
        """Tests if created_at and updated_at attrs are equal at init"""
        base = BaseModel()
        self.assertEqual(base.created_at, base.updated_at)

    def test_base_model_str_method(self):
        """Tests the __str__ method of base model"""
        base = BaseModel()
        base_str = base.__str__()
        self.assertIsInstance(base_str, str)
        self.assertEqual(base_str[:11], '[BaseModel]')
        self.assertEqual(base_str[12:50], '({})'.format(base.id))
        self.assertDictEqual(eval(base_str[51:]), base.__dict__)

    def test_base_model_save_method(self):
        """BaseModel save method alters updated_at date"""
        base = BaseModel()
        time.sleep(0.0001)
        base.save()
        self.assertNotEqual(base.updated_at, base.created_at)

    def test_base_model_to_dict_method(self):
        """BaseModel to_dict method creates accurate dictionary"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['id'], base.id)
        self.assertEqual(base_dict['__class__'], type(base).__name__)
        self.assertEqual(base_dict['created_at'], base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], base.updated_at.isoformat())
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_base_model_dict_to_instance_with_kwargs(self):
        """BaseModel can instantiate new object with dictionary"""
        base = BaseModel()
        base.name = "Betty"
        base.number = 972
        base_dict = base.to_dict()
        new_base = BaseModel(**base_dict)
        new_base_dict = new_base.to_dict()
        self.assertFalse(new_base is base)
        self.assertDictEqual(new_base_dict, base_dict)

    def test_base_model_dict_to_instance_with_empty_kwargs(self):
        """BaseModel can instantiate new object with empty dict"""
        base_dict = {}
        new_base = BaseModel(**base_dict)
        new_base_dict = new_base.to_dict()
        self.assertIsInstance(new_base, BaseModel)
        self.assertIsNotNone(new_base.id)
        self.assertIsNotNone(new_base.created_at)
        self.assertIsNotNone(new_base.updated_at)


if __name__ == '__main__':
    unittest.main()
