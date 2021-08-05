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
