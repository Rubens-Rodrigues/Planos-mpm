from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from . models import Product, Person, Order
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
        
        payment_process = MercadoPagoPayment()
        response_payment = payment_process.makePayment(amount, token, product_name, installments, payment_method, email, identification_type, identification_number)
        
        response_data = {}
        if 'id' in response_payment:
            response_data['id'] = response_payment['id']
            id_payment=response_payment['id']
        else: 
            response_data['id'] = ""
            id_payment=""
        
        client = Person(nome=email, email=email, document_number=identification_number, document_type=identification_type)
        client_save = client.save()
        print(client_save)
        order = Order(product=product, client=client_save, payment_method=payment_method, 
                      payed_status=response_payment['status'], installments=response_payment['installments'],
                      id_checkout_payment=id_payment, amount_payed=response_payment['transaction_details']['total_paid_amount'],
                      date_payment=response_payment['date_created'], last_for_digits_card=response_payment['card']['last_four_digits'])
        order.save()

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return render(request, '404.html')

def payment(request):
    print(request.GET['id_payment'])
    if 'id_payment' in request.GET:
        status_detail ={
            'Accredited': 'credited payment.',
            'pending_contingency': 'O pagamento está sendo processado',
            'pending_review_manual': 'o pagamento está sob revisão para determinar sua aprovação ou rejeição.',
            'cc_rejected_bad_filled_date': 'Data de validade incorreta',
            'cc_rejected_bad_filled_other': 'Detalhes incorreto do cartão',
            'cc_rejected_bad_filled_security_code': 'CVV incorreto',
            'cc_rejected_blacklist': 'O cartão está em uma lista de roubo/reclamações/fraude.',
            'cc_rejected_call_for_authorize': 'O meio de pagamento carece de autorização prévia do valor da operação.',
            'cc_rejected_card_disabled': 'O cartão está inativo.',
            'cc_rejected_duplicated_payment': 'Transação duplicada.',
            'cc_rejected_high_risk': 'Rejeitado por fraude.',
            'cc_rejected_insufficient_amount': 'Saldo insuficiente.',
            'cc_rejected_invalid_installments': 'Numero de parcelas inválida.',
            'cc_rejected_max_attempts': 'Excedido o numero máximo de tentativas.',
            'cc_rejected_other_reason': 'Erro generico.',
        }
        payment_id = request.GET['id_payment']
        payment = MercadoPagoPayment().getPayment(payment_id)
        print(payment)
        if payment['status'] == 200:
            context = {
                'status_payment': payment['response']['status'],
                'email': payment['response']['payer']['email'],
                'document_number': payment['response']['card']['cardholder']['identification']['number'],
                'document_type': payment['response']['card']['cardholder']['identification']['type'],
                'last_for_digits_card': payment['response']['card']['last_four_digits'],
                'date_payment': payment['response']['date_created'],
                'amount_payed': payment['response']['transaction_details']['total_paid_amount'],
                'product_payed': payment['response']['description'],
                'payment_method': payment['response']['payment_method']['type'],
                'installments': payment['response']['installments'],
            }
        else:
            
            context = {
                'status_payment': 'Pagamento não encontrado'
            }
        
        return render(request, 'payments.html', context)