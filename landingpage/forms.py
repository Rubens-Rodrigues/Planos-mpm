from django import forms
from django.forms import ModelForm
from . models import LeadsForm, TITLE_CHOICES

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
            'phone': forms.TextInput(attrs={'placeholder': 'Seu Whatsapp - (99) 9999-9999', 'pattern': '[0-9]{2} [0-9]{5}-[0-9]{4}', 'title': 'Informe um número de telefone válido'}),
            'leadsource': forms.TextInput(attrs={'type': 'hidden', 'value': 'Landing Page'}),
        }