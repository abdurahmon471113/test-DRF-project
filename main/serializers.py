from rest_framework import serializers
from .models import Product 



class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    price = serializers.DecimalField(max_digits=12, decimal_places=0)
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        
        instance.save()
        return instance
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # class Meta:
    #     model = Product
    #     fields = ["name", "price"]
    