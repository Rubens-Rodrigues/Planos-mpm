from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from . models import Product
from .payment_vendor.mercadopago_card import MercadoPagoPayment
import logging
import json

logger = logging.getLogger("store.views")

def checkout(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'checkout_bricks.html', context)

def process_payment(request):
    if request.method == "POST":
        raw_body_decoded = request.body.decode('utf-8')
        data = json.loads(raw_body_decoded)
        
        product_id = data['post_service']['product_id']
        product = Product.objects.get(id=product_id)

        token = data['cardFormData']['token']
        amount = product.price_discount
        product_name = product.name
        installments = data['cardFormData']['installments']
        identification_type = data['cardFormData']['payer']['identification']['type']
        identification_number = data['cardFormData']['payer']['identification']['number']
        email = data['cardFormData']['payer']['email']
        payment_method = data['cardFormData']['payment_method_id']
        
        payment_process = MercadoPagoPayment(amount, token, product_name, installments, payment_method, email, identification_type, identification_number)
        response_payment = payment_process.makePayment()
        
        #TODO: add função para cadastrar o usuario no banco banco de dados
                
        context = {
            'response': response_payment
        }

        return render(request, 'payments.html', context)
    else:
        return render(request, 'erropayment.html', context)
