from django.views.generic.base import ContextMixin

from applications.app_pages.models import BarraLinks


class BarraLateral(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["links_principales"] = BarraLinks.objects.filter(tipo=1)
        context["links_catalogo_vistas"] = BarraLinks.objects.filter(tipo=2)
        return context
