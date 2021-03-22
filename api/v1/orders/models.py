from django.db import models
import uuid
import datetime
from django_address.fields import AddressField
from django.utils.translation import ugettext_lazy as _
from api.v1.products.models import Product
from api.v1.accounts.models import Customer


# class ShipmentStatus(models.Model):

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     is_latest = models.BooleanField(_('Is Latest'), default=False)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     update_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):

#         return str(self.update_by)


class Order(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    cancelReason = models.CharField(max_length=255,default='delayed')
    cancelledOn = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    customer_email = models.EmailField(max_length=255, default = 'example@gmail.com',unique=True)
    customer_id = models.ForeignKey(Customer, default=uuid.uuid1(),on_delete=models.CASCADE)
    delivery_address = AddressField(default ='',verbose_name="Delivery address")
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(_('Order status'), default=False)

# class OrderStatus(models.Model):

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name  = models.CharField(max_length=255)




