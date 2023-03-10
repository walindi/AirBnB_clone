#!/usr/bin/python3
"""Unittests for models/base_model.py"""

import unittest
import models
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel_instantiation(unittest.TestCase):
    """Test instantiation of the BaseModel class"""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_if_BaseModel_instance_has_id(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "12345"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (12345)", bmstr)
        self.assertIn("'id': '12345'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)


class TestBaseModel_save(unittest.TestCase):
    """Test save method of BaseModel class"""

    def test_that_save_func_updates_update_at_attr(self):
        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)
        self.assertGreater(b.updated_at.microsecond,
                           b.created_at.microsecond)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Test to_dict method"""

    def test_if_to_dict_returns_dict(self):
        b = BaseModel()
        self.assertTrue(type(b.to_dict()) is dict)

    def test_to_dict_contains_added_attributes(self):
        b = BaseModel()
        attrs = ["id", "created_at", "updated_at", "__class__"]
        b.name = "Walindi"
        b.email = "walindi@123.com"
        attrs.extend(["name", "email"])
        for attr in attrs:
            self.assertIn(attr, b.to_dict())

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())


if __name__ == "__main__":
    unittest.main()
