from django_filters import rest_framework as filters

from .models import UserModel


class UserFilter(filters.FilterSet):
    class Meta:
        model = UserModel
        fields = ['id']
