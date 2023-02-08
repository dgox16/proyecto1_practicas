from django.apps import apps
from django.contrib import admin

app_pages = apps.get_app_config("app_pages")
admin.site.register(app_pages.get_models())
