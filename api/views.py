from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer




class ProductAPIView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        
        # Validate data; automatically raises a 400 Bad Request if validation fails
        serializer.is_valid(raise_exception=True)
        
        # Save the valid instance to the database
        serializer.save()
        
        # Return serialized database data alongside a 201 Created status
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
        
