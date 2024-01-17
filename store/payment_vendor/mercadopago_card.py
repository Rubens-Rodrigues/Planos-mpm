
import mercadopago
import os
from dotenv import load_dotenv

class MercadoPagoPayment():
    
    load_dotenv()
    
    def __init__(self):
        SECRET_KEY = os.getenv('SECRET_KEY')
        self.sdk = mercadopago.SDK(SECRET_KEY)
        
    def getPayment(self, id_payment):
        payment = self.sdk.payment().get(id_payment)
        return payment

    def makePayment(self, transaction_amount, token, description, installments, payment_method_id, payer_email, payer_id_type, payer_number):
        
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
            'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
        }
        
        preference_data = {
            "items": [
                {
                "title": f"Pagamento {description}",
                "description": "",
                "picture_url": "",
                "category_id": "",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": float(transaction_amount)
                }
            ],
        }
        payment_data = {
            "transaction_amount": float(transaction_amount),
            "token": token,
            "description": description,
            "installments": int(installments),
            "payment_method_id": payment_method_id,
            "payer": {
                "email": payer_email,
                "identification": {
                    "type": payer_id_type, 
                    "number": payer_number
                }
            }
        }
        
        payment_response = self.sdk.payment().create(payment_data, request_options)
        payment_preference = self.sdk.preference().create(preference_data)
        payment = payment_response["response"]
        print("status =>", payment["status"])
        print("additional info =>", payment_preference['status'])
        # print("Object", payment)
        return payment
        
        
