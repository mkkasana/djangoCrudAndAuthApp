from rest_framework import serializers
from .models import Product, Customer, Bill, BillProduct
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    # Nested Serializer to display customer details in each bill
    customer = CustomerSerializer(read_only=True)
    
    class Meta:
        model = Bill
        fields = '__all__'

class BillProductSerializer(serializers.ModelSerializer):
    # Nested Serializer to display product details in each bill product
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = BillProduct
        fields = '__all__'
