from django.db import models

# Create your models here.


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    region = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    premium_customer = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'customer'


class Product_Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'product_category'


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    reference = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    category = models.ForeignKey(Product_Category, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'product'


class Installation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    installation_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'installation'
