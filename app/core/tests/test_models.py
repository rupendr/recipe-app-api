from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'rupendra@gmail.com'
        password = 'Test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_email_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test124')

    def test_create_superUser(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com', 'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
