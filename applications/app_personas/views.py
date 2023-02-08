from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django_addanother.views import CreatePopupMixin

from applications.app_pages.views import BarraLateral
from applications.app_PLD.forms import FormPld
from applications.app_PLD.models import Pld
from applications.app_trabajo.forms import FormSocio, FormTrabajo
from applications.app_trabajo.models import Socio, Trabajo

from .forms import FormPersona
from .models import Clasificacion, Formulario, Persona, Sucursal, Tipo


class VistaAgregarTodo(BarraLateral, LoginRequiredMixin, CreatePopupMixin, CreateView):
    template_name = "personas/formulario.html"
    login_url = "/login/"
    success_url = reverse_lazy("personas_app:todas_personas")
    form_class = FormPersona
    form_class_pld = FormPld
    form_class_socio = FormSocio
    form_class_trabajo = FormTrabajo

    def post(self, request, *args, **kwargs):
        persona_form = self.form_class(request.POST)
        pld_form = self.form_class_pld(request.POST)
        socio_form = self.form_class_socio(request.POST)
        trabajo_form = self.form_class_trabajo(request.POST)

        persona = persona_form.save(commit=False)
        if persona_form.is_valid() and pld_form.is_valid() and socio_form.is_valid():
            pld = pld_form.save(commit=False)
            pld.persona = persona
            pld.perfilFrecuenciaCaptacion = 0
            pld.perfilMaximaCaptacion = 0
            pld.perfilFrecuenciaPrestamo = 0
            pld.perfilMaximoPrestamo = 0
            socio = socio_form.save(commit=False)
            socio.persona = persona
            socio.pld = pld
            trabajo = trabajo_form.save(commit=False)
            trabajo.persona = persona
            persona.save()
            pld.save()
            socio.save()
            trabajo.save()
            formulario = Formulario(
                persona=persona, pld=pld, socio=socio, trabajo=trabajo
            )
            formulario.save()
            return HttpResponseRedirect(reverse("personas_app:todos_formularios"))
        else:
            return self.form_invalid(**kwargs)

    def get_context_data(self, **kwargs):
        form = FormPersona()
        formPLD = FormPld()
        formSocio = FormSocio()
        formTrabajo = FormTrabajo()
        context = super(VistaAgregarTodo, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        context["formPLD"] = formPLD
        context["formSocio"] = formSocio
        context["formTrabajo"] = formTrabajo
        return context


class VistaAgregarPersona(
    BarraLateral, LoginRequiredMixin, CreatePopupMixin, CreateView
):
    template_name = "personas/agregar_persona.html"
    login_url = "/login/"
    form_class = FormPersona

    def get_context_data(self, **kwargs):
        form = FormPersona()
        context = super(VistaAgregarPersona, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        return context


class VistaModificarPersona(
    BarraLateral, LoginRequiredMixin, CreatePopupMixin, UpdateView
):
    template_name = "personas/agregar_persona.html"
    login_url = "/login/"
    model = Persona
    form_class = FormPersona
    success_url = reverse_lazy("personas_app:todas_personas")

    def get_context_data(self, **kwargs):
        context = super(VistaModificarPersona, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        return context


class AgregarSucursal(BarraLateral, CreatePopupMixin, CreateView):
    template_name = "personas/agregar_sucursal.html"
    model = Sucursal
    fields = ["name"]


class AgregarTipo(BarraLateral, CreatePopupMixin, CreateView):
    template_name = "personas/agregar_tipo.html"
    model = Tipo
    fields = ["name"]


class AgregarClasificacion(BarraLateral, CreatePopupMixin, CreateView):
    template_name = "personas/agregar_clasificacion.html"
    model = Clasificacion
    fields = ["name"]


class Vista_todas_personas(BarraLateral, LoginRequiredMixin, ListView):
    template_name = "personas/todas_personas.html"
    context_object_name = "personas"
    login_url = "/login/"

    def get_queryset(self):
        kword = self.request.GET.get("kword", "")
        queryset = Persona.objects.buscar_persona(kword)
        return queryset


class EliminarPersona(BarraLateral, LoginRequiredMixin, DeleteView):
    template_name = "personas/eliminar_persona.html"
    login_url = "/login/"
    model = Persona
    success_url = "/personas"


class VistaTodosFormularios(BarraLateral, LoginRequiredMixin, ListView):
    template_name = "personas/todos_formularios.html"
    context_object_name = "formularios"
    login_url = "/login/"
    model = Formulario


class VistaModificarFormulario(BarraLateral, LoginRequiredMixin, UpdateView):
    template_name = "personas/formulario.html"
    login_url = "/login/"
    success_url = reverse_lazy("personas_app:todas_personas")
    model = Formulario
    form_class = FormPersona
    form_class_pld = FormPld
    form_class_socio = FormSocio
    form_class_trabajo = FormTrabajo

    def post(self, request, *args, **kwargs):
        idPersona = self.get_object().persona.id
        obj_persona = get_object_or_404(Persona, id=idPersona)
        persona_form = self.form_class(request.POST, instance=obj_persona)
        idPld = self.get_object().pld.id
        obj_pld = get_object_or_404(Pld, id=idPld)
        pld_form = self.form_class_pld(request.POST, instance=obj_pld)
        idSocio = self.get_object().socio.id
        obj_socio = get_object_or_404(Socio, id=idSocio)
        socio_form = self.form_class_socio(request.POST, instance=obj_socio)
        idTrabajo = self.get_object().trabajo.id
        obj_trabajo = get_object_or_404(Trabajo, id=idTrabajo)
        trabajo_form = self.form_class_trabajo(request.POST, instance=obj_trabajo)

        persona = persona_form.save(commit=False)
        if persona_form.is_valid() and pld_form.is_valid():
            pld = pld_form.save(commit=False)
            socio = socio_form.save(commit=False)
            trabajo = trabajo_form.save(commit=False)
            print(persona)
            persona.save()
            pld.save()
            socio.save()
            trabajo.save()
            return HttpResponseRedirect(reverse("personas_app:todos_formularios"))
        else:
            return HttpResponseRedirect(reverse("personas_app:todas_personas"))

    def get_context_data(self, **kwargs):
        idPersona = self.get_object().persona.id
        idPld = self.get_object().pld.id
        idSocio = self.get_object().socio.id
        idTrabajo = self.get_object().trabajo.id
        form = FormPersona(instance=Persona.objects.get(id=idPersona))
        formPLD = FormPld(instance=Pld.objects.get(id=idPld))
        formSocio = FormSocio(instance=Socio.objects.get(id=idSocio))
        formTrabajo = FormTrabajo(instance=Trabajo.objects.get(id=idTrabajo))
        context = super(VistaModificarFormulario, self).get_context_data(**kwargs)
        context["jquery"] = "admin/js/vendor/jquery/jquery.js"
        context["form"] = form
        context["formPLD"] = formPLD
        context["formSocio"] = formSocio
        context["formTrabajo"] = formTrabajo
        return context
