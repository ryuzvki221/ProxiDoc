import pytest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
class BaseTest(TestCase):
    register_url=reverse('register')
    login_url=reverse('login')
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
            'username': 'test',
            'email': 'testemail@proxidoc.com',
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



class LoginTest(BaseTest):
    
    def test_login_success(self):
        self.client.post(self.register_url,self.user)
        user=User.objects.filter(username=self.user['username']).first()
        user.is_active=True
        user.save()
        response=self.client.post(self.login_url, self.user)
        self.assertEqual(response.status_code,200)

    # def test_login_without_username(self):
    #     response = self.client.post(self.login_url, {'password':'password', 'username':''})
    #     self.assertEqual(response.status_code,401)
    
    # def test_login_without_password(self):
    #     response = self.client.post(self.login_url, {'username':'username', 'password':''})
    #     self.assertEqual(response.status_code,401)