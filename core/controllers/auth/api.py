import logging

from django.contrib.auth.decorators import login_required
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

from core.controllers.auth.serializer import UserSerializer
from core.services.auth import AuthService

log = logging.getLogger(__name__)


class AuthAPIView:
    @staticmethod
    @api_view(['POST'])
    def sign_up(request):
        data = request.data
        log.info(f"creating user with data: {data}")
        name = data['name']
        email = data['email']
        password = data['password']
        is_staff = data['is_staff']

        user = AuthService.sign_up(name=name, email=email, password=password, is_staff=is_staff)
        log.info(f"user created : {user.id}")
        return Response(UserSerializer(user).data, status=HTTP_201_CREATED)

    @staticmethod
    @authentication_classes([BasicAuthentication])
    @api_view(['GET'])
    def login(request):
        return Response({"ok": "success", "user": UserSerializer(request.user).data}, status=HTTP_200_OK)
