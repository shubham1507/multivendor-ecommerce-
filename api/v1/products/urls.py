from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductView
# from rest_framework import routers

# router = routers.DefaultRouter()


urlpatterns = [

    path('',ProductView.as_view())
    ]