from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler

from registration.serializers import UserSerializer


class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        user = User.objects.get(username=response.data["username"])
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response.data["token"] = token
        return response
