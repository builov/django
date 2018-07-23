from django.shortcuts import render

from django.http import HttpResponse

from . import models

def index(request):

	user = request.user
	
	query = models.Product.objects.all()
	
	return render(request, 'products/index.html', {'query': query})