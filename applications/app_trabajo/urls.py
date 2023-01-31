from django.urls import path

from .views import (
    Vista_todas_empresas,
    Vista_todos_socios,
    Vista_todos_trabajos,
    VistaAgregarEmpresa,
    VistaAgregarFrecuencia,
    VistaAgregarPuesto,
)

app_name = "trabajo_app"


urlpatterns = [
    path("empresa/agregar", VistaAgregarEmpresa.as_view(), name="agregar_empresa"),
    path("puesto/agregar", VistaAgregarPuesto.as_view(), name="agregar_puesto"),
    path(
        "frecuencia/agregar",
        VistaAgregarFrecuencia.as_view(),
        name="agregar_frecuencia",
    ),
    path("empresas/", Vista_todas_empresas.as_view()),
    path("socios/", Vista_todos_socios.as_view()),
    path("trabajo/", Vista_todos_trabajos.as_view()),
]
