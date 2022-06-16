from django.test import TestCase

# Create base test .
from django.urls import reverse


class BaseTest(TestCase):
    def setUp(self):
        self.user = {
            'username': 'test',
            'email': 'testemail@proxidoc.com',
            'password1': 'Passer@123',
            'password2': 'Passer@123'
        }

        self.user_short_password = {
            'username': 'test',
            'email': 'testemail@proxidoc.com',
            'password1': 'tes',
            'password2': 'tes'
        }
        self.user_unmatching_password = {

            'email': 'testemail@proxidoc.com',
            'username': 'test',
            'password1': 'Passer@123',
            'password2': 'Passer@1234'
        }

        self.user_invalid_email = {
            'username': 'test',
            'email': 'test.com',
            'password1': 'Passer@123',
            'password2': 'Passer@123',
            'name': 'fullname'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


# Create test for register.
class RegisterTest(BaseTest):
    # test can register with valid data.
    def test_register_valid(self):
        response = self.client.post(reverse('register'), self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].is_valid(), True)
        self.assertTemplateUsed(response, 'auth/account/register.html')

    # test can't register with short password.
    def test_register_short_password(self):
        response = self.client.post(reverse('register'), self.user_short_password)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].is_valid(), False)
        self.assertTemplateUsed(response, 'auth/account/register.html')

    # test can't register with unmatching password.
    def test_register_unmatching_password(self):
        response = self.client.post(reverse('register'), self.user_unmatching_password)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].is_valid(), False)
        self.assertTemplateUsed(response, 'auth/account/register.html')

    # test can't register with invalid email.
    def test_register_invalid_email(self):
        response = self.client.post(reverse('register'), self.user_invalid_email)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].is_valid(), False)
        self.assertTemplateUsed(response, 'auth/account/register.html')
