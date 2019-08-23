from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token as DefaultTokenModel
from .utils import import_callable


class SimpleUser(AbstractUser):
    """Just user model"""

    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)


TokenModel = import_callable(
    getattr(settings, 'REST_AUTH_TOKEN_MODEL', DefaultTokenModel))