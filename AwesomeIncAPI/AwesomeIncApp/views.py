from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Country, Customer, Product, Product_Category, Installation
from .serializers import CountrySerializer, CustomerSerializer, ProductSerializer, ProductCategorySerializer, \
    InstallationSerializer


# Create your views here.

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductCategoryViewSet(ModelViewSet):
    queryset = Product_Category.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InstallationViewSet(ModelViewSet):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
