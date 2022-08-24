from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     ListCreateAPIView, RetrieveAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView, )
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from user_mgmt.api.serializers import UserRegisterSerializer
from rest_framework.response import Response
User = get_user_model()



class RegisterUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        password = make_password(serializer.validated_data.get('password'))
        username = serializer.validated_data.get('username')
        first_name = serializer.validated_data.get('first_name')
        middle_name = serializer.validated_data.get('middle_name')
        last_name = serializer.validated_data.get('last_name')
        phone_number = serializer.validated_data.get('phone_number')
        email = serializer.validated_data.get('email')
        user = serializer.save(
            password=password, username=username, phone_number=phone_number, email=email,
            first_name=first_name, last_name=last_name, middle_name=middle_name)
       
        return user

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.perform_create(serializer)

        custom_response = model_to_dict(
            user,
            fields=[
                "id",
                "username",
                "email",
                "first_name",
                "last_name",
                "mobile_number",
            ],
        )
        

        return Response(custom_response, status=status.HTTP_201_CREATED)
