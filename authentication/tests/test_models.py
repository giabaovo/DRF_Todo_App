from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_create_user(self):
        user = User.objects.create_user('bao', 'bao@gmail.com', 'bao123456')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'bao@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="",
                          email='bao@gmail.com', password='bao123456')

    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(
                username='', email='bao@gmail.com', password='bao123456')

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="bao",
                          email='', password='bao123456')

    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(
                username='bao', email='', password='bao123456')

    def test_create_super_user(self):
        user = User.objects.create_superuser(
            'bao', 'bao@gmail.com', 'bao123456')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'bao@gmail.com')

    def test_cant_create_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True'):
            User.objects.create_superuser(
                username='bao', email='bao@gmail.com', password='bao123456', is_staff=False)

    def test_cant_create_super_user_with_no_is_superuser_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True'):
            User.objects.create_superuser(
                username='bao', email='bao@gmail.com', password='bao123456', is_superuser=False)
