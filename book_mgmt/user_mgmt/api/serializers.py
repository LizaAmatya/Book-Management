from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=255, required=False)
    middle_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all(),
                                                   message="A user with this email already exist.")]
    )
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all(),
                                                   message="A user with this username already exist.")]
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "password",
            "first_name",
            "middle_name",
            'last_name',
        ]
