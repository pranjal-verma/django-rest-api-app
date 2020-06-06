from django.test import TestCase
from django.contrib.auth import get_user_model
class ModelsTest(TestCase):
    
    def test_create_user_success_with_email(self):
        """ Test creating a new user successfully with email """
        email = "test@gmail.com"
        passwrd = "password"

        user = get_user_model().objects.create_user(
            email = email,
            password = passwrd
        )

        self.assertEqual(user.email,email)

        self.assertTrue(user.check_password(passwrd))

    def test_user_email_normalise(self):
        """ Test lower case email"""

        email = 'jcnruad@NEWMAIL.com'

        user = get_user_model().objects.create_user(email,'pwsa23')
        self.assertEqual(user.email, email.lower())

    def test_email_is_presented(self):
        """ Test for validation of email"""
        
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '121321')
    
    def test_create_new_super_user(self):
        """Test to create new super user """
        user = get_user_model().objects.create_superuser(
            'foo@bar.com',
            'canvas'

        ) 
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
