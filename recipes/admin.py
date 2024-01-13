from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Category, Recipe

# admin.site.site_header = 'Recipe Admin'


class RecipeAdmin(VersionAdmin):
    ...


class CategoryAdmin(VersionAdmin):
    ...


# admin.site.register(Category, CategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
