from django.db import models

from applications.app_personas.models import Persona

from .managers import PldManager


class Parentesco(models.Model):

    GENDER_TIPO = (
        ("F", "Familiar"),
        ("O", "Otros"),
    )
    GENDER_GRADO = (
        ("1", "1er grado"),
        ("2", "2o. grado"),
        ("3", "3er. grado"),
        ("N", "No aplica"),
    )

    nombre = models.CharField(max_length=50, verbose_name="Nombre del parentesco")
    tipo = models.CharField(max_length=1, choices=GENDER_TIPO)
    grado = models.CharField(max_length=1, choices=GENDER_GRADO)
    tipoId = models.IntegerField()

    class Meta:
        verbose_name = "Parentesco"
        verbose_name_plural = "Parentescos"

    def __str__(self):
        return str(self.nombre)


class PldExpuesta(models.Model):

    funcionPublica = models.CharField(max_length=50, verbose_name="Funcion publica")
    familiarFuncionario = models.ForeignKey(Parentesco, on_delete=models.CASCADE)
    nombreFuncionario = models.CharField(
        max_length=50, verbose_name="Nombre del familiar funcionario"
    )

    class Meta:
        verbose_name = "PLDExpuesta"
        verbose_name_plural = "PLDExpuestas"

    def __str__(self):
        return str(self.nombreFuncionario)


class Pldocupacion(models.Model):

    nombre = models.CharField(max_length=50, verbose_name="Nombre de Ocupación")

    class Meta:
        verbose_name = "PLDOcupaciones"
        verbose_name_plural = "PLDOcupaciónes"

    def __str__(self):
        return str(self.nombre)


class Pldespecificacion(models.Model):

    ocupacionPld = models.ForeignKey(Pldocupacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, verbose_name="Nombre de Especificación")

    class Meta:
        verbose_name = "PLDEspecificación"
        verbose_name_plural = "PLDEspecificaciones"

    def __str__(self):
        return str(self.nombre)


class Pldactividad(models.Model):

    especificacionPld = models.ForeignKey(Pldespecificacion, on_delete=models.CASCADE)
    claveSiti = models.CharField(max_length=8, verbose_name="Clave SITI")
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la actividad PLD")

    class Meta:
        verbose_name = "PLDActividad"
        verbose_name_plural = "PLDActividad"

    def __str__(self):
        return str(self.nombre)


class Pld(models.Model):

    GENDER_EXPUESTA = (
        ("N", "No expuesta"),
        ("H", "Homonimo"),
        ("P", "Persona Politicamente Expuesta"),
        ("F", "Familiar PEPS"),
    )

    persona = models.ForeignKey(
        Persona, null=True, blank=True, on_delete=models.CASCADE
    )
    actividadPld = models.ForeignKey(Pldactividad, null=True, on_delete=models.CASCADE)
    frecuenciaCaptacion = models.IntegerField()
    maximaCaptacion = models.DecimalField(max_digits=15, decimal_places=2)
    frecuenciaPrestamo = models.IntegerField()
    maximoPrestamo = models.DecimalField(max_digits=15, decimal_places=2)
    perfilFrecuenciaCaptacion = models.IntegerField(default=0)
    perfilMaximaCaptacion = models.DecimalField(
        default=0, max_digits=15, decimal_places=2
    )
    perfilFrecuenciaPrestamo = models.IntegerField(
        default=0,
    )
    perfilMaximoPrestamo = models.DecimalField(
        default=0, max_digits=15, decimal_places=2
    )
    tipoExpuesta = models.CharField(max_length=1, choices=GENDER_EXPUESTA)
    personaExpuesta = models.ForeignKey(PldExpuesta, on_delete=models.CASCADE)

    objects = PldManager()

    class Meta:
        verbose_name = "PLD"
        verbose_name_plural = "PLD"

    def __str__(self):
        return str(self.actividadPld)


# Create your models here.
