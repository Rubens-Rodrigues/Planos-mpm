from django.db import models
from cpf_field.models import CPFField

class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
    details=models.CharField(max_length=200)
    slug=models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nome produto")
    description=models.TextField(verbose_name="Descrição")
    date=models.DateField(auto_now=True)
    price_total=models.DecimalField(max_digits=6,decimal_places=2, verbose_name="Preço normal")
    price_discount=models.DecimalField(max_digits=6,decimal_places=2, verbose_name="Preço com desconto")
    price_recurency=models.DecimalField(max_digits=6,decimal_places=2, verbose_name="Preço recorrente")
    type_recurency=models.CharField(max_length=10, verbose_name="Tipo de recorrência")
    observation=models.CharField(max_length=100, verbose_name="Observação")
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING, verbose_name="Categoria")
    status=models.BooleanField(default=True, verbose_name="Ativo")
    
    
    def __str__(self) -> str:
        return self.name
    
class Person(models.Model):
    nome=models.CharField(max_length=100, null=False, blank=False, verbose_name="Nome completo")
    nickname=models.CharField(max_length=15, verbose_name="Apelido")  
    email=models.EmailField(max_length=200, null=False, blank=False, verbose_name="E-mail")
    phone=models.CharField(max_length=16, verbose_name="Celular")
    document_number=models.CharField(max_length=20, default="", unique=True, null=False, verbose_name="Numero documento")
    document_type=models.CharField(max_length=5, default="CPF", null=False, verbose_name="Tipo documento")
    location=models.CharField(max_length=100, verbose_name="Endereço")
    country=models.CharField(max_length=50, verbose_name="Pais")
    city=models.CharField(max_length=100, verbose_name="Cidade")
    region=models.CharField(max_length=80, verbose_name="Estado")
    cep=models.CharField(max_length=9, verbose_name="CEP")
    date_birth=models.DateField(null=True,verbose_name="Data de nascimento")
    photo_perfil=models.ImageField(upload_to="person")

    def __str__(self) -> str:
        return self.nome

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=False, verbose_name="Produto")
    client=models.ForeignKey(Person, on_delete=models.DO_NOTHING, verbose_name="Cliente")
    payment_method=models.CharField(max_length=20, null=False, verbose_name="Metodo de pagamento")
    payed_status=models.CharField(max_length=10, null=False, verbose_name="Status pagamento")
    installments=models.CharField(max_length=2, verbose_name="Numero de parcelas")
    id_checkout_payment=models.CharField(max_length=50, null=True, verbose_name="Id pagamento")
    amount_payed=models.DecimalField(max_digits=6,decimal_places=2, null=False, verbose_name="Valor total")
    date_payment=models.DateTimeField(verbose_name="Data pagamento")
    last_for_digits_card=models.CharField(max_length=4, verbose_name="Ultimos 4 digitos do cartão")
    
        
    def __str__(self) -> str:
        return self.name