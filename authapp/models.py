from django.contrib.auth.models import User, AbstractUser
from django.db import models


class SimpleUser(AbstractUser):
    """Just user model"""

    name = models.CharField(max_length=32)
    mail = models.EmailField(max_length=32)
