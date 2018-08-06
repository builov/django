from django.urls import path
from . import views

app_name = 'security'

urlpatterns = [
    path('/signin/', views.SigninView.as_view(), name='sign'),
    path('', views.LoginView.as_view(), name='login')
]