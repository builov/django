from django import forms

class ProductForm(forms.Form):

    name = forms.CharField(label='name', required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='image', required=False, widget=forms.widgets.ClearableFileInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='name', required=True, widget=forms.widgets.Textarea(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(label='name', required=True, widget=forms.widgets.Select(attrs={'class': 'form-control'}))
    cost = forms.DecimalField(label='name', required=True, widget=forms.widgets.NumberInput(attrs={'class': 'form-control'}))
