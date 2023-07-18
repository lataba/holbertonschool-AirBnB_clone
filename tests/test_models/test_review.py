#!/usr/bin/python3

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReviewClass(unittest.TestCase):
    """Tests for Review class"""

    def test_class(self):
        review = Review()

        """ Verify if review is an instance of Review and BaseModel """
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

        """ Verify if attributes are public and correct type """
        self.assertIn("id", review.__dict__)
        self.assertIn("created_at", review.__dict__)
        self.assertIn("updated_at", review.__dict__)
        self.assertIn("place_id", Review.__dict__)
        self.assertIn("user_id", Review.__dict__)
        self.assertIn("text", Review.__dict__)

        """ Verify if attributes are public and correct type """
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

    def test_attributes_assignment(self):
        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "Great experience!"

        """ Verify if attributes are public and correct type """
        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "67890")
        self.assertEqual(review.text, "Great experience!")

    def test_to_dict(self):

        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "Great experience!"

        review_dict = review.to_dict()

        """ Verify if to_dict() returns a dictionary """
        self.assertEqual(review_dict["place_id"], "12345")
        self.assertEqual(review_dict["user_id"], "67890")
        self.assertEqual(review_dict["text"], "Great experience!")
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)


if __name__ == '__main__':
    unittest.main()
