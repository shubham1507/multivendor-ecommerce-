from django.db import models
import uuid
from address.models import AddressField
from django.utils.translation import ugettext_lazy as _
from api.v1.products.models import Product
from api.v1.accounts.models import User
# from api.v1.payments.models import Payment


class ShipmentStatus(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_address = AddressField()
    is_latest = models.BooleanField(_('Is Latest'), default=False)
    updated_at=models.DateTimeField(auto_now_add=True)
    update_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return str(self.update_by)


class Order(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    totalprice = models.PositiveIntegerField()
    # payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(_('Order status'), default=False)
    shipment_status_id = models.ForeignKey(ShipmentStatus, on_delete=models.CASCADE)
    invoice_number = models.PositiveIntegerField()

class OrderStatus(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=255)




