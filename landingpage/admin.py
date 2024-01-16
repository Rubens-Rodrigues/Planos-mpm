from django.contrib import admin
from . models import LeadsForm

@admin.register(LeadsForm)
class LeadsFormAdmin(admin.ModelAdmin):
    list_display=('nome','email','phone','leadsource')
    search_fields=('nome',)
    
