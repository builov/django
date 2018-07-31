from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from django.urls import reverse_lazy

from django.http import HttpResponse

from . import models

from . import forms


def index(request):
    # query = models.Product.objects.all()
    query = get_list_or_404(models.Product)

    return render(request, 'products/page.html', {'query': query})


def product_detail(request, pk):
    instance = get_object_or_404(models.Product, id=pk)

    return render(request, 'products/card.html', {'instance': instance})


def product_edit(request):

    success_url = reverse_lazy('products:index')

    form = forms.ProductForm(request.POST, request.FILES)

    if request.method == 'POST':

        if form.is_valid():

            form.save()

            #return redirect(success_url)

        print('*' * 50)

        print(form.errors)

    return render(request, 'products/edit.html', {'form': form})
