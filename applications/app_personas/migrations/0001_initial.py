# Generated by Django 4.1.6 on 2023-02-04 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Clasificacion:')),
            ],
            options={
                'verbose_name': 'Clasificacion',
                'verbose_name_plural': 'Clasificaciones',
            },
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de registro:')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Sucursal:')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tipo de persona:')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=20, unique=True, verbose_name='Identificador ??nico:')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre:')),
                ('apellidoPaterno', models.CharField(max_length=50, verbose_name='Apellido Paterno:')),
                ('apellidoMaterno', models.CharField(max_length=50, verbose_name='Apellido Materno:')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], max_length=1, verbose_name='Genero:')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='N??mero de Telefono:')),
                ('fechaRegistro', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de registro:')),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_personas.clasificacion', verbose_name='Clasificaci??n:')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_personas.sucursal', verbose_name='Sucursal a la que pertenece:')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_personas.tipo', verbose_name='Tipo de persona:')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario registro:')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
