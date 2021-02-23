from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter()
router.register('registration', UserViewSet)


urlpatterns = [

    path('', include(router.urls))
    ]