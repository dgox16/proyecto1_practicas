from django.urls import path

from .views import (
    AgregarClasificacion,
    AgregarSucursal,
    AgregarTipo,
    EliminarPersona,
    Vista_todas_personas,
    VistaAgregarPersona,
    VistaAgregarTodo,
    VistaModificarFormulario,
    VistaModificarPersona,
    VistaTodosFormularios,
)

app_name = "personas_app"


urlpatterns = [
    path("personas/", Vista_todas_personas.as_view(), name="todas_personas"),
    path("personas/<pk>/", VistaModificarPersona.as_view(), name="modificar_persona"),
    path("agregar/", VistaAgregarTodo.as_view(), name="agregar"),
    path("personas/agregar", VistaAgregarPersona.as_view(), name="agregar_persona"),
    path(
        "personas/sucursal/agregar", AgregarSucursal.as_view(), name="agregar_sucursal"
    ),
    path("personas/tipo/agregar", AgregarTipo.as_view(), name="agregar_tipo"),
    path(
        "personas/clasificacion/agregar",
        AgregarClasificacion.as_view(),
        name="agregar_clasificacion",
    ),
    path("personas/eliminar/<pk>/", EliminarPersona.as_view()),
    path("formularios/", VistaTodosFormularios.as_view(), name="todos_formularios"),
    path(
        "formularios/<pk>/",
        VistaModificarFormulario.as_view(),
        name="modificar_formulario",
    ),
]
