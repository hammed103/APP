from .base import *
from .base import env


DEBUG = True


SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-0^kx__fa260cxcnrfh9^7e1i=+q0m==0ln-2((wol_7_!4(iwo",
)


ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
