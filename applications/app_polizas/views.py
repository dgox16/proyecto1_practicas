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

    def post(self, request, *args, **kwargs):
        poliza_form = self.form_class(request.POST)
        detalleP_form = self.form_class_detalle_poliza(request.POST, prefix="_0")
        detalleP1_form = self.form_class_detalle_poliza(request.POST, prefix="_1")
        detalleP2_form = self.form_class_detalle_poliza(request.POST, prefix="_2")
        detalleP3_form = self.form_class_detalle_poliza(request.POST, prefix="_3")
        detalleP4_form = self.form_class_detalle_poliza(request.POST, prefix="_4")
        detalleP5_form = self.form_class_detalle_poliza(request.POST, prefix="_5")
        polizaE_form = self.form_class_poliza_egreso(request.POST)

        poliza = poliza_form.save(commit=False)
        poliza.numero = 1
        poliza.usuarioElabora = request.user
        if poliza_form.is_valid() and detalleP_form.is_valid():
            detallePoliza = detalleP_form.save(commit=False)
            detallePoliza.poliza = poliza
            poliza.save()
            detallePoliza.save()
            if polizaE_form.is_valid():
                polizaEgreso = polizaE_form.save(commit=False)
                polizaEgreso.poliza = poliza
                polizaEgreso.save()
            if detalleP1_form.is_valid():
                detallePoliza1 = detalleP1_form.save(commit=False)
                detallePoliza1.poliza = poliza
                detallePoliza1.save()
            if detalleP2_form.is_valid():
                detallePoliza2 = detalleP2_form.save(commit=False)
                detallePoliza2.poliza = poliza
                detallePoliza2.save()
            if detalleP3_form.is_valid():
                detallePoliza3 = detalleP3_form.save(commit=False)
                detallePoliza3.poliza = poliza
                detallePoliza3.save()
            if detalleP4_form.is_valid():
                detallePoliza4 = detalleP4_form.save(commit=False)
                detallePoliza4.poliza = poliza
                detallePoliza4.save()
            if detalleP5_form.is_valid():
                detallePoliza5 = detalleP5_form.save(commit=False)
                detallePoliza5.poliza = poliza
                detallePoliza5.save()

            return HttpResponseRedirect(reverse("polizas_app:todas_polizas"))
        else:
            return self.form_invalid(**kwargs)

    def get_context_data(self, **kwargs):
        form = FormPoliza()
        formPoliza = FormDetallePoliza(prefix="_0")
        formPoliza1 = FormDetallePoliza(prefix="_1")
        formPoliza2 = FormDetallePoliza(prefix="_2")
        formPoliza3 = FormDetallePoliza(prefix="_3")
        formPoliza4 = FormDetallePoliza(prefix="_4")
        formPoliza5 = FormDetallePoliza(prefix="_5")
        formPolizaEgreso = FormPolizaEgreso()
        context = super(VistaAgregarTodo, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["formPoliza"] = form
        context["formDetallePoliza"] = formPoliza
        context["formDetallePoliza1"] = formPoliza1
        context["formDetallePoliza2"] = formPoliza2
        context["formDetallePoliza3"] = formPoliza3
        context["formDetallePoliza4"] = formPoliza4
        context["formDetallePoliza5"] = formPoliza5
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
