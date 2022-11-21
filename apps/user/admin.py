from django.contrib import admin
# from django.contrib.auth.models import Group

from .models import UserModel


# class GroupInline(admin.StackedInline):
#     model = Group


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'email')
    list_editable = ('is_staff',)
    list_filter = ('is_staff', 'is_active', 'created_at', 'updated_at')
    search_fields = ('email',)
    fields = ('email', 'is_staff', 'is_active', 'groups', 'user_permissions')

    def has_module_permission(self, request):
        return True
    # inlines = (GroupInline,)

