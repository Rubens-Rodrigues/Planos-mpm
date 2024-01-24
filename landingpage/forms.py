from django import forms
from django.forms import ModelForm
from . models import LeadsForm, TITLE_CHOICES, PreInscricao

class LeadsFomul(ModelForm):
    class Meta:
        model = LeadsForm
        fields = ('nome', 'email', 'phone', 'leadsource')
        labels = {
            'nome': '',
            'email': '',
            'phone': '',
            'leadsource': '',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome', 'class':'lead-form'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Seu melhor e-mail'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Seu Whatsapp - (99) 9999-9999', 'title': 'Informe um número de telefone válido'}),
            'leadsource': forms.TextInput(attrs={'type': 'hidden', 'value': 'Landing Page'}),
        }

class PreInscricaoForm(ModelForm):
    class Meta:
        model = PreInscricao
        fields = ('__all__')
        labels = {
            'nome': 'Seu nome*',
            'telefone': 'Número de telefone*',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
            'telefone': forms.TextInput(attrs={'placeholder': '11981281099'}),
        }