from django.shortcuts import get_object_or_404,render
from store.models import Product, Category
from django.http import HttpResponseRedirect, HttpResponse
from . forms import LeadsFomul
from django.db import IntegrityError


# Create your views here.

def index(request):
    
    products=Product.objects.filter(status=True).values()
    categories=Category.objects.all().order_by('name')
    
    context={
        'products':products,
        'categories':categories,
        'title': 'Positive-se Mulher',
        'form': LeadsFomul,
    }
    
    return render(request, 'home.html', context)

def send_lead(request):
    submitted = False
    erro = False
    if request.method == "POST":
        lead = LeadsFomul(request.POST)
        try: 
            lead.is_valid()
            lead.save()
            # return HttpResponseRedirect('/?submitted=True#form')
            return HttpResponse(status=202)

        except Exception as err:
            erro = lead.errors.items
            print (err)
            # return HttpResponseRedirect(f"/?erro=True#form")
            return HttpResponse(status=409)
    else:
        lead = LeadsFomul
        if 'submitted' in request.GET:
            submitted = True
