from django.contrib import admin
from .models import Category

admin.site.site_header = 'Recipe Admin'


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
