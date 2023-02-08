from django.views.generic.base import ContextMixin

from applications.app_pages.models import BarraLinks


class BarraLateral(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["nav_links"] = BarraLinks.objects.filter(is_active=True)
        return context
