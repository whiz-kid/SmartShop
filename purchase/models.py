# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Userdetails(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic = models.CharField(max_length=200,default='../../static/purchase/images/')
    address = models.CharField(max_length=2000)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return  self.customer.username + " has number " + str(self.phone_number)
    


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

class Favorite(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Item,on_delete=models.CASCADE)
    add_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.customer.username + ' * ' + self.product.name 

class Like(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Item,on_delete=models.CASCADE)
    add_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.customer.username + ' liked ' + self.product.name


class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Cart,on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.customer.username + ' ordered ' + self.product.product.category.category