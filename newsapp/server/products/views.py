from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import View, CreateView, ListView, DetailView

from . import models

from . import forms

class ProductList(ListView):

    context_object_name = 'query'

    template_name = 'products/page.html'

    queryset = get_list_or_404(models.Product)


class ProductDetail(DetailView):

    model = models.Product

    context_object_name = 'instance'

    template_name = 'products/card.html'


class ProductCreate(CreateView):

    model = models.Product

    form_class = forms.ProductForm

    success_url = '/product/create'

    template_name = 'products/edit.html'

