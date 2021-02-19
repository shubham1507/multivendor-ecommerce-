from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from phone_field import PhoneField
from address.models import AddressField


class User(AbstractUser):

    user_type_data=((1,"Seller"),(2,"Customer"),(3,"Admin"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
    contact = PhoneField(blank=True, help_text='Contact phone number')
    alt_contact = PhoneField(blank=True, help_text='Contact phone number')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]
    
class Seller(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller=models.OneToOneField(User,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
   

class Customer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer=models.OneToOneField(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Admin(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin=models.OneToOneField(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


class Address(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = AddressField()
    address_line_2 = AddressField(related_name='+', blank=True, null=True)
    is_delivery_address = models.BooleanField(_('IsDeliveryAddress'), default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    insertedby = models.ForeignKey(User, on_delete=models.CASCADE)


class Vendor(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    address = AddressField()
    _type
    is_vendor_shipper = models.BooleanField(default=False)
    contact = PhoneField(blank=True, help_text='Contact phone number')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    insertedby = models.ForeignKey(User, on_delete=models.CASCADE)

class Shipper(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=255)
    _type = 
    transport_mode =
    contact = PhoneField(blank=True, help_text='Contact phone number')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    insertedby = models.ForeignKey(User, on_delete=models.CASCADE)




    

    