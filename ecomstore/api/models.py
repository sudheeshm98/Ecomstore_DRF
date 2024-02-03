from django.db import models

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

