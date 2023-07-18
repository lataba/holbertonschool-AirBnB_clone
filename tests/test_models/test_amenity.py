#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityClass(unittest.TestCase):
    """ Tests amenity class """

    def test_class(self):

        obj = Amenity()

        """ Verify that the object is an instance of the Amenity class  """
        self.assertIsInstance(obj, Amenity)

        """ Verify that the object is an instance of the BaseModel class   """
        self.assertIsInstance(obj, BaseModel)

        """ Verify that the object has the correct attributes """
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", Amenity.__dict__)

    def test_attributes_assignment(self):

        amenity = Amenity()
        amenity.name = "Pet allowed"

        """ Verify that the object has the correct attributes """
        self.assertEqual(amenity.name, "Pet allowed")

    def test_to_dict(self):

        amenity = Amenity()
        amenity.name = "Pet allowed"

        amenity_dict = amenity.to_dict()

        """ Verify that the object has the correct attributes """
        self.assertEqual(amenity_dict["name"], "Pet allowed")
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)


if __name__ == '__main__':
    unittest.main()
