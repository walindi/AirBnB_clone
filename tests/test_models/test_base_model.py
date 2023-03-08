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

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

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


class TestBaseModel_to_dict(unittest.TestCase):
    """Test to_dict method"""


if __name__ == "__main__":
    unittest.main()
