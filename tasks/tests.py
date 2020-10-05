from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.utils import jwt_encode_handler

from tasks.models import Status, Task


def get_client(user):
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="JWT " + token)
    return client


class TestTasks(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(TestTasks, cls).setUpClass()
        new = Status.objects.create(name="Новая")
        work = Status.objects.create(name="В работе")
        cls.task_dict = {
            "name": "name",
            "description": "descr",
            "status": "Новая",
            "end_date": "2020-10-01T00:00:00",
        }
        cls.user = User.objects.create(username="user")
        cls.user1 = User.objects.create(username="user1")
        cls.user2 = User.objects.create(username="user2")
        cls.task1 = Task.objects.create(
            **{**cls.task_dict, "status": new, "owner": cls.user1}
        )
        cls.task2 = Task.objects.create(
            **{**cls.task_dict, "status": work, "owner": cls.user1}
        )
        cls.task3 = Task.objects.create(
            **{**cls.task_dict, "status": work, "owner": cls.user2}
        )
        cls.task4 = Task.objects.create(
            **{**cls.task_dict, "status": new, "owner": cls.user1}
        )

    def setUp(self):
        self.client = get_client(self.user1)

    def test_return_200(self):
        response = self.client.get("/api/v1/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_return_401(self):
        client = APIClient()
        response = client.get("/api/v1/tasks/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_task(self):
        response = self.client.post("/api/v1/tasks/", self.task_dict)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = Task.objects.last()
        self.assertEqual(task.name, self.task_dict["name"])
        self.assertEqual(task.owner, self.user1)

    def test_get_task(self):
        response = self.client.get("/api/v1/tasks/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_another_user(self):
        client = get_client(self.user)
        response = client.get("/api/v1/tasks/1")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_only_user_tasks(self):
        response = self.client.get("/api/v1/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for task in response.data:
            self.assertEqual(task["owner"], self.user1.username)

    def test_filter_tasks(self):
        task_status = "Новая"
        response = self.client.get("/api/v1/tasks/?status=" + task_status)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for task in response.data:
            self.assertEqual(task["status"], task_status)

    def test_update_task_status(self):
        response = self.client.patch(
            "/api/v1/tasks/%s" % self.task4.id, {"status": "В работе"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = Task.objects.get(pk=self.task4.id)
        self.assertEqual(task.status.name, "В работе")

    def test_update_task_status_incorrect(self):
        response = self.client.patch(
            "/api/v1/tasks/%s" % self.task4.id, {"status": "bad"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_task_history(self):
        self.task1.name = "new_task_name"
        self.task1.save()
        response = self.client.get("/api/v1/tasks/history/%s" % self.task1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertNotEqual(response.data[0]["name"], response.data[1]["name"])
