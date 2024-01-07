from django.contrib import admin
from .models import Category, Recipe

# admin.site.site_header = 'Recipe Admin'


@admin.register(Recipe)  # outra forma de registrar no admin
class RecipeAdmin(admin.ModelAdmin):
    ...


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
