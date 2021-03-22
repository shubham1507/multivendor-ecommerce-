from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CarouselView


urlpatterns = [

    path('GetCarouselData/',CarouselView.as_view())
    ]