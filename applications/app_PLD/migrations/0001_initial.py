# Generated by Django 4.1.6 on 2023-02-04 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del parentesco')),
                ('tipo', models.CharField(choices=[('F', 'Familiar'), ('O', 'Otros')], max_length=1)),
                ('grado', models.CharField(choices=[('1', '1er grado'), ('2', '2o. grado'), ('3', '3er. grado'), ('N', 'No aplica')], max_length=1)),
                ('tipoId', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Parentesco',
                'verbose_name_plural': 'Parentescos',
            },
        ),
        migrations.CreateModel(
            name='Pldocupacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de Ocupación')),
            ],
            options={
                'verbose_name': 'PLDOcupaciones',
                'verbose_name_plural': 'PLDOcupaciónes',
            },
        ),
        migrations.CreateModel(
            name='PldExpuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcionPublica', models.CharField(max_length=50, verbose_name='Funcion publica')),
                ('nombreFuncionario', models.CharField(max_length=50, verbose_name='Nombre del familiar funcionario')),
                ('familiarFuncionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_PLD.parentesco')),
            ],
            options={
                'verbose_name': 'PLDExpuesta',
                'verbose_name_plural': 'PLDExpuestas',
            },
        ),
        migrations.CreateModel(
            name='Pldespecificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de Especificación')),
                ('ocupacionPld', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_PLD.pldocupacion')),
            ],
            options={
                'verbose_name': 'PLDEspecificación',
                'verbose_name_plural': 'PLDEspecificaciones',
            },
        ),
        migrations.CreateModel(
            name='Pldactividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claveSiti', models.CharField(max_length=8, verbose_name='Clave SITI')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de la actividad PLD')),
                ('especificacionPld', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_PLD.pldespecificacion')),
            ],
            options={
                'verbose_name': 'PLDActividad',
                'verbose_name_plural': 'PLDActividad',
            },
        ),
        migrations.CreateModel(
            name='Pld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuenciaCaptacion', models.IntegerField()),
                ('maximaCaptacion', models.DecimalField(decimal_places=2, max_digits=15)),
                ('frecuenciaPrestamo', models.IntegerField()),
                ('maximoPrestamo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('perfilFrecuenciaCaptacion', models.IntegerField(default=0)),
                ('perfilMaximaCaptacion', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('perfilFrecuenciaPrestamo', models.IntegerField(default=0)),
                ('perfilMaximoPrestamo', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('tipoExpuesta', models.CharField(choices=[('N', 'No expuesta'), ('H', 'Homonimo'), ('P', 'Persona Politicamente Expuesta'), ('F', 'Familiar PEPS')], max_length=1)),
                ('actividadPld', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_PLD.pldactividad')),
            ],
            options={
                'verbose_name': 'PLD',
                'verbose_name_plural': 'PLD',
            },
        ),
    ]
