#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateClass(unittest.TestCase):
    """Tests for State class"""

    def test_class(self):
        state = State()

        """ Verify if state is an instance of State class and BaseModel """
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

        """ Verify if state has attributes """
        self.assertIn("id", state.__dict__)
        self.assertIn("created_at", state.__dict__)
        self.assertIn("updated_at", state.__dict__)
        self.assertIn("name", State.__dict__)

        """ Verify if attributes are of the correct type """
        self.assertEqual(State.name, "")

    def test_attributes_assignment(self):
        state = State()
        """ Verify if attributes are of the correct type  """
        self.assertIsInstance(state.name, str)

        state.name = "Montevideo"
        """ Verify if attributes are of the correct type  """
        self.assertEqual(state.name, "Montevideo")

    def test_to_dict(self):

        state = State()
        state.name = "Montevideo"

        state_dict = state.to_dict()

        """ Verify if state_dict is a dictionary """
        self.assertEqual(state_dict["name"], "Montevideo")
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)

    def test_str_representation(self):

        state = State()
        state.name = "Montevideo"

        """ Verify if str representation is correct """
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)


if __name__ == '__main__':
    unittest.main()
