from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True) # product name must unique
    slug            = models.SlugField(max_length=200, unique=True) # convert product name as lowercase and create hifen between two name
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products') # image path
    stock           = models.IntegerField() # how many number is present in stock
    is_available    = models.BooleanField(default=True) # is product available or not.
    category        = models.ForeignKey(Category, on_delete=models.CASCADE) # ForeignKey is used for meantain One to Many relation ship
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_url(self): # causes of uses this functions = amra jokhon product_name click korbo tokhon product_details show korbe and url hisabe first a category slug/product slug
        return reverse('product_detail', args=[self.category.slug, self.slug])