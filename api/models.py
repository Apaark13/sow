# myapp/models.py
from django.db import models

class Term(models.Model):
    content = models.TextField()
    language = models.CharField(max_length=50)

class PriceList(models.Model):
    article_no = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    inprice = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    instock = models.PositiveIntegerField()
    description = models.TextField()
