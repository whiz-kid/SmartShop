# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Item(models.Model):

    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    logo = models.CharField(max_length=500,default='../../static/purchase/images/')

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Item,on_delete=models.CASCADE)
    add_date = models.DateTimeField(default=timezone.now())
 
    def __str__(self):
        return self.customer.username + ' - ' + self.product.name
