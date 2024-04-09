from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product, Customer, Bill, BillProduct
from .serializer import ProductSerializer, CustomerSerializer, BillSerializer, BillProductSerializer, UserSerializer
from django.contrib.auth.models import User

# User Serializer
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Product Views
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

# Customer Views
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

# Bill Views
class BillList(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

class BillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

# BillProduct Views
class BillProductList(generics.ListCreateAPIView):
    queryset = BillProduct.objects.all()
    serializer_class = BillProductSerializer
    permission_classes = [IsAuthenticated]

class BillProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillProduct.objects.all()
    serializer_class = BillProductSerializer
    permission_classes = [IsAuthenticated]
