from django.contrib import admin
from . models import LeadsForm, PreInscricao

@admin.register(LeadsForm)
class LeadsFormAdmin(admin.ModelAdmin):
    list_display=('nome','email','phone','leadsource')
    search_fields=('nome',)
    
@admin.register(PreInscricao)
class LeadsFormAdmin(admin.ModelAdmin):
    list_display=('nome','telefone')
    search_fields=('nome',)