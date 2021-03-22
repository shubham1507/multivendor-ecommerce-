from django.db import models
import uuid
from api.v1.accounts.models import User



class Category(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label= models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    parent_id = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    key = models.PositiveIntegerField()
    # desciption = models.TextField(default='', blank=True)
    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now_add=True)
    # insertedby = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    

    # def __str__(self):

    #     return str(self.category_name)




