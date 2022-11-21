from django.urls import path

from .views import (
    ActivateUserView,
    AddAvatarView,
    AdminToUserView,
    DeactivateUserView,
    DeleteUserView,
    # ListExceptUserView,
    UserUpdateAPIView,
    UserToAdminView,
    UserListCreateView)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>', UserListCreateView.as_view(), name='user_list_create'),
    # # -реализовать добавление прав администратора юзеру и понижение до обычного юзера (is_staff)
    path('/<int:pk>/admin', UserToAdminView.as_view(), name='user_set_to_admin'),
    path('/<int:pk>/not_admin', AdminToUserView.as_view(), name='admin_set_to_user'),
    # # -реализовать активацию деактивацию юзера по id (is_active)
    path('/<int:pk>/activate', ActivateUserView.as_view(), name='activate_user'),
    path('/<int:pk>/deactivate', DeactivateUserView.as_view(), name='deactivate_user'),
    # # -реализовать удаление юзеров
    path('/<int:pk>/delete', DeleteUserView.as_view(), name='delete_user'),
    # # -реализовать вывод всех юзеров кроме себя самого(исключаем залогиненого юзера)
    # path('/except', ListExceptUserView.as_view(), name='list_except_user'),
    path('/update', UserUpdateAPIView.as_view(), name='user_update'),
    # # Реализовать добавление аватарки
    path('/avatar', AddAvatarView.as_view(), name='user_add_avatar')
]