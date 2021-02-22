from django.db import models
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill
from api.v1.category.models import Category
from api.v1.accounts.models import Seller,User
import uuid



class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    categoryid = models.ForeignKey(Category,on_delete=models.CASCADE)
    desciption = models.TextField()
    price = models.PositiveIntegerField()
    # image = ProcessedImageField(upload_to='BackgroundImages/',
    #                             processors=[ResizeToFill(550, 550)],
    #                             format='JPEG',
    #                             options={'quality': 60},
    #                             blank=True,
    #                             null=True)
    by_seller =models.ForeignKey(Seller, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    insertedby = models.ForeignKey(User, on_delete=models.CASCADE)