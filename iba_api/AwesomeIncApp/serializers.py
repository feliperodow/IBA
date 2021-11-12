from rest_framework import serializers
from .models import Country, Customer, Product_Category, Product, Installation


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'region']


class CustomerSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())

    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'premium_customer', 'country')


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Product_Category.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'reference', 'name', 'price', 'category_id')


class InstallationSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = Installation
        fields = ('id', 'name', 'description', 'product_id', 'customer_id', 'installation_date')
