# Generated by Django 4.1.6 on 2023-02-08 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barralinks',
            name='icono',
            field=models.CharField(default='face', max_length=50, verbose_name='Icono:'),
        ),
    ]