from django.shortcuts import render, get_object_or_404, redirect
from . models import Product
from .payment_vendor.mercadopago_card import MercadoPagoPayment
import logging
import json

logger = logging.getLogger("store.views")

def checkout(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'checkout.html', context)

def process_payment(request):
    if request.method == "POST":
        raw_body_decoded = request.body.decode('utf-8')
        data = json.loads(raw_body_decoded)
        
        product_id = data['product_id']
        product = Product.objects.get(id=product_id)

        token = data['token']
        amount = product.price_discount
        product_name = product.name
        installments = data['installments']
        identification_type = data['payer']['identification']['type']
        identification_number = data['payer']['identification']['number']
        email = data['payer']['email']
        payment_method = data['payment_method_id']
        print(data)
        
        try:
            payment_process = MercadoPagoPayment(amount, token, product_name, installments, payment_method, email, identification_type, identification_number)
            response_payment = payment_process.makePayment()
        except:
            print("Algo deu errado com o pagamento")
        
        context = {
            'response': response_payment
        }

        return render(request, 'payments.html', context)
    else:
        return render(request, 'erropayment.html')
