from django.urls import path

from .views import (
    Vista_todas_empresas,
    Vista_todos_socios,
    Vista_todos_trabajos,
    VistaAgregarEmpresa,
    VistaAgregarFrecuencia,
    VistaAgregarPuesto,
    VistaModificarEmpresa,
)

app_name = "trabajo_app"


urlpatterns = [
    path("empresas/agregar", VistaAgregarEmpresa.as_view(), name="agregar_empresa"),
    path("empresas/<pk>/", VistaModificarEmpresa.as_view(), name="modificar_empresa"),
    path("puesto/agregar", VistaAgregarPuesto.as_view(), name="agregar_puesto"),
    path(
        "frecuencia/agregar",
        VistaAgregarFrecuencia.as_view(),
        name="agregar_frecuencia",
    ),
    path("empresas/", Vista_todas_empresas.as_view(), name="todas_empresas"),
    path("socios/", Vista_todos_socios.as_view()),
    path("trabajo/", Vista_todos_trabajos.as_view()),
]
