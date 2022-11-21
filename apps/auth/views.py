from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt import serializers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from utils.jwt_util import JwtUtils

from apps.auth.models import CustomTokenObtainPairSerializer


class ActivateUserView(GenericAPIView):
    """
    # Activates new user by _activate_ token.
    Returns empty response with status HTTP_200_OK, parameter __token__ passed by url string.
    """

    # AssertionError: 'ActivateUserView' should either include a `serializer_class` attribute,
    # or override the `get_serializer_class()` method.
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

    @staticmethod
    def get(*args, **kwargs):
        token = kwargs.get('token')
        user = JwtUtils.validate_token(token)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    # Handle login process
    Returns a pair of tokens (_access_ and _refresh_) by given in request body User-data (_email_ and _password_).
    """

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # print("request", request.data)
        # print("request *args", *args)
        # print("request **kwargs", **kwargs)
        # return super().post(request, *args, **kwargs)

        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise serializers.ValidationError({
                'detail': e,
                'custom': True
            })

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class CustomTokenRefreshView(TokenRefreshView):
    """
    # Handles refresh tokens
    Returns a pair of tokens (_access_ and _refresh_) by given in request body _refresh_ token.
    """

    # serializer_class = CustomTokenObtainPairSerializer
