from django.db import models

# Create your models here.

class Asset(models.Model):
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=200, default='')
    image_url = models.CharField(max_length=200, default='')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00 )
    note = models.CharField(max_length=256, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)