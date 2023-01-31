from django.apps import apps
from django.contrib import admin

app_trabajo = apps.get_app_config("app_trabajo")
admin.site.register(app_trabajo.get_models())
