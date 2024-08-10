# orders/models.py
from django.conf import settings
from django.db import models
from products.models import Products


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Products)

