from django.conf import settings
from django.db import models

from .managers import PersonaManager


class Tipo(models.Model):
    """Tipos de personas que se pueden registrar en la base de datos"""

    name = models.CharField("Tipo de persona:", max_length=50)

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.name


class Clasificacion(models.Model):
    """Clasificacion de las personas registradas"""

    name = models.CharField("Clasificacion:", max_length=50)

    class Meta:
        verbose_name = "Clasificacion"
        verbose_name_plural = "Clasificaciones"

    def __str__(self):
        return self.name


class Sucursal(models.Model):
    """registra las sucursales de la entidad"""

    name = models.CharField("Sucursal:", max_length=50)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.name


class Persona(models.Model):
    """modelo para registrar los datos basicos de una persona"""

    GENDER_CHOICES = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otros"),
    )

    identificador = models.CharField(
        max_length=20, unique=True, verbose_name="Identificador único:"
    )
    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.PROTECT,
        verbose_name="Sucursal a la que pertenece:",
    )
    tipo = models.ForeignKey(
        Tipo, on_delete=models.PROTECT, verbose_name="Tipo de persona:"
    )
    nombre = models.CharField(max_length=50, verbose_name="Nombre:")
    apellidoPaterno = models.CharField(max_length=50, verbose_name="Apellido Paterno:")
    apellidoMaterno = models.CharField(max_length=50, verbose_name="Apellido Materno:")
    clasificacion = models.ForeignKey(
        Clasificacion, on_delete=models.PROTECT, verbose_name="Clasificación:"
    )
    sexo = models.CharField(
        max_length=1, choices=GENDER_CHOICES, verbose_name="Genero:"
    )
    phone = models.CharField(
        max_length=15, blank=True, verbose_name="Número de Telefono:"
    )
    fechaRegistro = models.DateField(
        auto_now_add=True, null=True, verbose_name="Fecha de registro:"
    )
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name="Usuario registro:",
    )

    objects = PersonaManager()

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombre + " " + self.apellidoPaterno + " " + self.apellidoMaterno


class Formulario(models.Model):
    socio = models.ForeignKey("app_trabajo.Socio", on_delete=models.PROTECT, default=1)
    trabajo = models.ForeignKey(
        "app_trabajo.Trabajo", on_delete=models.PROTECT, default=1
    )
    pld = models.ForeignKey("app_PLD.Pld", on_delete=models.PROTECT, default=1)
    persona = models.ForeignKey(
        "app_personas.Persona", on_delete=models.PROTECT, default=1
    )
    fechaRegistro = models.DateField(
        auto_now_add=True, null=True, verbose_name="Fecha de registro:"
    )

    def __str__(self):
        return str(self.fechaRegistro)
