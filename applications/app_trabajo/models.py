from django.db import models

from applications.app_domicilio.models import Domicilio
from applications.app_personas.models import Persona
from applications.app_PLD.models import Pld

from .managers import EmpresaManager


class Socio(models.Model):

    GENDER_IDENTIFICACION = (
        ("I", "INE"),
        ("C", "Cartilla"),
        ("P", "Pasaporte"),
        ("O", "Otros"),
        ("N", "No Aplica"),
    )

    persona = models.OneToOneField(
        Persona, null=True, blank=True, on_delete=models.CASCADE
    )
    curp = models.CharField(max_length=18, verbose_name="CURP:")
    rfc = models.CharField(max_length=15, verbose_name="RFC:")
    Identificacion = models.CharField(max_length=1, choices=GENDER_IDENTIFICACION)
    NumeroIdentificacion = models.CharField(
        max_length=30, verbose_name="Número de identificación:"
    )
    email = models.EmailField(blank=True, null=True, verbose_name="Email:")
    domicilio = models.ForeignKey(
        Domicilio, null=True, blank=True, on_delete=models.CASCADE
    )
    pld = models.ForeignKey(Pld, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"

    def __str__(self):
        return self.persona.nombre + " " + self.rfc + " " + self.curp + " " + self.email


class Frecuencia(models.Model):
    nombre = models.CharField(max_length=50)
    dias = models.IntegerField()
    meses = models.IntegerField()

    class Meta:
        verbose_name = "Frecuencia"
        verbose_name_plural = "Frecuencias"

    def __str__(self):
        return self.nombre


class Empresa(models.Model):

    nombre = models.CharField(max_length=50)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.PROTECT)
    telefono = models.CharField(max_length=10)
    empleosFijos = models.IntegerField()
    frecuencia = models.ForeignKey(Frecuencia, on_delete=models.PROTECT)

    objects = EmpresaManager()

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre


class Puesto(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Puesto"
        verbose_name_plural = "Puestos"

    def __str__(self):
        return self.nombre


class Trabajo(models.Model):

    persona = models.ForeignKey(
        Persona, null=True, blank=True, on_delete=models.CASCADE
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    puesto = models.ForeignKey(Puesto, on_delete=models.PROTECT)
    fechaTrabajo = models.DateField(
        auto_now_add=True,
        null=True,
    )
    arraigoLaboralAnterior = models.CharField(max_length=100)
    igresoOrdinario = models.DecimalField(max_digits=15, decimal_places=2)
    otrosIngresos = models.DecimalField(max_digits=15, decimal_places=2)
    conceptoIngresos = models.CharField(max_length=50)
    telefono = models.CharField(
        max_length=10, verbose_name="Número de Teléfono del trabajo"
    )

    class Meta:
        verbose_name = "Trabajo"
        verbose_name_plural = "Trabajos"

    def __str__(self):
        return str(self.empresa) + " " + str(self.fechaTrabajo) + " " + str(self.puesto)
