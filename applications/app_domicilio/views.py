from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django_addanother.views import CreatePopupMixin

from .forms import FormCalle, FormDomicilio


class VistaAgregarDomicilio(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "domicilio/agregar_domicilio.html"
    login_url = "/login/"
    form_class = FormDomicilio

    def get_context_data(self, **kwargs):
        form = FormDomicilio()
        context = super(VistaAgregarDomicilio, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaAgregarCalle(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "domicilio/agregar_calle.html"
    login_url = "/login/"
    form_class = FormCalle

    def get_context_data(self, **kwargs):
        form = FormCalle()
        context = super(VistaAgregarCalle, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context
