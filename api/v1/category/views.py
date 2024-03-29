# from rest_framework.views import APIView
# from django.http import JsonResponse
from rest_framework import generics

from .serializers import CategorySerializer
from .models import Category


# class CategoryView(APIView):
#     def get(self,request,format =None):
#         items = Category.objects.all()
#         serializer = CategorySerializer(items, many =True)
#         return JsonResponse(serializer.data, safe =False)
 
#     def post(self,request,format =None):
#         data = JSONParser().parse(request)
#         serializer =CategorySerializer(data = data)
 
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
