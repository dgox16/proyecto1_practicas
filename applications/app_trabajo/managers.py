from django.db import models


class EmpresaManager(models.Manager):
    def buscar_empresa(self, kword):
        return self.filter(nombre__icontains=kword)
