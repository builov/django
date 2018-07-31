from django import forms
from . import models

class ProductForm(forms.ModelForm):

    class Meta:

        model = models.Product
        fields = ['name', 'category', 'image', 'content', 'cost']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'category': forms.widgets.Select(attrs={'class': 'form-control'}),
            'image': forms.widgets.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'content': forms.widgets.Textarea(attrs={'class': 'form-control'}),
            'cost': forms.widgets.NumberInput(attrs={'class': 'form-control'})
        }

