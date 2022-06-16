import pytest
from django.test import TestCase


# Create base test .
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
