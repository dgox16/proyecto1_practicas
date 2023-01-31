from django import forms
from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper

from applications.app_trabajo.models import Empresa, Frecuencia, Puesto, Socio, Trabajo


class FormSocio(forms.ModelForm):
    class Meta:
        model = Socio
        fields = (
            "persona",
            "curp",
            "rfc",
            "Identificacion",
            "NumeroIdentificacion",
            "email",
            "domicilio",
            "pld",
        )
        widgets = {
            "persona": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("personas_app:agregar_persona"),
            ),
            "curp": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "rfc": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "Identificacion": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "NumeroIdentificacion": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "domicilio": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("domicilio_app:agregar_domicilio"),
            ),
            "pld": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("pld_app:agregar_PLD"),
            ),
        }


class FormTrabajo(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = (
            "persona",
            "empresa",
            "puesto",
            "arraigoLaboralAnterior",
            "igresoOrdinario",
            "otrosIngresos",
            "conceptoIngresos",
            "telefono",
        )
        widgets = {
            "persona": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("personas_app:agregar_persona"),
            ),
            "empresa": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("trabajo_app:agregar_empresa"),
            ),
            "puesto": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("trabajo_app:agregar_puesto"),
            ),
            "arraigoLaboralAnterior": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "igresoOrdinario": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "otrosIngresos": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "conceptoIngresos": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "telefono": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class FormEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = (
            "nombre",
            "domicilio",
            "telefono",
            "empleosFijos",
            "frecuencia",
        )
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "domicilio": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("domicilio_app:agregar_domicilio"),
            ),
            "telefono": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "empleosFijos": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "frecuencia": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("trabajo_app:agregar_frecuencia"),
            ),
        }


class FormFrecuencia(forms.ModelForm):
    class Meta:
        model = Frecuencia
        fields = (
            "nombre",
            "dias",
            "meses",
        )
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "dias": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "meses": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class FormPuesto(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = ("nombre",)
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
