"""
Tests for the Signups models.
"""
from django.test import TestCase
from .. import models


class TestSignupModel(TestCase):
    """
    Test cases for the Signup model.
    """
    def test_can_create_with_email(self):
        """
        Create a new signup, save it, and ensure it now has an id and
        creation timestamp.
        """
        signup = models.Signup(email='test@test.com')
        signup.save()
        self.assertIsNotNone(signup.id)
        self.assertIsNotNone(signup.created_at)

    def test_can_retrieve_signup_by_up(self):
        """
        Create a new signup, save it, and ensure we can get the signup
        from the database with the new ID.
        """
        signup = models.Signup(email='test@test.com')
        signup.save()
        signup_id = signup.id

        retrieved_signup = models.Signup.objects.filter(pk=signup_id).first()
        self.assertEqual(signup.email, retrieved_signup.email)
