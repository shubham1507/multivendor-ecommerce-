from django.db import models
from django_postgres_extensions.models.fields import ArrayField
from api.v1.accounts.models import Seller,User
import uuid



class Varient(models.Model):

    seller_id = models.ForeignKey(Seller,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

