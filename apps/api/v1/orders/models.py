from django.db import models
from ..products.models import Product
from ..accounts.models import User, Address



class Order(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    totalprice = models.PositiveIntegerField()
    PaymentId
    date = models.DateTimeField(auto_now_add=True)
    delivery_address_id = models.OneToOneField(Address,on_delete=models.CASCADE)
    status = models.BooleanField(_('Order status'), default=False)
    shipment_status_id = 
    invoice_number =


class OrderStatus(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=255)

