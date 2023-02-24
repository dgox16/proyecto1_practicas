from django import forms
from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper

from .models import (
    Banco,
    CatalogoCuenta,
    DetallePoliza,
    Poliza,
    PolizaEgreso,
    Proveedor,
)


class FormPoliza(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = (
            "tipo",
            "numero",
            "sucursal",
            "fecha",
            "concepto",
            "usuarioElabora",
            "usuarioAutoriza",
            "aplicacion",
            "fuente",
            "automatica",
        )
        widgets = {
            "tipo": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "numero": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
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
            "fecha": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control mb-5",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
            "concepto": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "usuarioElabora": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "usuarioAutoriza": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "aplicacion": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "fuente": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "automatica": forms.CheckboxInput(attrs={}),
        }


class FormDetallePoliza(forms.ModelForm):
    class Meta:
        model = DetallePoliza
        fields = (
            "cuenta",
            "sucursal",
            "cargo",
            "abono",
            "proveedor",
            "concepto",
            "iva",
        )
        widgets = {
            "cuenta": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("polizas_app:agregar_cuenta"),
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
            "cargo": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "abono": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "proveedor": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("polizas_app:agregar_proveedor"),
            ),
            "concepto": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "iva": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
        }


class FormCuenta(forms.ModelForm):
    class Meta:
        model = CatalogoCuenta
        fields = (
            "cuenta",
            "cuentaSiti",
            "nombre",
            "clasificacion",
            "grupo",
            "finalidad",
            "naturaleza",
            "afectable",
            "padre",
            "nivel",
            "balance",
            "catalogoMinimo",
            "nombreBalance",
            "nombreSiti",
            "cuentaPadreSiti",
            "cuentaAgrupar",
            "ordenSiti",
            "subCuentaSiti",
            "prorrateo",
        )
        widgets = {
            "cuenta": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "cuentaSiti": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "clasificacion": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "grupo": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "finalidad": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "naturaleza": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "afectable": forms.CheckboxInput(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "padre": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "nivel": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "balance": forms.CheckboxInput(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "catalogoMinimo": forms.CheckboxInput(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "nombreBalance": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "nombreSiti": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "cuentaPadreSiti": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "cuentaAgrupar": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "ordenSiti": forms.NumberInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "subCuentaSiti": forms.CheckboxInput(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "prorrateo": forms.CheckboxInput(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
        }


class FormProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = (
            "nombre",
            "domicilio",
            "rfc",
            "curp",
            "telefono",
            "tipo",
            "operacion",
            "regimen",
            "nombreExtranjero",
            "paisResidencia",
            "nacionalidad",
            "banco",
            "cuentaClabe",
        )
        widgets = {
            "nombre": forms.TextInput(
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
            "rfc": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "curp": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "telefono": forms.TextInput(
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
            "operacion": forms.Select(
                attrs={
                    "class": "form-control selectpicker mb-5",
                    "data-style": "btn btn-link",
                }
            ),
            "regimen": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "nombreExtranjero": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "paisResidencia": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "nacionalidad": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "banco": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("polizas_app:agregar_banco"),
            ),
            "cuentaClabe": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
        }


class FormBanco(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ("nombre",)
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
        }


class FormPolizaEgreso(forms.ModelForm):
    class Meta:
        model = PolizaEgreso
        fields = (
            "beneficiario",
            "banco",
            "cheque",
        )
        widgets = {
            "beneficiario": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
            "banco": AddAnotherWidgetWrapper(
                forms.Select(
                    attrs={
                        "class": "form-control selectpicker col-md-10 mb-5",
                        "data-style": "btn btn-link",
                    }
                ),
                reverse_lazy("polizas_app:agregar_banco"),
            ),
            "cheque": forms.TextInput(
                attrs={
                    "class": "form-control mb-5",
                }
            ),
        }
