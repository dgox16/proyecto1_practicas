from django import forms
from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper

from .models import Persona


class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = (
            "nombre",
            "apellidoPaterno",
            "apellidoMaterno",
            "identificador",
            "sexo",
            "user",
            "sucursal",
            "tipo",
            "clasificacion",
            "phone",
        )
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "apellidoPaterno": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "apellidoMaterno": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "identificador": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "sexo": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "user": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "sucursal": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("personas_app:agregar_sucursal"),
            ),
            "tipo": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("personas_app:agregar_tipo"),
            ),
            "clasificacion": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("personas_app:agregar_clasificacion"),
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
