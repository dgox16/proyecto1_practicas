from django import forms
from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper

from applications.app_personas.models import Persona

from .models import (
    Parentesco,
    Pld,
    Pldactividad,
    Pldespecificacion,
    PldExpuesta,
    Pldocupacion,
)


class FormPld(forms.ModelForm):
    class Meta:
        model = Pld
        fields = (
            "actividadPld",
            "frecuenciaCaptacion",
            "maximaCaptacion",
            "frecuenciaPrestamo",
            "maximoPrestamo",
            "tipoExpuesta",
            "personaExpuesta",
        )
        widgets = {
            "actividadPld": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("pld_app:agregar_actividadPLD"),
            ),
            "frecuenciaCaptacion": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "maximaCaptacion": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "frecuenciaPrestamo": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "maximoPrestamo": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "tipoExpuesta": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "personaExpuesta": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("pld_app:agregar_expuestaPLD"),
            ),
        }


class FormPldActividad(forms.ModelForm):
    class Meta:
        model = Pldactividad
        fields = (
            "especificacionPld",
            "claveSiti",
            "nombre",
        )
        widgets = {
            "especificacionPld": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("pld_app:agregar_especificacionPLD"),
            ),
            "claveSiti": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class FormPldExpuesta(forms.ModelForm):
    class Meta:
        model = PldExpuesta
        fields = (
            "funcionPublica",
            "familiarFuncionario",
            "nombreFuncionario",
        )
        widgets = {
            "funcionPublica": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "familiarFuncionario": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("pld_app:agregar_parentesco"),
            ),
            "nombreFuncionario": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class FormParentesco(forms.ModelForm):
    class Meta:
        model = Parentesco
        fields = ("nombre", "tipo", "grado", "tipoId")
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "tipo": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "grado": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "tipoId": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class FormPldEspecificacion(forms.ModelForm):
    class Meta:
        model = Pldespecificacion
        fields = ("ocupacionPld", "nombre")
        widgets = {
            "ocupacionPld": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("pld_app:agregar_ocupacionPLD"),
            ),
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
        }


class FormPldOcupacion(forms.ModelForm):
    class Meta:
        model = Pldocupacion
        fields = {
            "nombre",
        }
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
        }


class PLDNewForm(forms.ModelForm):
    class Meta:
        model = PldExpuesta
        fields = ("funcionPublica", "familiarFuncionario", "nombreFuncionario")
        widgets = {
            "familiarFuncionario": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("pld_app:add2"),
            ),
            "nombreFuncionario": forms.TextInput(
                attrs={
                    "class": "form-control|",
                }
            ),
        }
