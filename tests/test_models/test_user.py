#!/usr/bin/python3
"""
TestUser module
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
       TestUser class
    """

    def test_create_user_instance(self):
        """
        test instance creation
        """
        user = User()
        self.assertIsInstance(user, User)

    def test_variables_of_user(self):
        """
        test variable creation
        """
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_id_user(self):
        """
        test unique id
        """
        user1_id = User()
        user2_id = User()
        self.assertNotEqual(user1_id, user2_id)

if __name__ == '__main__':
    unittest.main()
