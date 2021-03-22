# from rest_framework.views import APIView
# from django.http import JsonResponse
from rest_framework import generics
from .serializers import CarouselContentSerializer
from .models import CarouselContent

# Create your views here.


# class CarouselView(APIView):
#     def get(self,request,format =None):
#         items = CarouselContent.objects.all()
#         serializer = CarouselContentSerializer(items, many =True)
#         return JsonResponse(serializer.data, safe =False)
 
#     def post(self,request,format =None):
#         data = JSONParser().parse(request)
#         serializer =CarouselContentSerializer(data = data)
 
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)



class CarouselView(generics.ListCreateAPIView):
    queryset = CarouselContent.objects.all()
    serializer_class = CarouselContentSerializer
