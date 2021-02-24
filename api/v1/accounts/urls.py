from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import SellerRegistrationView, CustomerRegistrationView


app_name = 'accounts'
urlpatterns = [

    #Registration Urls
    path('registration/seller/', SellerRegistrationView.as_view(), name='register-seller'),
    path('registration/customer/', CustomerRegistrationView.as_view(), name='register-customer'),
    ]