from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('product/create', views.product_edit, name='create'),
	path('product/<int:pk>/', views.product_detail, name='detail')
]
