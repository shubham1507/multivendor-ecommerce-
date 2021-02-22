from django.contrib import admin
from .models import User,Seller,Customer,Admin,Address,Shipper

@admin.register(User,Seller,Customer,Admin,Address,Shipper)
class AppAdmin(admin.ModelAdmin):
    pass