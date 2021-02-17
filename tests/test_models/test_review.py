#!/usr/bin/python3
"""
   TestReview module
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    TestReview class
    """
    def test_create_review_instance(self):
        """
        Test instance creation
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_variables_of_review(self):
        """
        test variables creation
        """
        review = Review()
        self.assertIsInstance(review.name, str)
        self.assertIsInstance(review.user, str)
        self.assertIsInstance(review.text, str)

    def test_id_review(self):
        """
        test unique id for review
        """
        review1_id = Review()
        review2_id = Review()
        self.assertNotEqual(review1_id, review2_id)

if __name__ == '__main__':
    unittest.main()
