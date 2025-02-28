from.settings import *
import os
from.settings import BASE_DIR
import dj_database_url
DEBUG = False
ALLOWED_HOST = [os.environ.get('RENDER_EXTERNAL_HOSTNAME')]
CSRF_TRUSTED_ORIGINS = ['HTTPS://'+os.environ['RENDER_EXTERNAL_HOSTNAME']]
DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]


CORS_ALLOWED_ORIGINS = [
    # "http://localhost:3000",  
    # "http://127.0.0.1:3000",
    "https://thankful-tree-07e1b3610.4.azurestaticapps.net"
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}




DATABASES = {
    'default': dj_database_url.config(
    # Replace this value with your local database's connection string.
        default=os.environ["DATABASE_URL"],
    conn_max_age=600
    )
        
    
}