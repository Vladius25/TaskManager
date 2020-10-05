from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from tasks.models import Status, Task


class TestTasks(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(TestTasks, cls).setUpClass()
        Status.objects.create(name="Новая")
        Status.objects.create(name="В работе")
        pass

    def setUp(self):
        self.client = APIClient()

    def test_return_200(self):
        response = self.client.get("/api/v1/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        response = self.client.post("/api/v1/tasks/", {"name": "name", "description": "descr", "status": "Новая", "end_date": "2020-10-01T00:00:00"})
        task = Task.objects.get(pk=response.data["id"])