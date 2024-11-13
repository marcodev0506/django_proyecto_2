from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre')
    description = forms.CharField(max_length=300, label='Descripción')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    available = forms.BooleanField(initial=True, label='Disponible', required=False)
    photo = forms.ImageField(label='Foto', required=False)

    def save(self):
        data = self.cleaned_data
        Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            available=data['available'],
            photo=data['photo']
        )