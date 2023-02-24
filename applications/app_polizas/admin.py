from django.apps import apps
from django.contrib import admin

app_polizas = apps.get_app_config("app_polizas")
admin.site.register(app_polizas.get_models())
