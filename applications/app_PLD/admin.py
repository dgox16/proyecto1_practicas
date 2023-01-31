from django.apps import apps
from django.contrib import admin

app_PLD = apps.get_app_config("app_PLD")
admin.site.register(app_PLD.get_models())
