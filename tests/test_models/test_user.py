#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUserClass(unittest.TestCase):
    """ Tests User class """

    def test_class(self):

        obj = User()

        """ Verify if obj is an instance of User and BaseModel """
        self.assertIsInstance(obj, User)
        self.assertIsInstance(obj, BaseModel)

        """ Verify if obj has attributes """
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("email", User.__dict__)
        self.assertIn("password", User.__dict__)
        self.assertIn("first_name", User.__dict__)
        self.assertIn("last_name", User.__dict__)

        """ Verify if obj has attributes """
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")

    def test_attributes_assignment(self):

        user = User()
        user.email = "laura@ex.com"
        user.password = "123456"
        user.first_name = "Laura"
        user.last_name = "Balleste"

        """ Verify if obj has attributes """
        self.assertEqual(user.email, "laura@ex.com")
        self.assertEqual(user.password, "123456")
        self.assertEqual(user.first_name, "Laura")
        self.assertEqual(user.last_name, "Balleste")

    def test_to_dict(self):

        user = User()
        user.email = "ismael@ex.com"
        user.password = "123456"
        user.first_name = "Ismael"
        user.last_name = "Molina"

        user_dict = user.to_dict()

        """ Verify if obj has attributes and their values """
        self.assertEqual(user_dict["email"], "ismael@ex.com")
        self.assertEqual(user_dict["password"], "123456")
        self.assertEqual(user_dict["first_name"], "Ismael")
        self.assertEqual(user_dict["last_name"], "Molina")
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)


if __name__ == '__main__':
    unittest.main()
