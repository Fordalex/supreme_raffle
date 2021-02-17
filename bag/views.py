from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from raffles.models import Product

# Create your views here.
@login_required
def view_bag(request):
    return render(request, 'bag/bag.html')

@login_required
def add_to_bag(request, pk):
    # Add message to messages and add the tickets to the basket.
    product = Product.objects.get(pk=pk)
    ticketCount = request.POST.get('ticketCount')

    messages.success(request, f'Added {ticketCount} {product.name} tickets to your basket')

    # Getting items to the basket
    bag = request.session.get('bag', {})

    ticketCount = int(ticketCount)
    try:
        ticketCount += int(bag[product.name]['tickets'])
    except:
        ticketCount = int(ticketCount)

    product_info = {
        'name': product.name,
        'price': product.price,
        'tickets': int(ticketCount)
    }
    
    bag[product.name] = product_info

    request.session['bag'] = bag

    return redirect('raffle_info_page', pk)

@login_required
def empty_bag(request):
    request.session['bag'] = {}
    return redirect('home_page')