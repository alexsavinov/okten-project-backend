from django_filters import rest_framework as filters

from .models import SchoolModel, CityModel, CommentModel


class SchoolFilter(filters.FilterSet):
    class Meta:
        model = SchoolModel
        fields = ['id']


class CityFilter(filters.FilterSet):
    class Meta:
        model = CityModel
        fields = ['id']


class CommentFilter(filters.FilterSet):
    class Meta:
        model = CommentModel
        fields = ['id']
