from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings
from phone_field import PhoneField
from address.models import AddressField


# class User(AbstractUser):

#     user_type_data=((1,"Seller"),(2,"Customer"),(3,"Admin"))

#     user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
    

#     # @property
#     # def user__username(self):
#     #     return self.user.username

#     # def __unicode__(self):
#     #     return self.user.username
    
# class Seller(models.Model):

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     seller=models.OneToOneField(User,on_delete=models.CASCADE)
    
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
   

# class Customer(models.Model):

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     customer=models.OneToOneField(User,on_delete=models.CASCADE)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)

# class Admin(models.Model):

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     admin=models.OneToOneField(User,on_delete=models.CASCADE)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.admin)



# class Address(models.Model):


#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # address_line_1 = AddressField()
    # address_line_2 = AddressField(related_name='+', blank=True, null=True)
    # is_delivery_address = models.BooleanField(_('IsDeliveryAddress'), default=False)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     insertedby = models.ForeignKey(User, related_name='+',on_delete=models.CASCADE)


# # class Vendor(models.Model):

# #     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# #     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
# #     name=models.CharField(max_length=255)
# #     address = AddressField()
# #     # _type =
# #     is_vendor_shipper = models.BooleanField(default=False)
# #     contact = PhoneField(blank=True, help_text='Contact phone number')
# #     created_at=models.DateTimeField(auto_now_add=True)
# #     updated_at=models.DateTimeField(auto_now_add=True)
# #     insertedby = models.ForeignKey(User, on_delete=models.CASCADE)

# class Shipper(models.Model):

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name=models.CharField(max_length=255)
#     contact = PhoneField(blank=True, help_text='Contact phone number')
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     insertedby = models.ForeignKey(User, related_name='+',on_delete=models.CASCADE)


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

    
class Customer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer=models.OneToOneField(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    
    

