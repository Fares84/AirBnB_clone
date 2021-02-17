#!/usr/bin/python3
"""
   TestState module
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    TestState class
    """
    def test_create_state_instance(self):
        """
        Test instance creation
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_variables_of_state(self):
        """
        test variables creation
        """
        state = State()
        self.assertIsInstance(state.name, str)

    def test_id_state(self):
        """
        test unique id for state
        """
        state1_id = State()
        state2_id = State()
        self.assertNotEqual(state1_id, state2_id)

if __name__ == '__main__':
    unittest.main()
