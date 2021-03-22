from rest_framework import serializers
from .models import CarouselContent

class CarouselContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselContent
        fields = '__all__'