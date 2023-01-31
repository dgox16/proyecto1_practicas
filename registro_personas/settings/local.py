from .base import *

DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "registro_personas/db.sqlite3"),  # ROOT dir f
    }
}

STATIC_URL = "/static/"


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(BASE_DIR, "applications/static"),)


#############################################################
#############################################################
