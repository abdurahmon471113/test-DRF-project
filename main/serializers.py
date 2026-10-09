from rest_framework import serializers
from .models import Product 



class SerializerProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price"]
    