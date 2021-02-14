from django.shortcuts import render
from .models import Product
from functions import get_charity_product

# Create your views here.
def raffle_page(request):

    products = Product.objects.filter(charity=False)
    charity_product = get_charity_product()

    context = {
        'products': products,
        'charity_product': charity_product,
    }

    return render(request, 'raffles/raffles.html', context)

def raffle_info_page(request, pk):

    product = Product.objects.get(pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'raffles/raffle_info.html',context)