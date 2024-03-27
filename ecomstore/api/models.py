from django.contrib.auth.models import User
from django.db import models
from account.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Smartphones(models.Model):
    title = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand,related_name='smartphones',on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True,blank=True)
    image_url = models.URLField(max_length=2083)
    smartphones_available = models.BooleanField()

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Smartphones, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

