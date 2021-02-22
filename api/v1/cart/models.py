from django.db import models
import uuid
from api.v1.products.models import Product
from api.v1.accounts.models import User



class Cart(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,related_name="user_id", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    insertedby = models.ForeignKey(User,related_name="insertedby", on_delete=models.CASCADE)


    def __str__(self):

        return "{}".format(Product)
       


    
