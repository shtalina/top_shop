from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.TextField(null=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    name = models.CharField(max_length=20, blank=True)
    customer = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=[('online', 'Online'), ('offline', 'Offline')])
    status = models.CharField(max_length=255, choices=[('active', 'Active'), ('completed', 'Completed'),
                                                       ('cancelled', 'Cancelled')])

    def __str__(self):
        return self.customer

class Order_items(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.IntegerField()
    discount = models.FloatField(null=True)
    cost = models.FloatField()

class Cart(models.Model):
    products = models.ManyToManyField(Products, through='CartItem')

class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    order_items = models.ForeignKey(Order_items, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    image = models.TextField(null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_cart = models.IntegerField(null=True)
    count = models.IntegerField(null=True)
    discount = models.FloatField(null=True)
    cost = models.FloatField(null=True)