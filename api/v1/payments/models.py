from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from api.v1.accounts.models import User
# from api.v1.orders.models import Order


# Create your models here.

class PaymentOption(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    insertedby = models.ForeignKey(User,related_name="+", on_delete=models.CASCADE)

    def __str__(self):

        return str(self.insertedby)


class PaymentStatus(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)


class PaymentMode(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)


class Payment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # order_id = models.OneToOneField(Order,on_delete=models.CASCADE)
    payment_mode_id  =models.ForeignKey(PaymentMode, on_delete=models.CASCADE)
    payment_status_id = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE)
    payment_option_id = models.ForeignKey(PaymentOption, on_delete=models.CASCADE)

