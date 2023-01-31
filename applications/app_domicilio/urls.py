from django.urls import path

from .views import VistaAgregarCalle, VistaAgregarDomicilio

app_name = "domicilio_app"

urlpatterns = [
    path(
        "domicilio/agregar", VistaAgregarDomicilio.as_view(), name="agregar_domicilio"
    ),
    path("calle/agregar", VistaAgregarCalle.as_view(), name="agregar_calle"),
]
