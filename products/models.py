from django.db import models
from users.models import Users

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100,blank=False)
    product_type = models.CharField(max_length=50)
