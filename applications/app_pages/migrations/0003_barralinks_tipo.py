# Generated by Django 4.1.6 on 2023-02-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0002_barralinks_icono'),
    ]

    operations = [
        migrations.AddField(
            model_name='barralinks',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Principal'), (2, 'Catalogo vistas')], default=1),
        ),
    ]