from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from store import models as store

# Create your views here.

def index(request):
    
    products=store.Product.objects.filter(status=True).values()
    val = len(products)
    categories=store.Category.objects.all().order_by('name')
    # if categories != None:
    #     category_page=get_object_or_404(store.Category)
    #     products=store.Product.objects.filter(category=category_page, status=True)

    context={
        'products':products,
        'categories':categories,
        'title': 'Positive-se Mulher'
    }
    
    return render(request, 'home.html', context)

def checkout(request, product_id):
    product = store.Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'checkout.html', context)