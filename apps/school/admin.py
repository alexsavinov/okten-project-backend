from django.contrib import admin

from .models import SchoolModel, CityModel, CommentModel


@admin.register(CityModel)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


# class CityInline(admin.TabularInline):
#     model = SchoolModel.cities.through


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'approved_at', 'created_at')
    list_display_links = ('id', 'author')
    list_filter = ('author',)
    search_fields = ('author',)


class CommentInline(admin.TabularInline):
    model = CommentModel


# class AgeInline(admin.TabularInline):
#     model = AgeModel.ages.through
#
#
# class LearnFormatInline(admin.TabularInline):
#     model = LearnFormatModel.learn_formats.through


@admin.register(SchoolModel)
class SchoolAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'about', 'city', 'created_at', 'updated_at')
    list_display = ('id', 'name',
                    # 'about',
                    'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    # list_editable = ('is_staff',)
    list_filter = ('name',)
    search_fields = ('name',)
    # inlines = [
    #     CityInline,
    #     CommentInline,
    #     # AgeInline,
    #     # LearnFormatInline,
    # ]

# @admin.register(AgeModel)
# class AgeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     list_filter = ('name',)
#     search_fields = ('name',)


# @admin.register(LearnFormatModel)
# class LearnFormatAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     list_filter = ('name',)
#     search_fields = ('name',)
