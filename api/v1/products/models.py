from django.db import models
from django.utils.translation import gettext as _
from django_postgres_extensions.models.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from api.v1.category.models import Category
from api.v1.varient.models import Varient
from api.v1.accounts.models import Seller,User
import uuid



class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    varient_id = models.ForeignKey(Varient,default=1,on_delete=models.CASCADE)
    category_path = ArrayField(models.CharField(max_length=515), null=True, blank=True)
    category_rank = models.PositiveIntegerField(default=1)
    is_featured = models.BooleanField(_('is featured'), default=False)
    desciption = models.TextField()
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=255,default='')
    more_prop = ArrayField(models.CharField(max_length=515), null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    tags  = models.CharField(max_length=255,default='')
    by_seller =models.ForeignKey(Seller, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    insertedby = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return "{}".format(self.product_name)