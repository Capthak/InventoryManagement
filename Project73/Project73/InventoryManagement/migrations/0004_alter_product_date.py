# Generated by Django 3.2.7 on 2021-09-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryManagement', '0003_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(),
        ),
    ]