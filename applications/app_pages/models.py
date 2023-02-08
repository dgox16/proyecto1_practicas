from django.db import models


class BarraLinks(models.Model):
    titulo = models.CharField("Titulo:", max_length=50)
    url = models.CharField("URL:", max_length=50)
    orden = models.CharField("Orden:", max_length=50)
    icono = models.CharField("Icono:", max_length=50, default="face")
    is_active = models.BooleanField("Esta activo")

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.titulo
