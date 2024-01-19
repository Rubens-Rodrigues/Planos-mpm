from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("send_lead", views.send_lead, name="send_lead"),
]