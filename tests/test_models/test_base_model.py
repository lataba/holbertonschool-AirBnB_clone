#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ We create a class to test the BaseModel class
    that inherits from the unittest.TestCase class """

    def test_id_and_intances(self):
        model1 = BaseModel()
        model2 = BaseModel()

        """ Verify that the model1 and model2 are instances of BaseModel """
        self.assertIsInstance(model1, BaseModel)
        self.assertIsInstance(model2, BaseModel)

        """ Verify that the id is not None """
        self.assertIsNotNone(model1.id)
        self.assertIsNotNone(model2.id)

        """ Verify that the id is not None and is a stringes if id """
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model2.id, str)

        """ Verify that the id is not the same  """
        self.assertNotEqual(model1.id, model2.id)

    def test_dict_creation(self):
        obj = BaseModel()

        """ Verify that the obj is a dictionary """
        self.assertIn("id", obj.__dict__)

        """ Verify that the created_at and updated_at are in the dictionary """
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)

    def test_created_at(self):
        model = BaseModel()

        """ Verify that the created_at is not None """
        self.assertIsNotNone(model.created_at)

        """ Verify that the created_at is a datetime """
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        model = BaseModel()

        """ Verify that the updated_at is not None """
        self.assertIsNotNone(model.updated_at)

        """ Verify that the updated_at is a datetime instance """
        self.assertIsInstance(model.updated_at, datetime)

        """ Verify that the created_at is the same as updated_at  """
        self.assertEqual(model.updated_at, model.created_at)

    def test_str(self):
        obj = BaseModel()
        cls = type(obj).__name__

        """ Verify that the str method returns a string """
        string = "[{}] ({}) {}".format(cls, obj.id, obj.__dict__)

        """ Verify that the string is the same as the __str__ method  """
        self.assertEqual(obj.__str__(), string)

    def test_save_updated_at(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()

        """ Verify that the updated_at is not the same as the created_at """
        self.assertNotEqual(old_updated_at, model.updated_at)

        """ Verify that the updated_at is a datetime instance """
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict_contains_attributes(self):
        model = BaseModel()
        model.name = "Test Model"
        model.number = 123
        model_dict = model.to_dict()

        """ Verify that the model_dict is a dictionary """
        self.assertIsInstance(model_dict, dict)

        """ Verify that the model_dict contains the attributes of the model """
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("number", model_dict)

    def test_to_dict_class_name(self):
        model = BaseModel()
        model_dict = model.to_dict()

        """ Verify that the model_dict contains the class name """
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_to_dict_datetime_format(self):
        model = BaseModel()
        model_dict = model.to_dict()

        """ Verify that the datetime is in the correct format """
        created_at_str = datetime.strptime(
            model_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
        )
        updated_at_str = datetime.strptime(
            model_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
        )

        """ Verify that the datetime is a datetime instance """
        self.assertIsInstance(created_at_str, datetime)
        self.assertIsInstance(updated_at_str, datetime)


if __name__ == "__main__":
    unittest.main()
