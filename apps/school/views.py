from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, \
    CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.school.filters import SchoolFilter, CityFilter, CommentFilter
from apps.school.models import SchoolModel, CityModel, CommentModel
from apps.school.serializers import SchoolSerializer, AddLogoSerializer, CitySerializer, CommentSerializer
from apps.user.permissons import IsAdmin
from utils.jwt_util import JwtUtils


class SchoolListCreateView(ListCreateAPIView):
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()
    filterset_class = SchoolFilter

    # def post(self, request, *args, **kwargs):
    #     print('-------', self)
    #     print('-------', self.get_object())
    #     school = self.get_object()
    #     school_create_update(school, request)
    #     serializer = SchoolSerializer(school, partial=True)
    #     # school.name = request.data.get('name')
    #     # school.about = request.data.get('about')
    #     # print([item for item in request.data.get('cities')])
    #     # # school.cities.set([item.get(0) for item in request.data.get('cities')])
    #     # # school.ages.set([item.get(0) for item in request.data.get('ages')])
    #     # school.save()
    #
    #     return Response(serializer.data, status.HTTP_200_OK)


class SchoolCreateView(CreateAPIView):
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()
    filterset_class = SchoolFilter

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.cities.set([item.get('id') for item in self.request.data.get('cities')])
        return Response(obj, status.HTTP_201_CREATED)


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
        return Response(serializer.data, status.HTTP_200_OK)


def school_create_update(school, request):
    school.name = request.data.get('name')
    school.about = request.data.get('about')
    school.homework = request.data.get('homework')
    school.certificate = request.data.get('certificate')
    school.internship = request.data.get('internship')
    school.site = request.data.get('site')
    school.facebook = request.data.get('facebook')
    school.instagram = request.data.get('instagram')
    school.telegram = request.data.get('telegram')
    school.tiktok = request.data.get('tiktok')
    school.youtube = request.data.get('youtube')
    school.cities.set([item.get('id') for item in request.data.get('cities')])
    # school.comments.set([item.get('id') for item in request.data.get('comments')])
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
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
    filterset_class = CommentFilter

    def perform_create(self, serializer):
        obj = serializer.save(school_id=self.kwargs.get('pk'))
        return Response(obj, status.HTTP_201_CREATED)
