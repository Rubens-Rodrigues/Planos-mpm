
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
        
        sdk = mercadopago.SDK('')
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
            'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
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
        
        payment_response = sdk.payment().create(payment_data, request_options)
        payment = payment_response["response"]
        
        print(payment)
        print("status =>", payment["status"])
        print("status_detail =>", payment["status_detail"])
        print("id=>", payment["id"])
