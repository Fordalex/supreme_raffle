from django.shortcuts import render
from raffles.models import Product
from functions import get_charity_product

# Create your views here.
def home_page(request):

    charity_product = get_charity_product()
    products = Product.objects.filter(charity=False)[:3]

    context = {
        'charity_product': charity_product,
        'products': products
    }

    return render(request, 'home/home.html', context)