from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django_addanother.views import CreatePopupMixin

from .forms import (
    FormParentesco,
    FormPld,
    FormPldActividad,
    FormPldEspecificacion,
    FormPldExpuesta,
    FormPldOcupacion,
)
from .models import Pld


class VistaAgregarPld(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "pld/agregar_pld.html"
    login_url = "/login/"
    form_class = FormPld

    def get_context_data(self, **kwargs):
        form = FormPld()
        context = super(VistaAgregarPld, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaAgregarPldActividad(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "pld/agregar_pldactividad.html"
    login_url = "/login/"
    form_class = FormPldActividad

    def get_context_data(self, **kwargs):
        form = FormPldActividad()
        context = super(VistaAgregarPldActividad, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaAgregarPldExpuesta(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "pld/agregar_pldexpuesta.html"
    login_url = "/login/"
    form_class = FormPldExpuesta

    def get_context_data(self, **kwargs):
        form = FormPldExpuesta()
        context = super(VistaAgregarPldExpuesta, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaAgregarParentesco(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "pld/agregar_parentesco.html"
    login_url = "/login/"
    form_class = FormParentesco

    def get_context_data(self, **kwargs):
        form = FormParentesco()
        context = super(VistaAgregarParentesco, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaAgregarPldEspecificacion(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "pld/agregar_pldespecificacion.html"
    login_url = "/login/"
    form_class = FormPldEspecificacion

    def get_context_data(self, **kwargs):
        form = FormPldEspecificacion()
        context = super(VistaAgregarPldEspecificacion, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaAgregarPldOcupacion(LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "pld/agregar_pldocupacion.html"
    login_url = "/login/"
    form_class = FormPldOcupacion

    def get_context_data(self, **kwargs):
        form = FormPldOcupacion()
        context = super(VistaAgregarPldOcupacion, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VerPLD(LoginRequiredMixin, ListView):
    template_name = "pld/todos_pld.html"
    context_object_name = "pld"
    model = Pld
    login_url = "/login/"
