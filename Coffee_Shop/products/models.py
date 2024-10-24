from django.db import models

# Create your models here.

class Product (models.Model):
    name= models.TextField(max_length=200,verbose_name="nombre")
    description= models.TextField(max_length=300,name="Descripción")
    price=models.DecimalField(max_length=2, verbose_name="Precio")
    available=models.BooleanField(default=True)
    photo=models.ImageField(upload_to="logos", null=True,blank=True, verbose_name= "Fotos")

    def __str__(self):
        return self.name