from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductList



urlpatterns = [

    path('getProductsForSuggestion/',ProductList.as_view()),
    
    ]