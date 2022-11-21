from datetime import datetime

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.profile.serializers import AddAvatarSerializer, ProfileSerializer

from apps.user.filters import UserFilter
from apps.user.permissons import IsSuperUser, IsAdmin
from apps.user.serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    filterset_class = UserFilter

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        return super().get_permissions()

    def get_queryset(self):
        if self.kwargs.get('pk'):
            queryset = UserModel.objects.filter(pk=self.kwargs.get('pk'))
            return queryset


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile

    def patch(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = ProfileSerializer(profile)

        profileRequest = request.data.get('profile')

        profile.name = profileRequest['name']
        profile.surname = profileRequest['surname']
        profile.born = datetime.strptime(profileRequest['born'], '%Y-%m-%d').date()
        profile.phone = profileRequest['phone']
        # profile.name = request.data['name']
        # profile.surname = request.data['surname']
        # profile.born = datetime.strptime(request.data['born'], '%Y-%m-%d').date()
        # profile.phone = request.data['phone']
        profile.save()

        # profile.__dict__.update(request.data.__dict__)
        # profile.name = request.data.profile.name
        # print(profile.name)
        # profile.name = request.data['name']
        # print(request.data)
        # print(request.data.get('profile')['name'])
        # print(datetime.strptime(request.data['born'], '%Y-%m-%d'))

        return Response(serializer.data, status.HTTP_200_OK)


class UserToAdminView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            raise ValueError('User is already admin')
        user.is_staff = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            raise ValueError('User is already not admin')
        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class ActivateUserView(APIView):
    permission_classes = (IsAdmin,)
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            raise ValueError('User is already active')
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class DeactivateUserView(GenericAPIView):
    permission_classes = (IsAdmin,)
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            raise ValueError('User is already not active')
        user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class DeleteUserView(DestroyAPIView):
    permission_classes = (IsAdmin,)
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if user.is_superuser:
            raise ValueError('Cannot delete superuser')
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer_class = UserSerializer


class ListExceptUserView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = UserModel.objects.all()
        qs = qs.exclude(id=self.request.user.id)
        return qs


class AddAvatarView(UpdateAPIView):
    serializer_class = AddAvatarSerializer

    def get_object(self):
        return self.request.user.profile

