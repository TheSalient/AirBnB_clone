#!/usr/bin/env  python3

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Limestone"

    @classmethod
    def tearDownClass(cls):
        del cls.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.amenity1.name), str)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenity1), True)


if __name__ == "__main__":
    unittest.main()
