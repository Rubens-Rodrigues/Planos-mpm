from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
    details=models.CharField(max_length=200)
    slug=models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField(auto_now=True)
    price_total=models.DecimalField(max_digits=6,decimal_places=2)
    price_discount=models.DecimalField(max_digits=6,decimal_places=2)
    price_recurency=models.DecimalField(max_digits=6,decimal_places=2)
    type_recurency=models.CharField(max_length=10)
    observation=models.CharField(max_length=100)
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    status=models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.name