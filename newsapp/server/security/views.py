from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login

from . import forms


class LoginView(FormView):

    form_class = forms.LoginForm

    template_name = 'security/login.html'

    success_url = reverse_lazy('products:list')


    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            login(request, form.user)

            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})

class SigninView(FormView):

    template_name = 'security/signin.html'

    success_url = reverse_lazy('products:list')

    form_class = forms.SigninForm




