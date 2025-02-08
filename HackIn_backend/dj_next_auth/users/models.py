from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) 
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    id_card_number = models.CharField(max_length=18, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []