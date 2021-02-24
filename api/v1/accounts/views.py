from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from .serializers import (
    SellerCustomRegistrationSerializer, CustomerCustomRegistrationSerializer
    )

class SellerRegistrationView(RegisterView):
    serializer_class = SellerCustomRegistrationSerializer


class CustomerRegistrationView(RegisterView):
    serializer_class = CustomerCustomRegistrationSerializer