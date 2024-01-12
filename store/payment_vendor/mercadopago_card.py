
import mercadopago

class MercadoPagoPayment():
    
    def __init__(self, transaction_amount, token, description, installments, payment_method_id, payer_email, payer_id_type, payer_number):
        self.transation_amount = transaction_amount
        self.token = token
        self.description = description
        self.installments = installments
        self.payment_method_id = payment_method_id
        self.payer_email = payer_email
        self.payer_id_type = payer_id_type
        self.payer_number = payer_number

    def makePayment(self):
        
        sdk = mercadopago.SDK('TEST-')
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
            'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
        }
        
        preference_data = {
            "back_urls": {
                "success": "https://www.tu-sitio/success",
                "failure": "https://www.tu-sitio/failure",
                "pending": "https://www.tu-sitio/pendings"
            },
            "auto_return": "approved",
            "items": [
                {
                "title": f"Pagamento {self.description}",
                "description": "",
                "picture_url": "",
                "category_id": "",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": float(self.transation_amount)
                }
            ],
        }

        payment_data = {
            "transaction_amount": float(self.transation_amount),
            "token": self.token,
            "description": self.description,
            "installments": int(self.installments),
            "payment_method_id": self.payment_method_id,
            "payer": {
                "email": self.payer_email,
                "identification": {
                    "type": self.payer_id_type, 
                    "number": self.payer_number
                }
            }
        }
        
        # try:
        payment_response = sdk.payment().create(payment_data, request_options)
        payment_preference = sdk.preference().create(preference_data)
        payment = payment_response["response"]
        print("status =>", payment["status"])
        print("additional info =>", payment_preference['status'])
        print("id=>", payment["id"])
        return payment
        # except:
        #     print(f"Algo deu errado com o pagamento, status do pagamento { payment_response }")
        #     return "Erro pagamento"
        
        
