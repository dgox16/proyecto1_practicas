from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django_addanother.views import CreatePopupMixin

from .forms import FormEmpresa, FormFrecuencia, FormPuesto
from .models import Empresa, Socio, Trabajo


class VistaAgregarEmpresa(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "trabajo/agregar_empresa.html"
    login_url = "/login/"
    form_class = FormEmpresa

    def get_context_data(self, **kwargs):
        form = FormEmpresa()
        context = super(VistaAgregarEmpresa, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaModificarEmpresa(LoginRequiredMixin, CreatePopupMixin, UpdateView):
    template_name = "trabajo/agregar_empresa.html"
    login_url = "/login/"
    model = Empresa
    form_class = FormEmpresa
    success_url = reverse_lazy("trabajo_app:todas_empresas")

    def get_context_data(self, **kwargs):
        context = super(VistaModificarEmpresa, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        return context


class VistaAgregarFrecuencia(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "trabajo/agregar_frecuencia.html"
    login_url = "/login/"
    form_class = FormFrecuencia

    def get_context_data(self, **kwargs):
        form = FormFrecuencia()
        context = super(VistaAgregarFrecuencia, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaAgregarPuesto(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "trabajo/agregar_puesto.html"
    login_url = "/login/"
    form_class = FormPuesto

    def get_context_data(self, **kwargs):
        form = FormPuesto()
        context = super(VistaAgregarPuesto, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class Vista_todas_empresas(LoginRequiredMixin, ListView):
    template_name = "trabajo/todas_empresas.html"
    context_object_name = "empresas"
    login_url = "/login/"

    def get_queryset(self):
        kword = self.request.GET.get("kword", "")
        queryset = Empresa.objects.buscar_empresa(kword)
        return queryset


class Vista_todos_socios(LoginRequiredMixin, ListView):
    template_name = "trabajo/todos_socios.html"
    context_object_name = "socios"
    model = Socio
    login_url = "/login/"


class Vista_todos_trabajos(LoginRequiredMixin, ListView):
    template_name = "trabajo/todos_trabajos.html"
    context_object_name = "trabajos"
    model = Trabajo
    login_url = "/login/"
