from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from django.contrib import admin

admin.autodiscover()

schema_view = get_schema_view(
    openapi.Info(
        title="MapIT API",
        default_version='v1',
        description="Map IT",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@mapit.itermit.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('/admin', admin.site.urls),
    path('/users', include('apps.user.urls')),
    path('/auth', include('apps.auth.urls')),
    path('/schools', include('apps.school.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
