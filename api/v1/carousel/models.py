from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class CarouselContent(models.Model):

    heading = models.CharField(max_length=255,default='main')
    paragraph = models.CharField(max_length=255,default='para')
    active = models.BooleanField(default=False)
    expiry = models.DateField(_("Date"), default=datetime.date.today)