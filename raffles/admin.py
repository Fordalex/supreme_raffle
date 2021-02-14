from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'image', 'price', 'end_date', 'max_tickets', 'tickets_sold', 'max_tickets_pp', 'charity',)

    list_display = ('name','end_date', 'charity')

admin.site.register(Product, ProductAdmin)
