from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    max_tickets = models.CharField(max_length=150)
    tickets_sold = models.CharField(max_length=150)
    max_tickets_pp = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
