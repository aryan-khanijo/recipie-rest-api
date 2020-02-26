from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user(self):
        """Test for creating a new user"""
        email = 'test@iron.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
	       """Test the email for a new user is normalized"""
	       email = 'test@LONDONAPPDEV.com'
	       user = get_user_model().objects.create_user(email, 'test123')

	       self.assertEqual(user.email, email.lower())

    def test_new_user_valid_email(self):
        """test user for valid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_new_superuser(self):
        """Create new User Model"""
        user = get_user_model().objects.create_superuser(
            'aryan@iron.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff )
