# Generated by Django 3.2.9 on 2021-11-12 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AwesomeIncApp', '0002_auto_20211112_0952'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='country',
            table='country',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='installation',
            table='installation',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
        migrations.AlterModelTable(
            name='product_category',
            table='product_category',
        ),
    ]
