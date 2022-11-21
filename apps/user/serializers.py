from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import HttpResponse

from rest_framework.serializers import ModelSerializer

from exceptions.sendemail_exception import SendEmailException
from utils.email_util import EmailUtils
from utils.jwt_util import JwtUtils

from apps.profile.models import ProfileModel
from apps.profile.serializers import ProfileSerializer

from .models import UserModel as User

UserModel: User = get_user_model()


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'profile', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at'
        )
        read_only_fields = (
            'id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at'
        )
        # write_only_fields = ('password',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        token = JwtUtils.create_token(user)

        try:
            EmailUtils.register_email(user.email, user.profile.name, token)
        except Exception as e:
            raise SendEmailException(e)

        return user
