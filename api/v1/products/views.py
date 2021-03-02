from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import ProductSerializer
from .models import Product



class ProductView(APIView):
    def get(self,request,format =None):
        items = Product.objects.all()
        serializer = ProductSerializer(items, many =True)
        return JsonResponse(serializer.data, safe =False)
 
    def post(self,request,format =None):
        data = JSONParser().parse(request)
        serializer =ItemSerializer(data = data)
 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)