from django.db import models


class BarraLinks(models.Model):
    TIPO = (
        (1, "Principal"),
        (2, "Catalogo vistas"),
    )

    titulo = models.CharField("Titulo:", max_length=50)
    url = models.CharField("URL:", max_length=50)
    orden = models.CharField("Orden:", max_length=50)
    icono = models.CharField("Icono:", max_length=50, default="face")
    is_active = models.BooleanField("Esta activo")
    tipo = models.IntegerField(choices=TIPO, default=1)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.titulo
