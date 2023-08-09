from django.db import models
from django.contrib.auth.models import AbstractUser


class RMDUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
