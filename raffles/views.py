from django.shortcuts import render
from .models import Product
from functions import get_charity_product, add_ending_time_to_product

# Create your views here.
def raffle_page(request):

    products = Product.objects.filter(charity=False)

    context = {
        'products': products,
    }

    return render(request, 'raffles/raffles.html', context)

def raffle_info_page(request, pk):

    product = Product.objects.get(pk=pk)
    product = add_ending_time_to_product(product)
    charity_product = get_charity_product()
    products = Product.objects.filter(charity=False)[:3]
    
    context = {
        'product': product,
        'products': products,
        'charity_product': charity_product,

    }

    return render(request, 'raffles/raffle_info.html',context)