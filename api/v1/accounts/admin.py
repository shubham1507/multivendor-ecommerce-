from django.contrib import admin
from .models import User,Seller,Customer


@admin.register(User,Seller,Customer)
class AppAdmin(admin.ModelAdmin):
    pass