from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    selling_price = models.CharField(max_length=30)
    mrp = models.CharField(max_length=30)
    image = models.FileField(blank=True)

class Meta:
    db_table = 'Products'