from django.contrib.auth import authenticate
from rest_framework.utils import json
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    default_error_messages = {
        'no_active_account': 'Email or password is incorrect!',
    }

    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'id': self.user.id})

        print("validate data:", data)

        # try:
        #     request = self.context["request"]
        # except KeyError:
        #     pass
        #
        # self.user = authenticate()
        #
        # if not api_settings.USER_AUTHENTICATION_RULE(self.user):
        #     raise exceptions.AuthenticationFailed(
        #         self.error_messages["no_active_account"],
        #         "no_active_account",
        #     )

        return data
