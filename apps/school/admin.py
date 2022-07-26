from django.contrib import admin

from .models import SchoolModel, CityModel, AgeModel


@admin.register(CityModel)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(AgeModel)
class AgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


class CityInline(admin.TabularInline):
    model = SchoolModel.cities.through


class AgeInline(admin.TabularInline):
    model = AgeModel.ages.through


@admin.register(SchoolModel)
class SchoolAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'about', 'city', 'created_at', 'updated_at')
    list_display = ('id', 'name', 'about', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    # list_editable = ('is_staff',)
    list_filter = ('name',)
    search_fields = ('name',)
    inlines = [
        CityInline,
        AgeInline
    ]
