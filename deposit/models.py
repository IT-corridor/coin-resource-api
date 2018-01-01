from django.db import models
from django.conf import settings

# Create your models here.


class Deposit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_deposits', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.id
