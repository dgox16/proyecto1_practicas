"""registro_personas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, re_path


def my_view(request):
    return redirect("/personas/")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", my_view),
    re_path("", include("applications.app_auth.urls")),
    re_path("", include("applications.app_personas.urls")),
    re_path("", include("applications.app_trabajo.urls")),
    re_path("", include("applications.app_PLD.urls")),
    re_path("", include("applications.app_domicilio.urls")),
    re_path("", include("applications.app_polizas.urls")),
]
