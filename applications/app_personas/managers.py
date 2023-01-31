from django.db import models
from django.db.models import Q


class PersonaManager(models.Manager):
    def buscar_persona(self, kword):
        return self.filter(
            Q(nombre__icontains=kword)
            | Q(apellidoPaterno__icontains=kword)
            | Q(apellidoMaterno__icontains=kword)
        )
