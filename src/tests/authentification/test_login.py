import pytest
from django.urls import reverse
from .base_test import BaseTest
from django.contrib.auth.models import User


# Create class test for login.
class LoginTest(BaseTest):
    # test login success with test database.
    @pytest.mark.django_db
    def test_login_success(self):
        User.objects.create_user(username=self.user['username'], password=self.user['password1'])
        response = self.client.post(reverse('login'), {'username': 'test', 'password': 'Passer@123'})
        self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, reverse('index'))

    # test login with invalid password.
    @pytest.mark.django_db
    def test_login_invalid_password(self):
        User.objects.create_user(username=self.user['username'], password=self.user['password2'])
        response = self.client.post(reverse('login'), self.user_unmatching_password)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/account/login.html')

    # test login with no username.
    @pytest.mark.django_db
    def test_login_no_username(self):
        User.objects.create_user(username=self.user['username'], password=self.user['password1'])
        response = self.client.post(reverse('login'), {'username': '', 'password': 'Passer@123'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/account/login.html')

    # test login with invalid password.
    @pytest.mark.django_db
    def test_login_invalid_username(self):
        User.objects.create_user(username=self.user['username'], password=self.user['password1'])
        response = self.client.post(reverse('login'), {'username': 'invalid', 'password': 'Passer@123'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/account/login.html')
