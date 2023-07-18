#!/usr/bin/python3

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCityClass(unittest.TestCase):
    """Tests for City class"""

    def test_class(self):
        obj = City()

        """ Verify that obj is an instance of City and BaseModel """
        self.assertIsInstance(obj, City)

        """ Verify that obj is an instance of BaseModel  """
        self.assertIsInstance(obj, BaseModel)

        """ Verify that obj has the correct attributes """
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("state_id", City.__dict__)
        self.assertIn("name", City.__dict__)

        """ Verify that obj has the correct attributes """
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_attributes_assignment(self):
        city = City()
        city.state_id = "12345"
        city.name = "New York"

        """ Verify that obj has the correct attributes """
        self.assertEqual(city.state_id, "12345")
        self.assertEqual(city.name, "New York")

    def test_to_dict(self):

        city = City()
        city.state_id = "12345"
        city.name = "New York"

        city_dict = city.to_dict()

        """ Verify that obj has the correct attributes """
        self.assertEqual(city_dict["state_id"], "12345")
        self.assertEqual(city_dict["name"], "New York")
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)


if __name__ == '__main__':
    unittest.main()
