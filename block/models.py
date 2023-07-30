from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.first_name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    details = models.TextField(max_length=400, null=True)
    price = models.FloatField(default=0)
    digital = models.BooleanField(default=False, blank=False)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def remove_product(self, product):
        self.products.remove(product)

    def __str__(self):
        return str(self.id)

class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, blank=True)

class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
