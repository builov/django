from django.shortcuts import render, get_list_or_404, get_object_or_404

from django.http import HttpResponse

from . import models

from . import forms



def index(request):

	user = request.user
	
	#query = models.Product.objects.all()
	query = get_list_or_404(models.Product)
	
	return render(request, 'products/page.html', {'query': query})
	
	
def product_detail(request, pk):

	instance = get_object_or_404(models.Product, id=pk)
	
	return render(request, 'products/card.html', {'instance': instance})

def product_edit(request):

    print('*'*50)

    print(request.POST)

    form = forms.ProductForm()

    return render(request, 'products/edit.html', {'form': form})

