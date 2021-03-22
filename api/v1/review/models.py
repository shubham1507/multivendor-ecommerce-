from django.db import models
from api.v1.accounts.models import User
import uuid


# Create your models here.


class Review(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User,default=uuid.uuid4,on_delete=models.CASCADE)
    rating  = models.PositiveIntegerField()
    comment = models.CharField(max_length=255,default='its good')
    question = models.CharField(max_length=255,default='')
    answer   = models.CharField(max_length=255,default='')

