from django.shortcuts import render
from .models import Product
from functions import get_charity_product, add_details_to_products

# Create your views here.
def raffle_page(request):

    products = Product.objects.filter(charity=False)

    context = {
        'products': add_details_to_products(products),
    }

    return render(request, 'raffles/raffles.html', context)

def raffle_info_page(request, pk):

    product = Product.objects.get(pk=pk)
    charity_product = get_charity_product()
    products = Product.objects.filter(charity=False)[:3]
    
    context = {
        'product': add_details_to_products(product),
        'products': add_details_to_products(products),
        'charity_product': add_details_to_products(charity_product),
    }

    return render(request, 'raffles/raffle_info.html',context)