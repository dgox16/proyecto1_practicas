from django.views.generic.base import ContextMixin

from applications.app_pages.models import BarraLinks


class BarraLateral(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["links_acciones"] = BarraLinks.objects.filter(tipo=1, solo_admin=False)
        context["links_acciones_admin"] = BarraLinks.objects.filter(tipo=1)
        context["links_catalogo_trabajos"] = BarraLinks.objects.filter(
            tipo=2, solo_admin=False
        )
        context["links_catalogo_trabajos_admin"] = BarraLinks.objects.filter(tipo=2)
        context["links_catalogo_pld"] = BarraLinks.objects.filter(
            tipo=3, solo_admin=False
        )
        context["links_catalogo_pld_admin"] = BarraLinks.objects.filter(tipo=3)
        context["links_catalogo_persona"] = BarraLinks.objects.filter(
            tipo=4, solo_admin=False
        )
        context["links_catalogo_persona_admin"] = BarraLinks.objects.filter(tipo=4)
        context["links_catalogo_formulario"] = BarraLinks.objects.filter(
            tipo=5, solo_admin=False
        )
        context["links_catalogo_formulario_admin"] = BarraLinks.objects.filter(tipo=5)
        context["links_catalogo_domicilio"] = BarraLinks.objects.filter(
            tipo=6, solo_admin=False
        )
        context["links_catalogo_domicilio_admin"] = BarraLinks.objects.filter(tipo=6)
        context["links_catalogo_polizas"] = BarraLinks.objects.filter(
            tipo=7, solo_admin=False
        )
        context["links_catalogo_polizas_admin"] = BarraLinks.objects.filter(tipo=7)

        return context
