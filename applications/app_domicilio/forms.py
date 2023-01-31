from django import forms
from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper

from .models import Calle, Domicilio


class FormDomicilio(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = (
            "cp",
            "colonia",
            "calle",
            "entrecalle",
            "ycalle",
            "numero",
            "interior",
            "geolocalizacion",
        )
        widgets = {
            "cp": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "colonia": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "calle": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("domicilio_app:agregar_calle"),
            ),
            "entrecalle": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("domicilio_app:agregar_calle"),
            ),
            "ycalle": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("domicilio_app:agregar_calle"),
            ),
            "numero": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "interior": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "geolocalizacion": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class FormCalle(forms.ModelForm):
    class Meta:
        model = Calle
        fields = (
            "nombre",
            "tipo",
        )
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "tipo": forms.Select(
                attrs={
                    "class": "form-control selectpicker",
                    "data-style": "btn btn-link",
                }
            ),
        }
