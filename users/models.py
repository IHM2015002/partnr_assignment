import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=50,blank=False)
    phone = models.CharField(max_length=50,blank=False)
    password = models.CharField(max_length=50,blank=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['name', 'phone']





    


