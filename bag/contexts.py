from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag = request.session.get('bag', {}) 
    grand_total = request.session.get('grand_total', 0) 
    total_tickets = request.session.get('total_tickets', 0) 

    context = {
        'bag_items': bag,
        'grand_total': grand_total,
        'total_tickets': total_tickets,
    }

    return context