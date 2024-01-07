# Generated by Django 5.0 on 2024-01-07 11:41

import django.db.models.deletion
import recipes.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_cover'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.category', verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=recipes.models.recipe_directory_path, verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=165, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='publicado'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_steps',
            field=models.TextField(verbose_name='receita'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_steps_is_html',
            field=models.BooleanField(default=False, verbose_name='receita em html?'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.IntegerField(verbose_name='tempo de preparo'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time_unit',
            field=models.CharField(max_length=65, verbose_name='unidade de medida'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(verbose_name='rendimento'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings_unit',
            field=models.CharField(max_length=65, verbose_name='medida do rendimento'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=65, verbose_name='título'),
        ),
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(choices=[('C', 'Create'), ('R', 'Read'), ('U', 'Update'), ('D', 'Delete')], max_length=1)),
                ('dt_operation', models.DateTimeField(auto_now=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
