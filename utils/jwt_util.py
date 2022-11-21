from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.tokens import AccessToken, BlacklistMixin

from exceptions.jwt_exception import JwtException
from enums.action_enum import ActionTokenEnum

UserModel = get_user_model()


class ActionToken(BlacklistMixin, AccessToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.exp_time


class JwtUtils:
    @staticmethod
    def create_token(user):
        return ActionToken.for_user(user)

    @staticmethod
    def validate_token(token):
        try:
            action_token = ActionToken(token)
            action_token.check_blacklist()
        except Exception:
            raise JwtException
        action_token.blacklist()
        user_id = action_token.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
