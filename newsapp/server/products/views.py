from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import View, CreateView, ListView, DetailView

from . import models

from . import forms

class ProductList(ListView):

    queryset = get_list_or_404(models.Product)

    context_object_name = 'query'

    template_name = 'products/page.html'



class ProductDetail(DetailView):

    model = models.Product

    context_object_name = 'instance'

    template_name = 'products/card.html'


class ProductCreate(CreateView):

    model = models.Product

    form_class = forms.ProductForm

    template_name = 'products/edit.html'

    success_url = '/product/create'

