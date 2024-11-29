from django import forms
from .models import ProductList

class ProductListForm(forms.ModelForm):
    class Meta:
        model = ProductList
        fields = ['name', 'category', 'price']