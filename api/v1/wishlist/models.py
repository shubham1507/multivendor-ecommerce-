from django.db import models
import uuid
from api.v1.products.models import Product
from api.v1.accounts.models import User






class Wishlist(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)