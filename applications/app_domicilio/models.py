from django.db import models


class Calle(models.Model):
    GENDER_TIPOS = (
        ("C", "Calle"),
        ("A", "Avenida"),
        ("P", "Prolongación"),
        ("E", "Cerrada"),
        ("R", "Privada"),
        ("L", "Calzada"),
        ("O", "Otro"),
    )
    nombre = models.CharField(max_length=70, verbose_name="Nombre de la calle")
    tipo = models.CharField(max_length=1, choices=GENDER_TIPOS)

    class Meta:
        verbose_name = "Calle"
        verbose_name_plural = "Calles"

    def __str__(self):
        return self.tipo + " " + self.nombre


class Domicilio(models.Model):
    cp = models.CharField(max_length=5, verbose_name="CP:")
    colonia = models.CharField(max_length=50, verbose_name="Barrio/Colonia")
    calle = models.ForeignKey(
        Calle, on_delete=models.PROTECT, verbose_name="Calle", related_name="calle"
    )
    entrecalle = models.ForeignKey(
        Calle,
        on_delete=models.PROTECT,
        verbose_name="Entre la Calle",
        related_name="entrecalle",
    )
    ycalle = models.ForeignKey(
        Calle,
        on_delete=models.PROTECT,
        verbose_name="Y la Calle",
        related_name="ycalle",
    )
    numero = models.CharField(max_length=10, verbose_name="Numero exterior")
    interior = models.CharField(max_length=10, verbose_name="Interior")
    geolocalizacion = models.CharField(max_length=50, verbose_name="Geo localizacion")

    class Meta:
        verbose_name = "Domicilio"
        verbose_name_plural = "Domicilios"

    def __str__(self):
        return str(self.cp) + " " + str(self.colonia)


# Create your models here.
