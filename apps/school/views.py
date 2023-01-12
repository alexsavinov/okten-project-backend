from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.school.filters import SchoolFilter, CityFilter, CommentFilter
from apps.school.models import SchoolModel, CityModel, CommentModel
from apps.school.serializers import SchoolSerializer, AddLogoSerializer, CitySerializer, CommentSerializer
from apps.user.permissons import IsAdmin
from utils.jwt_util import JwtUtils


# class SchoolView(GenericAPIView):
#     """
#     # Activates new user by _activate_ token.
#     Returns empty response with status HTTP_200_OK, parameter __token__ passed by url string.
#     """
#
#     queryset = SchoolModel.objects.all()
#
#     # permission_classes = (AllowAny,)
#     #
#     @staticmethod
#     def get(*args, **kwargs):
#         #     token = kwargs.get('token')
#         #     user = JwtUtils.validate_token(token)
#         #     user.is_active = True
#         #     user.save()
#
#         serializer = SchoolSerializer()
#         return Response(serializer.data, status=status.HTTP_200_OK)


class SchoolListCreateView(ListCreateAPIView):
    # permission_classes = (IsAdmin,)
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()
    filterset_class = SchoolFilter

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return AllowAny(),
    #     return super().get_permissions()


class SchoolRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get school by id
    put:
        Update school by id
    patch:
        Partial update by id
    delete:
        Delete school by id
    """
    # permission_classes = (IsAdmin,)
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer


class SchoolUpdateAPIView(UpdateAPIView):
    serializer_class = SchoolSerializer

    def get_object(self):
        return SchoolModel.objects.get(pk=self.request.data['id'])

    def patch(self, request, *args, **kwargs):
        school = self.get_object()
        school_create_update(school, request)
        serializer = SchoolSerializer(school, partial=True)
        # school.name = request.data.get('name')
        # school.about = request.data.get('about')
        # print([item for item in request.data.get('cities')])
        # # school.cities.set([item.get(0) for item in request.data.get('cities')])
        # # school.ages.set([item.get(0) for item in request.data.get('ages')])
        # school.save()

        return Response(serializer.data, status.HTTP_200_OK)


def school_create_update(school, request):
    school.name = request.data.get('name')
    school.about = request.data.get('about')
    school.cities.set([item.get('id') for item in request.data.get('cities')])
    school.comments.set([item.get('id') for item in request.data.get('comments')])
    # school.ages.set([item.get('id') for item in request.data.get('ages')])
    # school.learn_formats.set([item.get('id') for item in request.data.get('learn_formats')])
    # school.ages.set([item.get(0) for item in request.data.get('ages')])
    school.save()


class AddLogoView(UpdateAPIView):
    serializer_class = AddLogoSerializer

    def get_object(self):
        return SchoolModel.objects.get(pk=self.request.data['id'])


class CityListCreateView(ListCreateAPIView):
    # permission_classes = (IsAdmin,)
    serializer_class = CitySerializer
    queryset = CityModel.objects.all()
    filterset_class = CityFilter


class CommentListCreateView(ListCreateAPIView):
    # permission_classes = (IsAdmin,)
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
    filterset_class = CommentFilter
