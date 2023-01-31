from django.apps import apps
from django.contrib import admin

app_domicilio = apps.get_app_config("app_domicilio")
admin.site.register(app_domicilio.get_models())
