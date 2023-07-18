#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """Tests for Place class"""

    def test_class(self):
        obj = Place()

        """ Verify if obj is an instance of Place """
        self.assertIsInstance(obj, Place)

        """ Verify if obj is an instance of BaseModel  """
        self.assertIsInstance(obj, BaseModel)

        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("city_id", Place.__dict__)
        self.assertIn("user_id", Place.__dict__)
        self.assertIn("name", Place.__dict__)
        self.assertIn("description", Place.__dict__)
        self.assertIn("number_rooms", Place.__dict__)
        self.assertIn("number_bathrooms", Place.__dict__)
        self.assertIn("max_guest", Place.__dict__)
        self.assertIn("price_by_night", Place.__dict__)
        self.assertIn("latitude", Place.__dict__)
        self.assertIn("longitude", Place.__dict__)
        self.assertIn("amenity_ids", Place.__dict__)

        """ Verify if attributes are public """
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])

    def test_attributes_assignment(self):
        place = Place()
        place.city_id = "12345"
        place.user_id = "67890"
        place.name = "Somewhere"
        place.description = "A charming place to stay"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = [1, 2, 3]

        """ Verify if attributes are assigned correctly """
        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "67890")
        self.assertEqual(place.name, "Somewhere")
        self.assertEqual(place.description, "A charming place to stay")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, [1, 2, 3])

    def test_to_dict(self):

        place = Place()
        place.city_id = "12345"
        place.user_id = "67890"
        place.name = "Somewhere"
        place.description = "A charming place to stay"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = [1, 2, 3]

        place_dict = place.to_dict()

        """ Verify if to_dict() returns a dictionary """
        self.assertEqual(place_dict["city_id"], "12345")
        self.assertEqual(place_dict["user_id"], "67890")
        self.assertEqual(place_dict["name"], "Somewhere")
        self.assertEqual(place_dict["description"], "A charming place to stay")
        self.assertEqual(place_dict["number_rooms"], 2)
        self.assertEqual(place_dict["number_bathrooms"], 1)
        self.assertEqual(place_dict["max_guest"], 4)
        self.assertEqual(place_dict["price_by_night"], 100)
        self.assertEqual(place_dict["latitude"], 37.7749)
        self.assertEqual(place_dict["longitude"], -122.4194)
        self.assertEqual(place_dict["amenity_ids"], [1, 2, 3])
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)


if __name__ == '__main__':
    unittest.main()
