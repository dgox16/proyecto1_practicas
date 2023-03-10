from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django_addanother.views import CreatePopupMixin

from applications.app_pages.views import BarraLateral
from applications.app_polizas.models import Poliza

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
    success_url = reverse_lazy("polizas_app:todas_polizas")
    form_class = FormPoliza
    form_class_detalle_poliza = FormDetallePoliza
    form_class_poliza_egreso = FormPolizaEgreso

    global numDetalles
    numDetalles = 50

    def post(self, request, *args, **kwargs):
        poliza_form = self.form_class(request.POST)
        polizaE_form = self.form_class_poliza_egreso(request.POST)
        poliza = poliza_form.save(commit=False)

        poliza.numero = 1
        poliza.usuarioElabora = request.user
        if poliza_form.is_valid():
            poliza.save()
            if polizaE_form.is_valid():
                polizaEgreso = polizaE_form.save(commit=False)
                polizaEgreso.poliza = poliza
                polizaEgreso.save()

            for n in range(numDetalles):
                detalleForm = self.form_class_detalle_poliza(
                    request.POST, prefix="_" + str(n + 1)
                )
                if detalleForm.is_valid():
                    detallePoliza = detalleForm.save(commit=False)
                    detallePoliza.poliza = poliza
                    detallePoliza.save()

            return HttpResponseRedirect(reverse("polizas_app:todas_polizas"))
        else:
            return self.form_invalid(**kwargs)

    def get_context_data(self, **kwargs):
        form = FormPoliza()
        formsDetalle = []
        for n in range(numDetalles):
            formsDetalle.append(FormDetallePoliza(prefix="_" + str(n + 1)))
        formPolizaEgreso = FormPolizaEgreso()
        context = super(VistaAgregarTodo, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["formPoliza"] = form
        context["forms"] = formsDetalle
        context["formPolizaEgreso"] = formPolizaEgreso
        return context


class VistaVerPolizas(BarraLateral, LoginRequiredMixin, ListView):
    template_name = "polizas/ver_polizas.html"
    login_url = "/login/"
    context_object_name = "polizas"
    model = Poliza


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
