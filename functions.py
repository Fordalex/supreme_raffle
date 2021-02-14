from raffles.models import Product

def get_charity_product():

    try:
        charity_product = Product.objects.get(charity=True)
    except:
        charity_product = []

    return charity_product

