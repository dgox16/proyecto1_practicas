from django.db import models


class PldManager(models.Manager):
    def buscar_pld(self, kword):
        return self.filter(actividadPld_id__icontains=kword)
