from django.urls import path

from .views import SchoolListCreateView, SchoolRetrieveUpdateDestroyAPIView, AddLogoView, SchoolUpdateAPIView, \
    CityListCreateView, SchoolCreateView, CommentListCreateView

urlpatterns = [
    path('', SchoolListCreateView.as_view(), name='schools_list_create'),
    path('/add', SchoolCreateView.as_view(), name='school_create'),
    path('/<int:pk>', SchoolRetrieveUpdateDestroyAPIView.as_view(), name='school_list_create'),
    path('/update', SchoolUpdateAPIView.as_view(), name='school_update'),
    path('/logo', AddLogoView.as_view(), name='school_add_logo'),
    path('/city', CityListCreateView.as_view(), name='cities_list'),
    path('/<int:pk>/comments', CommentListCreateView.as_view(), name='comments_list'),
    path('/<int:pk>/comments/add', CommentListCreateView.as_view(), name='comment_create'),
]
