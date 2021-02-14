from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150, default="")
    description = models.CharField(max_length=150, default="")
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.CharField(max_length=150, default="")
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    max_tickets = models.CharField(max_length=150, default="")
    tickets_sold = models.CharField(max_length=150, default="")
    max_tickets_pp = models.CharField(max_length=150, default="")
    charity = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
