from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings




class User(AbstractUser):

    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]

    def __str__(self):
        return str(self.username )
    
    

class Seller(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    company_name=models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.seller.username)

    
class Customer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer=models.OneToOneField(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=100)


    def __str__(self):
        return str(self.customer.username)
    
    

