from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class RegistrationTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register(self):
        response = self.client.post(
            "/register/", {"username": "test", "password": "123"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], "test")
        self.assertIn("token", response.data)

    def test_login(self):
        user = User.objects.create(username="user")
        user.set_password("123")
        user.save()
        response = self.client.post("/login/", {"username": "user", "password": "123"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
