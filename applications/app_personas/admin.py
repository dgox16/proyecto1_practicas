from django.apps import apps
from django.contrib import admin

app_personas = apps.get_app_config("app_personas")
admin.site.register(app_personas.get_models())
