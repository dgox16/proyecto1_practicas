from django.urls import path

from .views import (
    VerPLD,
    VistaAgregarParentesco,
    VistaAgregarPld,
    VistaAgregarPldActividad,
    VistaAgregarPldEspecificacion,
    VistaAgregarPldExpuesta,
    VistaAgregarPldOcupacion,
)

app_name = "pld_app"

urlpatterns = [
    path("pld/agregar", VistaAgregarPld.as_view(), name="agregar_PLD"),
    path("pld/", VerPLD.as_view(), name="ver_pld"),
    path(
        "pld/actividad/agregar",
        VistaAgregarPldActividad.as_view(),
        name="agregar_actividadPLD",
    ),
    path(
        "pld/expuesta/agregar",
        VistaAgregarPldExpuesta.as_view(),
        name="agregar_expuestaPLD",
    ),
    path(
        "pld/parentesco/agregar",
        VistaAgregarParentesco.as_view(),
        name="agregar_parentesco",
    ),
    path(
        "pld/especificacion/agregar",
        VistaAgregarPldEspecificacion.as_view(),
        name="agregar_especificacionPLD",
    ),
    path(
        "pld/ocupacion/agregar",
        VistaAgregarPldOcupacion.as_view(),
        name="agregar_ocupacionPLD",
    ),
]
