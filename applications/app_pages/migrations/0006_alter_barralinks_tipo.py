# Generated by Django 4.1.6 on 2023-02-12 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0005_alter_barralinks_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barralinks',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Acciones'), (2, 'Catalogo trabajo'), (3, 'Catalogo pld'), (4, 'Catalogo personas'), (5, 'Catalogo formularios'), (6, 'Catalogo domicilo')], default=1),
        ),
    ]