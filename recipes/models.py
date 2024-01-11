from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


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

    def save(self, *args, **kwargs):
        old_image_path = self.cover.path if self.pk else None

        super().save(*args, **kwargs)

        # Redimensiona a imagem após o upload
        if self.cover:
            # Abre a imagem original
            img = Image.open(self.cover.path)

            # Dimensões desejadas para o crop
            target_width = 800
            target_height = 600

            # Redimensiona a imagem para garantir que ela se encaixe nas dimensões desejadas
            img_resized = img.resize((target_width, target_height), Image.LANCZOS)

            # Obtém as dimensões da imagem redimensionada
            img_width, img_height = img_resized.size

            # Calcula as coordenadas para cortar a imagem centralizada
            left = max(0, (img_width - target_width) // 2)
            top = max(0, (img_height - target_height) // 2)
            right = min(img_width, left + target_width)
            bottom = min(img_height, top + target_height)

            # Corta a imagem redimensionada
            img_cropped = img_resized.crop((left, top, right, bottom))

            # Salva a imagem cortada
            img_cropped.save(self.cover.path)

        if old_image_path and os.path.exists(old_image_path):
            os.remove(old_image_path)
