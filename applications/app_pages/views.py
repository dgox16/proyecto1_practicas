from django.views.generic.base import ContextMixin

from applications.app_pages.models import BarraLinks


class BarraLateral(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["links_acciones"] = BarraLinks.objects.filter(tipo=1)
        context["links_catalogo_trabajos"] = BarraLinks.objects.filter(tipo=2)
        context["links_catalogo_pld"] = BarraLinks.objects.filter(tipo=3)
        context["links_catalogo_persona"] = BarraLinks.objects.filter(tipo=4)
        context["links_catalogo_formulario"] = BarraLinks.objects.filter(tipo=5)
        context["links_catalogo_domicilio"] = BarraLinks.objects.filter(tipo=6)
        return context
