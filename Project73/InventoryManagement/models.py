from django.db import models


class Product(models.Model):
    date = models.DateField()
    provider=models.CharField(max_length=100)
    name_product=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.IntegerField()
    amount=models.FloatField()
    stock=models.IntegerField()

    def __str__(self):
        return self.name_product


