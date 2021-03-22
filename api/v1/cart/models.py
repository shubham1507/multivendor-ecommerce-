from django.db import models
import uuid
from api.v1.products.models import Product
from api.v1.accounts.models import Customer



class Cart(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,related_name="user_id",default=1, on_delete=models.CASCADE)
    customer_email = models.EmailField(max_length=255, default = 'example@gmail.com',unique=True)
    # user_id = models.ForeignKey(User,related_name="user_id", on_delete=models.CASCADE)
    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return "{}".format(Product)
       


    
