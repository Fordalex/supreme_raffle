from django.shortcuts import render
from raffles.models import Product

# Create your views here.
def home_page(request):

    charity_product = Product.objects.get(charity=True)

    context = {
        'charity_product': charity_product,
    }

    return render(request, 'home/home.html', context)