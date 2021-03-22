from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer




# class ProductView(APIView):
#     def get(self,request,format =None):
#         items = Product.objects.all()[:5]
#         serializer = ProductSerializer(items, many =True)
#         return JsonResponse(serializer.data, safe =False)
 
#     def post(self,request,format =None):
#         data = JSONParser().parse(request)
#         serializer =ProductSerializer(data = data)
 
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status = status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

