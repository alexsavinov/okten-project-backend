from django.urls import path

from .views import SchoolListCreateView, SchoolRetrieveUpdateDestroyAPIView, AddLogoView, SchoolUpdateAPIView, \
    CityListCreateView

urlpatterns = [
    path('', SchoolListCreateView.as_view(), name='schools_list_create'),
    path('/<int:pk>', SchoolRetrieveUpdateDestroyAPIView.as_view(), name='school_list_create'),
    path('/update', SchoolUpdateAPIView.as_view(), name='school_update'),
    path('/logo', AddLogoView.as_view(), name='school_add_logo'),
    path('/city', CityListCreateView.as_view(), name='cities_list'),

    # path('', SchoolView.as_view(), name='School'),
    # path('/refresh', CustomTokenRefreshView.as_view(), name='refresh_tokens'),
    # path('/activate/<str:token>', ActivateUserView.as_view(), name='auth_activate_user')
]
