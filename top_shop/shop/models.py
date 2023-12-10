from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()

class Orders(models.Model):
    name = models.CharField(max_length=20)
    customer = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    user_id = models.BigIntegerField()
    type = models.CharField(max_length=255, choices=[('online', 'Online'), ('offline', 'Offline')])
    status = models.CharField(max_length=255, choices=[('active', 'Active'), ('completed', 'Completed'),
                                                       ('cancelled', 'Cancelled')])

class Order_items(models.Model):
    order_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    count = models.IntegerField()
    discount = models.FloatField()
    cost = models.FloatField()