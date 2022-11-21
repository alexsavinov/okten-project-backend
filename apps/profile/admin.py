from django.contrib import admin

# from apps.user.models import UserModel
# from .models import UserModel
from apps.profile.models import ProfileModel


# admin.site.register(UserModel)
# admin.site.register(ProfileModel)

@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'born', 'avatar', 'phone', 'user')
    list_display_links = ('id', 'name', 'user')
    search_fields = ('name', 'surname', 'phone')
