from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)