from django.shortcuts import get_object_or_404,render
from store.models import Product, Category
from django.http import HttpResponseRedirect
from . forms import LeadsFomul


# Create your views here.

def index(request):
    submitted = False
    if request.method == "POST":
        lead = LeadsFomul(request.POST)
        if lead.is_valid():
            lead.save()
            return HttpResponseRedirect('/?submitted=True#form')
    else:
        lead = LeadsFomul
        if 'submitted' in request.GET:
            submitted = True
    
    products=Product.objects.filter(status=True).values()
    categories=Category.objects.all().order_by('name')
    
    context={
        'products':products,
        'categories':categories,
        'title': 'Positive-se Mulher',
        'form': LeadsFomul,
        'submitted': submitted
    }
    
    return render(request, 'home.html', context)

# def index(request):
    
#     lead = LeadsForm(request.POST)
#     new_lead = lead.save()