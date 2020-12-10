from django.db import models
from users.models import CustomUser

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=60)
    balance = models.FloatField()

