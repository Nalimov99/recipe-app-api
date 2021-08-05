from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''
        email = 'email@email.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_new_user_email_normalize(self):
        '''Test lowercasing the domain portion of the email address'''
        email = 'email@EMAIL.CoM'
        user = get_user_model().objects.create_user(
            email=email,
            password='Test123'
        )
        self.assertEqual(email.lower(), user.email)

    def test_new_user_valid_email(self):
        '''Test creating a user with no email'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')

    def test_create_superuser(self):
        '''Test creating super user'''
        user = get_user_model().objects.create_superuser(
            'email@email.com',
            'Test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
