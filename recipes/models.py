from django.db import models
from django.contrib.auth.models import User


def recipe_directory_path(instance, filename):
    return 'recipe/covers/{0}/{1}'.format(instance.id, filename)


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65, verbose_name='título')
    description = models.CharField(max_length=165, verbose_name='descrição')
    slug = models.SlugField()
    preparation_time = models.IntegerField(verbose_name='tempo de preparo')
    preparation_time_unit = models.CharField(max_length=65,
                                             verbose_name='unidade de medida')
    servings = models.IntegerField(verbose_name='rendimento')
    servings_unit = models.CharField(max_length=65,
                                     verbose_name='medida do rendimento')
    preparation_steps = models.TextField(verbose_name='receita')
    preparation_steps_is_html = models.BooleanField(default=False,
                                                    verbose_name='receita em html?')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False,
                                       verbose_name='publicado')
    cover = models.ImageField(upload_to=recipe_directory_path,
                              null=True, blank=True,
                              verbose_name='imagem')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        verbose_name='categoria'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,
        verbose_name='autor'
    )

    def __str__(self):
        return self.title
