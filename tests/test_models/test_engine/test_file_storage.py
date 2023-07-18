#!/usr/bin/python3
"""Unittests for FileStorage class"""

import unittest
import os
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageClass(unittest.TestCase):

    def test_all(self):

        self.assertIsInstance(storage, FileStorage)

        obj = BaseModel()
        __objects = storage.all()

        self.assertIsInstance(__objects, dict)

        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, __objects)

        self.assertEqual(obj, __objects[key])
        self.assertIsInstance(__objects[key], BaseModel)

    def set_up(self):
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage.reload()

    def tear_down(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        obj = BaseModel()
        new_dict = {}
        new_dict["id"] = "012345"
        new_dict["created_at"] = "1995-2-2T10:23:35.123450"
        new_dict["updated_at"] = "1999-1-4T7:15:05.543210"
        obj2 = BaseModel(**new_dict)
        key = "{}.{}".format(type(obj2).__name__, obj2.id)
        self.assertNotIn(key, storage.all())
        obj2 = BaseModel()
        key = "{}.{}".format(type(obj2).__name__, obj2.id)
        __objects = storage.all()
        self.assertIn(key, __objects)
        self.assertEqual(obj2, __objects[key])

    def test_save(self):

        file = "file.json"
        if os.path.exists(file):
            os.remove(file)
        storage.save()
        self.assertTrue(os.path.exists(file))
        with open(file, 'w') as f:
            f.write("TestingTheProgram")
        with open(file, 'r') as f:
            content = f.read()
            storage.save()
            new_content = f.read()
        self.assertNotEqual(content, new_content)

    def test_reload(self):

        from json import dumps

        old_dict = storage.all()
        storage.reload()
        new_dict = storage.all()
        self.assertEqual(old_dict.keys(), new_dict.keys())

        obj = BaseModel()
        obj.id = 1
        dict_dict = {"BaseModel.1": obj.to_dict()}
        obje_dict = {"BaseModel.1": obj}
        if os.path.exists("file.json"):
            os.remove("file.json")
        with open("file.json", 'w') as f:
            f.write(dumps(dict_dict))


if __name__ == '__main__':
    unittest.main()
