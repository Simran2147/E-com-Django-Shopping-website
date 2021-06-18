from django.db import models
from django.urls import reverse

# create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('produits:product_list_by_category', args=[self.slug])



class Product(models.Model):
    Category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    nameProd = models.CharField(max_length=225, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description =  models.TextField(blank=True)
    price = models.FloatField(default=True)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/%Y%m%d',blank=True)


    def __str__(self):
        return self.nameProd

    def get_absolute_url(self):
        return reverse('produits:product_detail', args=[self.pk, self.slug])

