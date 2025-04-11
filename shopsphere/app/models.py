from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Who added to cart
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Which product
    quantity = models.PositiveIntegerField(default=1)  # How many
    added_at = models.DateTimeField(auto_now_add=True)  # When it was added

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
