from django.shortcuts import render
from raffles.models import Product
from functions import get_charity_product, add_details_to_products

# Create your views here.
def home_page(request):

    charity_product = get_charity_product()
    products = Product.objects.filter(charity=False)[:3]

    context = {
        'charity_product': add_details_to_products(charity_product),
        'products': add_details_to_products(products),
    }

    return render(request, 'home/home.html', context)