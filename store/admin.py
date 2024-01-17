from django.contrib import admin
from . models import Category, Product, Person

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price_total','price_discount')
    search_fields=('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(Person)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('nome','document_number')
    search_fields=('nome',)