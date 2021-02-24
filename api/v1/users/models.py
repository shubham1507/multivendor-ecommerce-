from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    # Boolean fields to select the type of account.
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)