from django.db import models


class BarraLinks(models.Model):
    TIPO = (
        (1, "Acciones"),
        (2, "Catalogo trabajo"),
        (3, "Catalogo pld"),
        (4, "Catalogo personas"),
        (5, "Catalogo formularios"),
        (6, "Catalogo domicilo"),
    )

    titulo = models.CharField("Titulo:", max_length=50)
    url = models.CharField("URL:", max_length=50)
    orden = models.CharField("Orden:", max_length=50)
    is_active = models.BooleanField("Esta activo")
    tipo = models.IntegerField(choices=TIPO, default=1)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.titulo
