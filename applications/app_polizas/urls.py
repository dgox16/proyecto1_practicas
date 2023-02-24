from django.urls import path

from .views import (
    VistaAgregarBanco,
    VistaAgregarCuenta,
    VistaAgregarProveedor,
    VistaAgregarTodo,
)

app_name = "polizas_app"
urlpatterns = [
    path("polizas/agregar", VistaAgregarTodo.as_view(), name="agregar"),
    path("polizas/cuenta/agregar", VistaAgregarCuenta.as_view(), name="agregar_cuenta"),
    path(
        "polizas/proveedor/agregar",
        VistaAgregarProveedor.as_view(),
        name="agregar_proveedor",
    ),
    path("polizas/banco/agregar", VistaAgregarBanco.as_view(), name="agregar_banco"),
]
