from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:product_id>',views.checkout,name="checkout"),
    path('process_payment', views.process_payment, name='process_payment'),
]

   