from django.shortcuts import render
from . models import Product

def checkout(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'checkout.html', context)