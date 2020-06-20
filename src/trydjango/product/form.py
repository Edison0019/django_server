from django import forms
from .models import products

class product_form(forms.ModelForm):
    class Meta:
        model = products
        fields = [
            'title',
            'description',
            'price'
        ]