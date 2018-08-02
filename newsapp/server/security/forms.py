from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(label='Login', required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(label='Password', required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))


