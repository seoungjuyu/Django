from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    numbers = models.CharField(max_length=15, unique=True)
    adderas = models.TextField()