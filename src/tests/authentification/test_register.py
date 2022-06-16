from django.urls import reverse
from .base_test import BaseTest


# Create class test for register.
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

    