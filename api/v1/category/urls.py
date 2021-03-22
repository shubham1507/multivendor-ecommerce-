from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryView

# from rest_framework import routers

# router = routers.DefaultRouter()


# urlpatterns = [

#     path('', include(router.urls))
#     ]



urlpatterns = [

    path('getAllCategories/',CategoryView.as_view())
    ]