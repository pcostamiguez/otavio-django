# Generated by Django 5.0 on 2024-01-07 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_historicalcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalrecipe',
            name='author',
        ),
        migrations.RemoveField(
            model_name='historicalrecipe',
            name='category',
        ),
        migrations.RemoveField(
            model_name='historicalrecipe',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalCategory',
        ),
        migrations.DeleteModel(
            name='HistoricalRecipe',
        ),
    ]
