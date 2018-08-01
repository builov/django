from django.urls import path
from . import views


urlpatterns = [
	path('', views.ProductList.as_view(), name='list'),
	path('product/create', views.ProductCreate.as_view(), name='create'),
	path('product/<int:pk>/', views.ProductDetail.as_view(), name='detail')
]
