from django.db import models

# Create your models here.

class prueba(models.Model):
    nombre = models.CharField(max_length=20)

    
# class Producto(models.Model): 
 #   name = models.CharField(max_length=255)
  #  description = models.TextField()
   # price = models.DecimalField(max_digits=10, decimal_places=2)
    #image = models.CharField(max_length=255)
    #id_product_type = models.IntegerField()
    #sku = models.CharField(max_length=50)

class Usuario(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rut = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)