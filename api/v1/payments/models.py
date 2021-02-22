from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from api.v1.accounts.models import User
from api.v1.orders.models import Order


# Create your models here.


class Payment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.OneToOneField(Order,on_delete=models.CASCADE)
    payment_mode_id  =models.ForeignKey(PaymentMode, on_delete=models.CASCADE)
    payment_status_id = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE)
    payment_option_id = models.ForeignKey(PaymentOption, on_delete=models.CASCADE)


class PaymentOption(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
    # CardType =   ("cc","gf","db")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    insertedby = models.ForeignKey(User, on_delete=models.CASCADE)

class PaymentStatus(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)


class PaymentMode(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)



