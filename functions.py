from raffles.models import Product
from datetime import datetime, timezone

def get_charity_product():

    try:
        charity_product = Product.objects.get(charity=True)
    except:
        charity_product = []

    return charity_product

def add_ending_time_to_product(product):

    time_remaining = product.end_date - datetime.now(timezone.utc)
    time_remaining_array = str(time_remaining).split()
    time_remaining_days = time_remaining_array[0]
    
    try:
        time_array = time_remaining_array[2].split(':')
    except:
        time_array = str(time_remaining).split(':')
        time_remaining_days = 0

    time_remaining = {
        'days': int(time_remaining_days),
        'hours': int(time_array[0]),
        'minutes': int(time_array[1]),
        'seconds': int(float(time_array[2])),
    }

    remaining_tickets = int(product.max_tickets) - int(product.tickets_sold)

    sold_percentage = int(product.max_tickets) / 100 

    formatted_product = {
        'name': product.name,
        'description': product.description,
        'image': product.image,
        'price': product.price,
        'end_date': product.end_date,
        'max_tickets': product.max_tickets,
        'tickets_sold': product.tickets_sold,
        'max_tickets_pp': product.max_tickets_pp,
        'charity': product.charity,
        'time_remaining': time_remaining,
        'remaining_tickets': remaining_tickets,
        'sold_percentage': sold_percentage,
    }

    return formatted_product