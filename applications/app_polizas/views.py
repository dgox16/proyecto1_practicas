from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django_addanother.views import CreatePopupMixin

from applications.app_pages.views import BarraLateral

from .forms import (
    FormBanco,
    FormCuenta,
    FormDetallePoliza,
    FormPoliza,
    FormPolizaEgreso,
    FormProveedor,
)


class VistaAgregarTodo(BarraLateral, LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "polizas/agregar.html"
    login_url = "/login/"
    success_url = reverse_lazy("personas_app:todas_personas")
    form_class = FormPoliza
    form_class_detalle_poliza = FormDetallePoliza
    form_class_poliza_egreso = FormPolizaEgreso

    def post(self, request, *args, **kwargs):
        poliza_form = self.form_class(request.POST)
        detalleP_form = self.form_class_detalle_poliza(request.POST)
        polizaE_form = self.form_class_poliza_egreso(request.POST)
        print(polizaE_form)

        poliza = poliza_form.save(commit=False)
        if poliza_form.is_valid() and detalleP_form.is_valid():
            detallePoliza = detalleP_form.save(commit=False)
            detallePoliza.poliza = poliza
            poliza.save()
            detallePoliza.save()
            if polizaE_form.is_valid():
                print("Aqui estoy---------------------------------------")
                polizaEgreso = polizaE_form.save(commit=False)
                polizaEgreso.poliza = poliza
                polizaEgreso.save()
            return HttpResponseRedirect(reverse("personas_app:todos_formularios"))
        else:
            return self.form_invalid(**kwargs)

    def get_context_data(self, **kwargs):
        form = FormPoliza()
        formPoliza = FormDetallePoliza()
        formPolizaEgreso = FormPolizaEgreso
        context = super(VistaAgregarTodo, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["formPoliza"] = form
        context["formDetallePoliza"] = formPoliza
        context["formPolizaEgreso"] = formPolizaEgreso
        return context


class VistaAgregarCuenta(
    BarraLateral, LoginRequiredMixin, CreatePopupMixin, CreateView
):
    template_name = "pld/agregar_pldactividad.html"
    login_url = "/login/"
    form_class = FormCuenta

    def get_context_data(self, **kwargs):
        form = FormCuenta()
        context = super(VistaAgregarCuenta, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaAgregarProveedor(
    BarraLateral, LoginRequiredMixin, CreatePopupMixin, CreateView
):
    template_name = "pld/agregar_pldactividad.html"
    login_url = "/login/"
    form_class = FormProveedor

    def get_context_data(self, **kwargs):
        form = FormProveedor()
        context = super(VistaAgregarProveedor, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaAgregarBanco(BarraLateral, LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "pld/agregar_pldactividad.html"
    login_url = "/login/"
    form_class = FormBanco

    def get_context_data(self, **kwargs):
        form = FormBanco()
        context = super(VistaAgregarBanco, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context
