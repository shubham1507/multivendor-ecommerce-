from django.db import models
from ..accounts.models import Seller



class Category(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name= models.CharField(max_length=255)
    desciption = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    insertedby = models.ForeignKey(Seller, on_delete=models.CASCADE)




