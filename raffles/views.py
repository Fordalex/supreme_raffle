from django.shortcuts import render
from .models import Product

# Create your views here.
def raffle_page(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'raffles/raffles.html', context)

def raffle_info_page(request, pk):

    product = Product.objects.get(pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'raffles/raffle_info.html',context)