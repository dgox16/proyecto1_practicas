# Generated by Django 4.1.6 on 2023-02-14 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0007_remove_barralinks_is_active_barralinks_solo_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barralinks',
            name='solo_admin',
            field=models.BooleanField(default=False, verbose_name='Solo podran verlo el administrador'),
        ),
    ]
