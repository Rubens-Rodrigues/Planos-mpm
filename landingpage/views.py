from django.shortcuts import get_object_or_404,render
from store.models import Product, Category

# Create your views here.

def index(request):
    
    products=Product.objects.filter(status=True).values()
    categories=Category.objects.all().order_by('name')
    # if categories != None:
    #     category_page=get_object_or_404(store.Category)
    #     products=store.Product.objects.filter(category=category_page, status=True)

    context={
        'products':products,
        'categories':categories,
        'title': 'Positive-se Mulher'
    }
    
    return render(request, 'home.html', context)
