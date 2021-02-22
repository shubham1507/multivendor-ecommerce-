from django.contrib import admin
from .models import User,Seller,Customer,Admin,Address,Shipper

admin.site.register(User)

admin.site.register(Admin)

# class Admin(models.Model):
# @admin.register(User,Seller,Customer,Admin,Address,Shipper)
# class AppAdmin(admin.ModelAdmin):
#     pass