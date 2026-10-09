from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        print("products: ", products)

        serializer = ProductSerializer(products, many=True)  # many=True если передаём больше 1-го объекта
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        
        return Response(serializer.data)
    
    